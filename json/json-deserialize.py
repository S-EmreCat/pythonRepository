# serialize

# deserialize

import json

# with open("person.json") as file:
#     data = json.load(file)

# json-string
with open("person.json") as file:
    data = file.read()

# print(data)
# print(type(data))



data = """
    {
        "firstName":"Sadık",
        "lastName":"Turan",
        "hobbies": ["spor","sinema"],
        "age":37,
        "children": [
            {
                "firstName": "Çınar",
                "age":3
            }
        ]
    }
    """
data = json.loads(data)

print(data)
print(type(data))
print(data["firstName"])
print(data["hobbies"])
print(data["hobbies"][0])

