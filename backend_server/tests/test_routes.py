import unittest
import json
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_root_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Flask App!', response.data)

    def test_health_and_hello(self):
        app = create_app()
        client = app.test_client()

        # health
        r = client.get("/api/health")
        assert r.status_code == 200
        j = r.get_json()
        assert j["status"] == "ok"

        # hello
        r = client.get("/api/hello?name=Tester")
        assert r.status_code == 200
        assert r.get_json()["message"] == "Hello, Tester!"

    def test_echo_and_add_and_items_crud(self):
        app = create_app()
        client = app.test_client()

        # echo
        r = client.post("/api/echo", json={"x": 1})
        assert r.status_code == 200
        assert r.get_json()["echo"] == {"x": 1}

        # add
        r = client.get("/api/add?a=2&b=3")
        assert r.get_json()["sum"] == 5

        # create item
        r = client.post("/api/items", json={"name": "item1", "data": {"k": "v"}})
        assert r.status_code == 201
        item = r.get_json()
        item_id = item["id"]

        # get item
        r = client.get(f"/api/items/{item_id}")
        assert r.status_code == 200
        assert r.get_json()["name"] == "item1"

        # update item
        r = client.put(f"/api/items/{item_id}", json={"name": "item1-updated"})
        assert r.status_code == 200
        assert r.get_json()["name"] == "item1-updated"

        # delete item
        r = client.delete(f"/api/items/{item_id}")
        assert r.status_code == 200
        assert r.get_json()["deleted"] == item_id

    # Add more tests for other endpoints as needed

if __name__ == '__main__':
    unittest.main()