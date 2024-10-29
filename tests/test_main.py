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

def test_delete_sheep():
    #create test sheep data
    new_sheep_data = {
        "id" : 30,
        "name": "Giants",
        "breed" : "football",
        "sex" : "embarrassing"
    }
    #create a new entry in the db and assert that it was created successfully
    response = client.post("/sheep/", json=new_sheep_data)
    assert response.status_code == 201
    
    #delete the new entry and assert that it was deleted successfully
    delete_response = client.delete("/sheep/30")
    assert delete_response.status_code == 200
    #check to make sure the deleted entry matched that of our hardcoded new sheep data
    assert delete_response.json() == new_sheep_data
    #verify the data was successfully deleted by attempting to retrieve it. 
    #updated get method in main successfully handles 404 not found errors
    retrieve_response = client.get("/sheep/30")
    assert retrieve_response.status_code == 404

def test_update_sheep():
    #create test sheep data
    new_sheep_data = {
        "id" : 10,
        "name": "Cutie patootie",
        "breed" : "babydoll",
        "sex" : "ram"
    }
    #create a new entry in the db and assert that it was created successfully
    response = client.post("/sheep/", json=new_sheep_data)
    assert response.status_code == 201
    #create updated test sheep data
    updated_sheep_data = {
        "id" : 10,
        "name": "Cutie patootie",
        "breed" : "babydoll",
        "sex" : "ewe"
    }
    #update the new_sheep data originally created with the new data
    #assert that it successfuly did so with code 200
    #assert again that the json matches with the updated version (aka successfully updated)
    response = client.put("/sheep/", json=updated_sheep_data)
    assert response.status_code == 200
    assert response.json() == updated_sheep_data

    #verify entry was successfully updated by accessing it with the id that didnt change
    retrieve_response = client.get("/sheep/10")
    assert retrieve_response.status_code == 200
    assert retrieve_response.json() == updated_sheep_data

#cant figure this one out :(
def test_read_all_sheep():
    
    # sheep_data_1 = {
    #     "id": 20,
    #     "name": "test",
    #     "breed": "case",
    #     "sex": "ewe"
    # }
    # sheep_data_2 = {
    #     "id": 22,
    #     "name": "i hate",
    #     "breed": "the steelers",
    #     "sex": "ram"
    # }
    # client.post("/sheep/", json=sheep_data_1)
    # client.post("/sheep/", json=sheep_data_2)

    
    # response = client.get("/sheep/")
    # assert response.status_code == 200

    # expected_sheep = [sheep_data_1, sheep_data_2]
    # assert response.json() == expected_sheep
    pass