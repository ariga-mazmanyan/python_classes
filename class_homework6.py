import json
import yaml


def json_to_text(a, b):
    with open(a, "r") as json_file:
        data = json.load(json_file)

    with open(b, "a") as txt_file:
        txt_file.write(data)

    return txt_file


def json_to_yaml(a, b):
    with open(a, "r") as json_file:
        data = json.load(json_file)

    with open(b, "a") as yaml_file:
        yaml.dump(data, yaml_file)

    return yaml_file


def yaml_to_json(a, b):
    with open(a, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

    with open(b, "a") as json_file:
        json.dump(data, json_file)

    return json_file


def yaml_to_text(a, b):
    with open(a, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)

    with open(b, "a") as txt_file:
        txt_file.write(data)

    return txt_file


print(json_to_text("package.json", "text_file.txt"))
print(json_to_yaml("package.json", "sample_yaml.yml"))
print(yaml_to_json("sample_yaml.yml", "package.json"))
print(yaml_to_text("sample_yaml.yml", "text_file.txt"))