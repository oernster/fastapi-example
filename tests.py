from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestClass:
    def test_hello_world(self):
        text = "Hello World"
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == "Hello World"

    def test_add_numbers(self):
        num1 = 4
        num2 = 99
        response = client.post(
            "/add/",
            json={
                "num1": 4,
                "num2": 99,
            },
        )
        assert response.status_code == 200
        assert response.json() == {
            "result": "103",
        }

    def test_join_words(self):
        text1 = "Hello"
        text2 = "World"
        joined_text = "Hello-World"
        response = client.post(
            "/joinwords/",
            json={
                "w1": text1,
                "w2": text2,
            },
        )
        assert response.status_code == 200
        assert response.json() == {"result": joined_text}
