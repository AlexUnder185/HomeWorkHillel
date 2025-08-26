def common_elements():
    multi_3 = {x for x in range(100) if x % 3 == 0}

    multi_5 = {x for x in range(100) if x % 5 == 0}

    return multi_3 & multi_5


assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print('ОК')
