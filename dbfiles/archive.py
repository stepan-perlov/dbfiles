import os
import uuid


class Archive(object):

    @classmethod
    def setArgs(cls, args):
        cls._name = args.name
        cls._dstRoot = args.dstRoot
        cls._oneFile = args.oneFile
        cls._debug = args.debug

    @classmethod
    def create(cls):
        if cls._oneFile:
            return OneFileArchive()
        else:
            return ManyFilesArchive()

    def __init__(self):
        self._tmpRoot = os.path.join("/tmp", "dbfiles-{}".format(uuid.uuid1()))
        os.makedirs(self._tmpRoot)

    def add(self, schema):
        pass


class OneFileArchive(Archive):
    pass

class ManyFilesArchive():
    pass
