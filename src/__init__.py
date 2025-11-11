from data_loader import DataLoader
from vector_store import FaissVectorStore

if __name__ == "__main__":
    # load data in dataloader
    dataLoader= DataLoader("../content/")
    data= dataLoader.document_loader()

    # create vectorstore
    vectorStore= FaissVectorStore(persist_dir="../vector_store/")
    vectorStore.build_from_documents(data)

    # test example
    print("\n\n\n\n\n")
    vectorStore.load()
    query= vectorStore.query("What is the name of the hotel?", top_k=3)
    for i, result in enumerate(query):
        print(f"  Result {i+1}: Distance={result['distance']:.4f}")
        print(f"  Text: {result['metadata']['text'][:200]}...")