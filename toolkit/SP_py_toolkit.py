import json, os

def write_json(_path, _data):
    with open(_path, 'w') as out_json:
        json.dump(_data, out_json, indent=4)


def read_json(_path):
    if os.path.exists(_path) == False:
        write_json(_path, {})
    with open(_path, 'r') as in_json:
        _data = json.load(in_json)

    return _data
