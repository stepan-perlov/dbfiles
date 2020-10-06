import os
import yaml

from jsonschema import Draft7Validator

from .items import Item
from .errors import SchemaException


curDir = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(curDir, "schema.yaml")) as fstream:
    protocol = yaml.load(fstream, Loader=yaml.FullLoader)

Draft7Validator.check_schema(protocol)

class Schema(object):

    validator = Draft7Validator(protocol)

    @classmethod
    def setArgs(cls, args):
        cls._srcRoot = args.srcRoot

    @property
    def counter(self):
        return self._counter

    @property
    def path(self):
        return self._path

    @property
    def fileName(self):
        return self._fileName

    @property
    def dir(self):
        return self._dir

    @property
    def data(self):
        return self._data

    @property
    def items(self):
        return self._items


    def __init__(self, counter, schemaPath):
        self._counter = counter
        self._path = os.path.abspath(os.path.join(Schema._srcRoot, schemaPath))
        self._fileName = os.path.basename(self._path)
        self._dir = os.path.dirname(self._path)

        with open(self._path) as fstream:
            self._data = yaml.load(fstream, Loader=yaml.FullLoader)

        if not Schema.validator.is_valid(self._data):
            error = "Invalid schema {}".format(self._path)
            for err in Schema.validator.iter_errors(self._data):
                print("Error: {}".format(err.message))
                print("Context: {}".format(err.absolute_schema_path))

            raise SchemaException(error)

        self._items = []

    def parse(self):
        self._items = [Item.create(self, itemDict) for itemDict in self._data["main"]]
