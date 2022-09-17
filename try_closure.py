def test_closure(check_value):
    data = []

    def add_data(checked_value):
        if checked_value > check_value:
            data.append(checked_value)

    def get_data():
        return data

    return add_data, get_data


class DataClass(object):
    def __init__(self, checked_value):
        self.data = []
        self.checked_value = checked_value

    def add_data(self, check_value):
        if self.checked_value > check_value:
            self.data.append(check_value)

    def get_data(self):
        return self.data

if __name__ == '__main__':
    add_data, get_data = test_closure(3)
    data_object = DataClass(3)
    data_object.add_data(10)
    data_object.add_data(-10)
    data_object.add_data(510)

    print(data_object.get_data())

    add_data(2)
    add_data(3)
    add_data(20)
    add_data(10)
    add_data(-10)
    add_data(+110)

    data = get_data()
    print(data)