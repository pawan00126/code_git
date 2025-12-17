import json

user = {
    'name' : 'Pawan Bhati',
    'Age' : 23
}

# json.dumps() =>  dict -> json
def serialize_json(data):
    return json.dumps(data)

# json.loads() => json -> dict
def deserialize_json(data):
    return json.loads(data)


serialized_json_data = serialize_json(user)
deserialize_json_data = deserialize_json(serialized_json_data)

print(f'we got the serialize user in JSON : {serialized_json_data}')
print(f'type : {type(serialized_json_data)}')


print(f'we got the de-serialized JSON user in dict : {deserialize_json_data}')
print(f'type : {type(deserialize_json_data)}')