import abc


itemMap = {
    "=#": SqlInline,
    "sql": SqlFile,
    "json": JsonFile,
    "yaml": YamlFile,
    "csv": CsvFile,
}

class Item(abc.ABC):

    @staticmethod
    def create(schema, itemDict):
        itemType = list(itemDict.keys())[0]
        itemValue = itemDict[itemType]
        return itemMap[itemType](schema, itemType, itemValue)

    @property
    def schema(self):
        return self._schema

    @property
    def type(self):
        return self._type

    @property
    def intNum(self):
        return self._intNum

    @property
    def textNum(self):
        return self._textNum

    @property
    def value(self):
        return self._value

    @property
    def fileName(self):
        return "{}_{}_{}.sql".format(
            self._textNum,
            self._intNum,
            self._type,
        )

    def initialize(self):
        pass

    def __init__(self, schema, itemType, itemValue):
        self._schema = schema
        self._type = itemType
        self._value = itemValue

        self._intNum, self._textNum = self._schema.counter.next()

        self.initialize()

    @abc.abstractmethod
    def getContent(self):
        pass
