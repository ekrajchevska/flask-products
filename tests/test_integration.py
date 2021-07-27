# import requests
# import pytest


# def test_get_products_check_status_code_200():
#       response = requests.get('http://app:5000/products')
#       assert response.status_code == 200

# def test_get_product_by_id_check_status_code_200():
#       response = requests.get('http://app:5000/product/2')
#       assert response.status_code == 200

# test_data_products = [
#       (1, "Violet crop top"),
#       (2, "Red Skirt"),
#       (4, "Silver necklace"),
#       (5, "Ripped jeans"),
#       (8, "Knitted bag"),
# ]

# @pytest.mark.parametrize("product_id, expected_name", test_data_products)
# def test_using_test_data_object_get_products_data_check_name(product_id, expected_name):
#      response = requests.get(f"http://app:5000/product/{product_id}")
#      response_body = response.json()
#      assert response_body["name"] == expected_name


# new_product =  {
#          "name": "Sweater",
#          "description": "Fall season 2021",
#          "price": 40.0,
#          "quantity": 55
# }
# headers = {"Content-Type" : "application/json"}

# def test_post_new_product_check_status_code_200():
#       response = requests.post('http://app:5000/create', json=new_product, headers=headers)
#       assert response.status_code == 200

# def test_delete_product_check_status_code_200():
#       response = requests.delete('http://app:5000/product/14')
#       assert response.status_code == 200
