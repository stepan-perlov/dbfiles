from .item_with_query import ItemWithQuery

class CsvFile(ItemWithQuery):

    def getContent(self):
        return self._query.format(file=self._fileName)
