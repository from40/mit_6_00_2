class Stuff(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def get_density(self):
        return self.value / self.weight

    def __str__(self):
        return self.name + ": <" + str(self.value) + ", " + str(self.weight) + ">"


def pack_stuff(names, values, weights):
    stuff_list = []
    for i in range(len(values)):
        stuff_list.append(Stuff(names[i], values[i], weights[i]))
    return stuff_list


def greedy(items, constraint, key_function):
    new_staff_list = sorted(items, key=key_function, reverse=True)
    total_weigth = 0
    total_value = 0
    burglar_list = []
    for i in range(len(new_staff_list)):
        if total_weigth + new_staff_list[i].get_weight() <= constraint:
            burglar_list.append(new_staff_list[i])
            total_weigth += new_staff_list[i].get_weight()
            total_value += new_staff_list[i].get_value()
    return burglar_list, total_value


def test_greedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print("Total value of taken items = ", val)
    for item in taken:
        print(" ", item)


def test_greedys(items, constraint):
    print("For max value as key function :")
    test_greedy(items, constraint, Stuff.get_value)
    print("For min weight as key function :")
    test_greedy(items, constraint, lambda x: 1 / Stuff.get_weight(x))
    print("For max value / weigth ration as key function :")
    test_greedy(items, constraint, Stuff.get_density)


names = ["clock", "picture", "radio", "vase", "book", "computer"]
values = [175, 90, 20, 50, 10, 200]
weights = [10, 9, 4, 2, 1, 20]
stuff_list = pack_stuff(names, values, weights)
constraint = 20
test_greedys(stuff_list, constraint)
