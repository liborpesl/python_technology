test = "Dnes je krasne"


def find_index(collection, element):
    for index, value in enumerate(collection):
        if value == element:
            return index
    return -1
