#Функция для подсчета числа элементов в списках:
def count(lst):
    if not lst:
        return 0
    if isinstance(lst, list):
        return count(lst[0]) + count(lst[1:])
    return 1
#Функция для расчета xi:
def calculate_xi(n):
    if n == 1:
        return 1
    if n == 2:
        return -1 / 8
    return ((n - 1) * calculate_xi(n - 1)) / 3 + ((n - 2) * calculate_xi(n - 2)) / 4
print(count([]))
print(count([1, 2, 3]))
print(count(["x", "y", ["z"]]))
print(count([1, 2, [3, 4, [5]]]))
print(calculate_xi(1))
print(calculate_xi(2))