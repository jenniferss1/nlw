import pytest
import uuid
from datetime import datetime, timedelta
from .trip_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason= "interacao com o banco")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    
    trip_infos = {
        "id": trip_id,
        "destination": "Rio De Janeiro",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Jennifer",
        "owner_email": "jennifersantos@hotmail.com"
    }
    
    trip_repository.create_trip(trip_infos)

@pytest.mark.skip(reason= "interacao com o banco")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    
    trip = trip_repository.find_trip_by_id(trip_id)
    print(trip)

@pytest.mark.skip(reason= "interacao com o banco")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    
    trip_repository.update_trip_status(trip_id)