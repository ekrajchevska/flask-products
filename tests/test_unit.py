# da dodadam pytest marks -> za da se izvrshuvaat zasebno (moze i so parametar pytest test_1)
# so pytest -m birame koi tests (so koi marks t.e)


def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200

def test_create_product(client):
    response = client.post(
        '/create',
        json={ "name": "Leather Jacket", "description": "Vegan materials", "price": 120.00, "quantity": 20 }
    )

    assert response.status_code == 200


def test_get_products(client):
    response = client.get('/products')
    data = response.get_json()
    assert response.status_code == 200
    assert data[0]["name"] == "Leather Jacket"


def test_get_product(client):
    response = client.get('/product/1')
    assert response.status_code == 200

    data = response.get_json()
    print(data)
    assert data["name"] == "Leather Jacket"


def test_update_product(client):
    response = client.put(
        '/product/1',
        json={ "name":"Leather Jacket", "description": "Limited Edition" ,"price": 180.00, "quantity": 10 }
    )
    assert response.status_code == 200

    data = response.get_json()
    assert data["price"] == 180.00
    assert data["quantity"] == 10


def test_delete_product(client):
     response = client.delete('/product/1')
     assert response.status_code == 200
