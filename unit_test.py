import unittest
import requests
from product_model import *

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/products"
    req_data = {
    "name": "LMN",
    "brand": "LMN_Brand",
    "weight": 10,
    "sku": "15",
    "available": True
    }
    
    expected_result = {
    "name": "ABC",
    "brand": "ABC_Brand",
    "weight": 1,
    "sku": "100",
    "available": False
    }
    
    update_data = {
    "name": "DEF_updated",
    "brand": "DEF_Brand",
    "weight": 2,
    "sku": "200",
    "available": False
    }
    
    def test_1_get_all_products(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 3)
        print("Test 1 completed")
        
    def test_2_post_product(self):
        resp = requests.post(self.URL, json=self.req_data)
        self.assertEqual(resp.status_code, 201)
        print("Test 2 completed")
      
    def test_3_get_specific_product(self):
        resp = requests.get(self.URL + '/100')
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(resp.json(), self.expected_result)
        print("Test 3 completed")
        
    def test_4_delete(self):
        resp = requests.delete(self.URL + '/100')
        self.assertEqual(resp.status_code, 200)
        print("Test 4 completed")
    
    def test_5_update(self):
        resp = requests.put(self.URL + '/200', json=self.update_data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['sku'], self.update_data['sku'])
        self.assertEqual(resp.json()['message'], "Product "+self.update_data['sku']+" has been updated")
        print("Test 5 completed")
        
if __name__ == "__main__":
    test_api = TestAPI()
    test_api.test_1_get_all_products()
    test_api.test_2_post_product()
    test_api.test_3_get_specific_product()
    test_api.test_4_delete()
    test_api.test_5_update()