from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name" : "Spice",
        "breed" : "Gotland",
        "sex" : "ewe"
    }

def test_add_sheep():

    #TODO: prepare the new sheep data in a dictionary format
    new_sheep_data = {
        "id" : 7,
        "name": "Cutie pie",
        "breed" : "babydoll",
        "sex" : "ewe"
    }
    response = client.post("/sheep/", json=new_sheep_data)


    
    #todo send a post request to the endpoint "/sheep/" with the new sheep
    #arguments should be your enpoint and new sheep data

    #todo: assert that the response status code is 201 (Created)
    assert response.status_code == 201
    #todo: assert that the response JSON matches the new sheep data
    created_sheep = response.json()
    assert created_sheep["id"] == new_sheep_data["id"]
    assert created_sheep["name"] == new_sheep_data["name"]
    assert created_sheep["breed"] == new_sheep_data["breed"]
    assert created_sheep["sex"] == new_sheep_data["sex"]



    #todo verifty that the sheep was actually added to the database by retrieving it
    retrieved_sheep = client.get(f"/sheep/{created_sheep['id']}")
    #include an assert statement to see if the new sheep data can be retrieved
    assert retrieved_sheep.status_code == 200
    assert retrieved_sheep.json() == created_sheep