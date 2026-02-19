import chromadb
from chromadb.utils import embedding_functions

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Creating an instance of ChromaClient to establish a connection with the Chroma database
client = chromadb.Client()
collection_name = "employee_collection"


def main():
    try:
        collection = client.create_collection(
            name=collection_name,
            metadata={"description": "A collection for storing employee data"},
            configuration={"hnsw": {"space": "cosine"}, "embedding_function": ef},
        )
        print(f"Collection created: {collection.name}")
        employees = [
            {
                "id": "employee_1",
                "name": "John Doe",
                "experience": 5,
                "department": "Engineering",
                "role": "Software Engineer",
                "skills": "Python, JavaScript, React, Node.js, databases",
                "location": "New York",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_2",
                "name": "Jane Smith",
                "experience": 8,
                "department": "Marketing",
                "role": "Marketing Manager",
                "skills": "Digital marketing, SEO, content strategy, analytics, social media",
                "location": "Los Angeles",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_3",
                "name": "Alice Johnson",
                "experience": 3,
                "department": "HR",
                "role": "HR Coordinator",
                "skills": "Recruitment, employee relations, HR policies, training programs",
                "location": "Chicago",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_4",
                "name": "Michael Brown",
                "experience": 12,
                "department": "Engineering",
                "role": "Senior Software Engineer",
                "skills": "Java, Spring Boot, microservices, cloud architecture, DevOps",
                "location": "San Francisco",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_5",
                "name": "Emily Wilson",
                "experience": 2,
                "department": "Marketing",
                "role": "Marketing Assistant",
                "skills": "Content creation, email marketing, market research, social media management",
                "location": "Austin",
                "employment_type": "Part-time",
            },
            {
                "id": "employee_6",
                "name": "David Lee",
                "experience": 15,
                "department": "Engineering",
                "role": "Engineering Manager",
                "skills": "Team leadership, project management, software architecture, mentoring",
                "location": "Seattle",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_7",
                "name": "Sarah Clark",
                "experience": 8,
                "department": "HR",
                "role": "HR Manager",
                "skills": "Performance management, compensation planning, policy development, conflict resolution",
                "location": "Boston",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_8",
                "name": "Chris Evans",
                "experience": 20,
                "department": "Engineering",
                "role": "Senior Architect",
                "skills": "System design, distributed systems, cloud platforms, technical strategy",
                "location": "New York",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_9",
                "name": "Jessica Taylor",
                "experience": 4,
                "department": "Marketing",
                "role": "Marketing Specialist",
                "skills": "Brand management, advertising campaigns, customer analytics, creative strategy",
                "location": "Miami",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_10",
                "name": "Alex Rodriguez",
                "experience": 18,
                "department": "Engineering",
                "role": "Lead Software Engineer",
                "skills": "Full-stack development, React, Python, machine learning, data science",
                "location": "Denver",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_11",
                "name": "Hannah White",
                "experience": 6,
                "department": "HR",
                "role": "HR Business Partner",
                "skills": "Strategic HR, organizational development, change management, employee engagement",
                "location": "Portland",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_12",
                "name": "Kevin Martinez",
                "experience": 10,
                "department": "Engineering",
                "role": "DevOps Engineer",
                "skills": "Docker, Kubernetes, AWS, CI/CD pipelines, infrastructure automation",
                "location": "Phoenix",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_13",
                "name": "Rachel Brown",
                "experience": 7,
                "department": "Marketing",
                "role": "Marketing Director",
                "skills": "Strategic marketing, team leadership, budget management, campaign optimization",
                "location": "Atlanta",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_14",
                "name": "Matthew Garcia",
                "experience": 3,
                "department": "Engineering",
                "role": "Junior Software Engineer",
                "skills": "JavaScript, HTML/CSS, basic backend development, learning frameworks",
                "location": "Dallas",
                "employment_type": "Full-time",
            },
            {
                "id": "employee_15",
                "name": "Olivia Moore",
                "experience": 12,
                "department": "Engineering",
                "role": "Principal Engineer",
                "skills": "Technical leadership, system architecture, performance optimization, mentoring",
                "location": "San Francisco",
                "employment_type": "Full-time",
            },
        ]
        employee_documents = []
        for employee in employees:
            document = f"{employee['role']} with {employee['experience']} years of experience in {employee['department']}. "
            document += (
                f"Skills: {employee['skills']}. Located in {employee['location']}. "
            )
            document += f"Employment type: {employee['employment_type']}."
            employee_documents.append(document)

        collection.add(
            ids=[employee["id"] for employee in employees],
            documents=employee_documents,
            metadatas=[
                {
                    "name": employee["name"],
                    "department": employee["department"],
                    "role": employee["role"],
                    "experience": employee["experience"],
                    "location": employee["location"],
                    "employment_type": employee["employment_type"],
                }
                for employee in employees
            ],
        )
        all_items = collection.get()
        print("Collection contents:")
        print(f"Number of documents: {len(all_items['documents'])}")

        def perform_advanced_search(collection, all_items):
            try:
                print("=== Similarity Search Examples ===")
                # Example 1: Search for Python developers
                print("\n1. Searching for Python developers:")
                query_text = "Python developer with web development experience"
                results = collection.query(query_texts=[query_text], n_results=3)
                print(f"Query: '{query_text}'")
                for i, (doc_id, document, distance) in enumerate(
                    zip(
                        results["ids"][0],
                        results["documents"][0],
                        results["distances"][0],
                    )
                ):
                    metadata = results["metadatas"][0][i]
                    print(
                        f"  {i+1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}"
                    )
                    print(
                        f"     Role: {metadata['role']}, Department: {metadata['department']}"
                    )
                    print(f"     Document: {document[:100]}...")
                print("\n2. Searching for leadership and management roles:")
                query_text = "team leader manager with experience"
                results = collection.query(query_texts=[query_text], n_results=3)
                print(f"Query: '{query_text}'")
                for i, (doc_id, document, distance) in enumerate(
                    zip(
                        results["ids"][0],
                        results["documents"][0],
                        results["distances"][0],
                    )
                ):
                    metadata = results["metadatas"][0][i]
                    print(
                        f"  {i+1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}"
                    )
                    print(
                        f"     Role: {metadata['role']}, Experience: {metadata['experience']} years"
                    )
                print("\n=== Metadata Filtering Examples ===")
                print("\n3. Finding all Engineering employees:")
                results = collection.get(where={"department": "Engineering"})
                print(f"Found {len(results['ids'])} Engineering employees:")
                for i, doc_id in enumerate(results["ids"]):
                    metadata = results["metadatas"][i]
                    print(
                        f"  - {metadata['name']}: {metadata['role']} ({metadata['experience']} years)"
                    )
                print("\n4. Finding employees with 10+ years experience:")

                results = collection.get(where={"experience": {"$gte": 10}})
                print(f"Found {len(results['ids'])} senior employees:")
                for i, doc_id in enumerate(results["ids"]):
                    metadata = results["metadatas"][i]
                    print(
                        f"  - {metadata['name']}: {metadata['role']} ({metadata['experience']} years)"
                    )

                print("\n5. Finding employees in California:")
                results = collection.get(
                    where={"location": {"$in": ["San Fransisco", "Los Angeles"]}}
                )
                print(f"Found {len(results['ids'])} employees in California:")
                for i, doc_id in enumerate(results["ids"]):
                    metadata = results["metadatas"][i]
                    print(f"  - {metadata['name']}: {metadata['location']}")
                print("\n=== Combined Search: Similarity + Metadata Filtering ===")
                print("\n6. Finding senior Python developers in major tech cities:")
                query_text = "senior Python developer full-stack"
                results = collection.query(
                    query_texts=[query_text],
                    n_results=5,
                    where={
                        "$and": [
                            {"experience": {"$gte": 8}},
                            {
                                "location": {
                                    "$in": ["San Francisco", "New York", "Seattle"]
                                }
                            },
                        ]
                    },
                )
                print(
                    f"Query: '{query_text}' with filters (8+ years, major tech cities)"
                )
                print(f"Found {len(results['ids'][0])} matching employees:")
                for i, (doc_id, document, distance) in enumerate(
                    zip(
                        results["ids"][0],
                        results["documents"][0],
                        results["distances"][0],
                    )
                ):
                    metadata = results["metadatas"][0][i]
                    print(
                        f"  {i+1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}"
                    )
                    print(
                        f"     {metadata['role']} in {metadata['location']} ({metadata['experience']} years)"
                    )
                    print(f"     Document snippet: {document[:80]}...")
                if not results or not results["ids"] or len(results["ids"][0]) == 0:
                    # Log a message if no similar documents are found for the query term
                    print(f'No documents found similar to "{query_text}"')
                    return

                # Log the header for the top 3 similar documents based on the query term
                print(f'Top 3 similar documents to "{query_text}":')
                # Loop through the top 3 results and log the document details
                for i in range(min(3, len(results["ids"][0]))):
                    # Extract the document ID and similarity score from the results
                    doc_id = results["ids"][0][i]
                    score = results["distances"][0][i]
                    # Retrieve the document text corresponding to the current ID from the results
                    text = results["documents"][0][i]
                    # Check if the text is available; if not, log 'Text not available'
                    if not text:
                        print(
                            f' - ID: {doc_id}, Text: "Text not available", Score: {score:.4f}'
                        )
                    else:
                        print(f' - ID: {doc_id}, Text: "{text}", Score: {score:.4f}')

            except Exception as err:
                print(f"Error in advanced search {err}")

        perform_advanced_search(collection, all_items)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
