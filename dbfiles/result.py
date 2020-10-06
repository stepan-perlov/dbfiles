import os
import abc
import uuid
import subprocess
from .schema import Schema
from .statement import Statement

CUR_DIR = os.path.abspath(os.path.dirname(__file__))


class AbstractResult(abc.ABC):

    def __init__(self, name, debug):
        self._name = name
        self._debug = debug
        self._dstRoot = os.path.join("/tmp", "dbfiles-{}".format(uuid.uuid1()))
        self._files = []
        os.makedirs(self._dstRoot)

    @abstractmethod
    def writeItem(self, item):
        pass


class OneFileResult(AbstractResult):

    def writeItem(self, item):
        pass


class ManyFilesResult(AbstractResult):

    def writeItem(self, item):
        pass




class OneFileWriter(object):

    def __init__(self, name, dstRoot):
        self._name = name
        self._dstRoot = dstRoot


class ManyFilesWriter(object):

    def __init__(self, name, dstRoot):
        self._name = name
        self._dstRoot = dstRoot
        self._files = []


class Result(object):

    def __init__(self, name, oneFile, debug):
        self._name = name
        self._debug = debug
        self._dstRoot = os.path.join("/tmp", "dbfiles-{}".format(uuid.uuid1()))
        os.makedirs(self._dstRoot)

        if oneFile:
            self.writer = OneFileWriter(self._name, self._dstRoot)
        else:
            self.writer = ManyFilesWriter(self._name, self._dstRoot)

    def writeItem(self, item):
        self.writer.writeItem(item)


    def _writeItem(self, item):
        with open(os.path.join(self._dstStatements, stmt.fileName), "w") as fstream:
            fstream.write(stmt.content)

        self._initStatements.append(stmt)
        if stmt.type in self.UPDATABLE:
            self._updateStatements.append(stmt)

    def addSchema(self, schema, parentSchemas=[]):
        for itemDict in schema.data["main"]:
            item = Item.fromDict(schema, itemDict)
            if item.type == "include":
                includePath = os.path.abspath(os.path.join(
                    os.path.dirname(schemaPath),
                    item.value
                ))
                parentSchemas.append(schema)
                self.addSchema(includePath, parentSchemas)
            else:
                self._writeItem(item)

    def _writeEntry(self, fileName, statements):
        with open(os.path.join(self._dstRoot, fileName), "w") as fstream:
            fstream.write(
                "\n".join([
                    "\\i {}".format(os.path.join("statements", stmt.fileName))
                    for stmt in statements
                ]) + "\n"
            )

    def make(self):
        self._writeEntry("init.sql", self._initStatements)
        self._writeEntry("update.sql", self._updateStatements)

    def onDone(self):
        if not self._debug:
            subprocess.run("sudo rm -rf {}".format(self._dstRoot), shell=True)
