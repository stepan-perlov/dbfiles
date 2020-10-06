import yaml
from .item_with_query import ItemWithQuery

class YamlFile(ItemWithQuery):

    def getContent(self):
        with open(self._absFilePath) as fstream:
            data = yaml.load(fstream)
        return self._query.format(file=self._srcPath, value=data)
