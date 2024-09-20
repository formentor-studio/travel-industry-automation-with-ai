import json
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore

def load_hotels(vector_store: VectorStore):
    with open('resources/hotels.json') as file_hotels:
        hotels = json.load(file_hotels)

    docs_hotels = [
        Document(
            page_content = hotel["description"],
            metadata = {
                "type": "hotel",
                "id": hotel["id"],
                "name": hotel["name"],
                "country": hotel["country"],
                "destination": hotel["destination"]
            }
        ) for hotel in hotels]

    docs_rooms = []
    for hotel in hotels:
        docs_rooms += [
            Document(
                page_content = room["description"],
                metadata = {
                    "type": "room",
                    "code": room["code"],
                    "hotel": hotel["id"],
                    "name": room["name"],
                    "max_pax": room["max_pax"],
                    "max_adults": room["max_adults"],
                    "max_children": room["max_children"]
                }
            ) for room in hotel["rooms"]]
        
    vector_store.add_documents(docs_hotels)
    vector_store.add_documents(docs_rooms)