import requests

url = "https://api.restful-api.dev/objects"

def get_objects():
    response = requests.get(url)

    if response.status_code == 200:
        objects = response.json()

        for object in objects[:1]:
            print("ID:", object["id"])
            print("Name:", object["name"])
            print("Data:", object["data"])
            data_dict = object.get("data")
            if data_dict and "color" in data_dict:
                print("Color:", data_dict["color"])
            else:
                print("Color: N/A")
            print("-" * 50)

    else:
        print("Error", response.status_code)

get_objects()

def add_objects():
    new_object = {
        "name": "iPhone Duo",
        "data": {
            "color": "Midnight",
            "price": 3000,
            "year": 2026
        }
    }

    response = requests.post(f"{url}", json=new_object)
    if response.status_code == 200 or response.status_code == 201:
        data = response.json()
        print("Successfully created object!!")
        print(data)
        return data["id"]
    else:
        print("Failed to retrieve data. Error:", response.text)

# add_objects()

def update_put(object_id):
    updated_data = {
        "name": "iPhone Duo Pro Max",
        "data": {
            "color": "Space Black",
            "price": 3499,
            "year": 2026,
            "storage": "512GB"
        }
    }
    

    response = requests.put(f"{url}/{object_id}", json=updated_data)
    
    if response.status_code == 200:
        print("PUT Success")
        print(response.json())
    else:
        print("PUT Error:", response.status_code, response.text)

def update_patch(object_id):
    patch_data = {
        "name": "iPhone Duo Pro Max [On Sale]"
    }
    
    response = requests.patch(f"{url}/{object_id}", json=patch_data)
    
    if response.status_code == 200:
        print("PATCH Success")
        print(response.json())
    else:
        print("PATCH Error:", response.status_code, response.text)


def delete_object(object_id):
    response = requests.delete(f"{url}/{object_id}")
    
    if response.status_code == 200:
        print("DELETE Success")
        print(f"Object ID {object_id} was removed.")
        print(response.json())
    else:
        print("DELETE Error:", response.status_code, response.text)


my_object_id = add_objects()


if my_object_id:
    update_put(my_object_id)
    update_patch(my_object_id)
    delete_object(my_object_id)