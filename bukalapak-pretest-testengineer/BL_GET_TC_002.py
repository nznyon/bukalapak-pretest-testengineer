import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.status_code)
jsonResponse = response.json()
data = response.json()

def test_id():
    for i in range(len(data)):
        assert(isinstance((data[i]['id']),int))
        print("true")

def test_title():
    for i in range(len(data)):
        assert (isinstance((data[i]['title']), str))
        print("true")

def test_body():
    for i in range(len(data)):
        assert (isinstance((data[i]['body']), str))
        print("true")

def test_userId():
    for i in range(len(data)):
        assert (isinstance((data[i]['userId']), int))
        print("true")
        