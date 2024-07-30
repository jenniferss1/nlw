import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason= "interacao com o banco")
def test_add_links():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    links_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "www.link.com",
        "title": "images for the trip"
    }
    
    links_repository.add_links(links_info)

@pytest.mark.skip(reason= "interacao com o banco")
def test_find_links():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    links = links_repository.find_links(trip_id)
    print()
    print(links)