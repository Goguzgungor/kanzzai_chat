# app.py

from flask import Flask, request, jsonify, Response
from service.ai_service import AIService
from service.db_service import DBService

app = Flask(__name__)

# MongoDB bağlantısını yapın
uri = "mongodb+srv://berkegenckaya:123@cluster0.p2zsgy9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_service = DBService(uri, 'db', 'kanzz')

ai_service = AIService()


@app.route("/ai", methods=["POST"])
def ai_post():
    print("Post /ai called")
    json_content = request.json
    query = json_content.get("query")

    print(f"query: {query}")

    # İş mantığını ai_service.py'den çağır
    response = ai_service.process_query(query)

    print(response)

    response_answer = {"answer": response}
    return jsonify(response_answer)

@app.route("/ai/auto", methods=["POST"])
def ai_auto_post():
    print("Post /ai called")
    json_content = request.json
    query = json_content.get("query")
    wallet_address = json_content.get("wallet_address")




    ai_promt = db_service.get_data(wallet_address)

    # İş mantığını ai_service.py'den çağır
    response = ai_service.process_query_auto(query, ai_promt)

    print(response)

    response_answer = {"answer": response}
    return jsonify(response_answer)


@app.route("/test", methods=["POST"])
def test_post():
    json_content = request.json
    data = json_content.get("data")
    inserted_id = db_service.insert_data(data)

    response_answer = {"inserted_id": inserted_id}

    print(response_answer)

    return jsonify(response_answer)


def start_app():
    app.run(host="0.0.0.0", port=8081, debug=True)


if __name__ == "__main__":
    start_app()

# @app.route("/ask_pdf", methods=["POST"])
# def askPDFPost():
#     print("Post /ask_pdf called")
#     json_content = request.json
#     query = json_content.get("query")
#
#     print(f"query: {query}")
#
#     print("Loading vector store")
#     vector_store = Chroma(persist_directory=folder_path, embedding_function=embedding)
#
#     print("Creating chain")
#     retriever = vector_store.as_retriever(
#         search_type="similarity_score_threshold",
#         search_kwargs={
#             "k": 20,
#             "score_threshold": 0.1,
#         },
#     )
#
#     document_chain = create_stuff_documents_chain(cached_llm, raw_prompt)
#     chain = create_retrieval_chain(retriever, document_chain)
#
#     result = chain.invoke({"input": query})
#
#     print(result)
#
#     sources = []
#     for doc in result["context"]:
#         sources.append(
#             {"source": doc.metadata["source"], "page_content": doc.page_content}
#         )
#
#     response_answer = {"answer": result["answer"], "sources": sources}
#     return response_answer
#
#
# @app.route("/pdf", methods=["POST"])
# def pdfPost():
#     file = request.files["file"]
#     file_name = file.filename
#     save_file = "pdf/" + file_name
#     file.save(save_file)
#     print(f"filename: {file_name}")
#
#     loader = PDFPlumberLoader(save_file)
#     docs = loader.load_and_split()
#     print(f"docs len={len(docs)}")
#
#     chunks = text_splitter.split_documents(docs)
#     print(f"chunks len={len(chunks)}")
#
#     vector_store = Chroma.from_documents(
#         documents=chunks, embedding=embedding, persist_directory=folder_path
#     )
#
#     vector_store.persist()
#
#     response = {
#         "status": "Successfully Uploaded",
#         "filename": file_name,
#         "doc_len": len(docs),
#         "chunks": len(chunks),
#     }
#     return response
