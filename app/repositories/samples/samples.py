items = [
    {'name': 'uchida', 'age': 30},
    {'name': 'kosuke', 'age': 40},
]

def index(id):
    return id - 1

class SamplesRepository:

    @staticmethod
    def getlist():
        return items

    def getitem(id):
        return items[index(id)]
