from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.retrieval_qa.base import RetrievalQA
from huggingface_hub import HfFolder
import os
import gradio as gr
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

def get_llm():
    model_id = 'ibm/granite-3-2-8b-instruct'

    parameters = {
    GenParams.MAX_NEW_TOKENS: 256,  # this controls the maximum number of tokens in the generated output
    GenParams.TEMPERATURE: 0.2, # this randomness or creativity of the model's responses 
    }

    url = os.getenv("IBM_URL_END_POINT")
    apikey = os.getenv("IBM_API_KEY")
    project_id = os.getenv("IBM_PROJECT_ID")

    watsonx_llm = WatsonxLLM(
        model_id=model_id,
        url=url,
        project_id=project_id,
        params=parameters,
        apikey=apikey
    )
    return watsonx_llm

def document_loader(file):
    loader = PyPDFLoader(file)
    loaded_document = loader.load()
    return loaded_document

def text_splitter(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len
    )
    chunks = text_splitter.split_documents(data)
    return chunks

def watsonx_embedding():
    url = os.getenv("IBM_URL_END_POINT")
    apikey = os.getenv("IBM_API_KEY")
    project_id = os.getenv("IBM_PROJECT_ID")

    embed_params = {
        EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: 3,
        EmbedTextParamsMetaNames.RETURN_OPTIONS: {"input_text": True}
    }
    watsonx_embedding = WatsonxEmbeddings(
        model_id="ibm/slate-125m-english-rtrvr-v2",
        url=url,
        project_id=project_id,
        params=embed_params,
        apikey=apikey
    )
    return watsonx_embedding

def vector_database(chunks):
    embedding_model = watsonx_embedding()
    vectordb = Chroma.from_documents(chunks, watsonx_embedding())
    return vectordb

def retriever(file):
    splits = document_loader(file)
    chunks = text_splitter(splits)
    vectordb = vector_database(chunks)
    retriever = vectordb.as_retriever()
    return retriever

def retriever_qa(file, query):
    llm = get_llm()
    retriever_obj = retriever(file)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever_obj,
        return_source_documents=True
    )
    response = qa.invoke(input=query)
    return response['result']

rag_application = gr.Interface(
    fn=retriever_qa,
        inputs=[
        gr.File(label="Upload PDF File", file_count="single", file_types=['.pdf'], type="filepath"),  # Drag and drop file upload
        gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here...")
    ],
    outputs=gr.Textbox(label="Answer"),
    title="RAG Bot with IBM Watsonx",
    description="Upload a PDF document and ask questions about its content. Powered by IBM Watsonx"
)
rag_application.launch()