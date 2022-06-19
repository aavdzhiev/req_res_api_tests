import json
from os.path import join, dirname
from jsonschema import validate


def load_json_schema(filename):
    """ Loads the given schema file """

    # relative_path = join('resources', filename)
    absolute_path = join(dirname(__file__), filename)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())


def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """

    schema = load_json_schema(schema_file)
    return validate(data, schema)
