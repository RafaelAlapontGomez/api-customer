from fastapi.testclient import TestClient
from main import app

endpoint = '/api/v1/customer'

def test_create_customer_ok():
    client = TestClient(app)

    customer = {
        "firstName": "Rafael",
        "lastName": "Alapont Gómez",
        "birthdate": "1973-06-12",
        "email": "myemail18@cosasdedevs.com",
        "active": True,
        "phone": "619524675",
        "city": "MAD",
    }

    response = client.post(
        endpoint,
        json = customer
    )

    assert response.status_code == 201, response.text
    data = response.json()
    assert data['email'] == customer['email']
    assert data['phone'] == customer['phone']

def test_create_customer_duplicate():
    client = TestClient(app)

    customer = {
        "firstName": "Rafael",
        "lastName": "Alapont Gómez",
        "birthdate": "1973-06-12",
        "email": "myemail18@cosasdedevs.com",
        "active": True,
        "phone": "619524675",
        "city": "MAD",
    }

    response = client.post(
        endpoint,
        json = customer
    )

    assert response.status_code == 400, response.text
    data = response.json()
    assert data['detail'] == "customer already registered"

def test_get_all_customers_ok():
    client = TestClient(app)

    response = client.get(
        endpoint
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data) == 1
    
def test_get_customer_ok():
    client = TestClient(app)

    response = client.get(
        endpoint + '/1'
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['email'] == "myemail18@cosasdedevs.com"
    assert data['phone'] == "619524675"

def test_update_customer_ok():
    client = TestClient(app)

    customer = {
        "firstName": "Rafael",
        "lastName": "Alapont Gómez",
        "birthdate": "1973-06-12",
        "email": "rafae@kktua.com",
        "active": False,
        "phone": "919524675",
        "city": "BAR",
    }

    response = client.put(
        endpoint + '/1',
        json = customer
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['email'] == "rafae@kktua.com"
    assert data['active'] == False
    assert data['phone'] == "919524675"
    assert data['city']['code'] == "BAR"

def test_delete_customer_ok():
    client = TestClient(app)

    response = client.delete(
        endpoint + '/1'
    )

    assert response.status_code == 204
