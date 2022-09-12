#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    num = 0
    try:
        for (el, value) in zip(my_list_1, my_list_2):
            if isinstance(el, (int, float)) and isinstance(value, (int, float)):
                print("{} {}".format(el, value))
                result.append(el / value)
            elif not isinstance(el, (int, float)) or not isinstance(value, (int, float)):
                result.append(0)
                print("wrong type")
    except ZeroDivisionError:
        result.append(0)
        print("division by 0")
    except Exception:
        result.append(0)
        print("out of range")
    finally:
        return result

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
