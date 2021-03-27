"""
Плакунов Иван - Python.Март2021.5урок.4задание

"""
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([src[el] for el in range(1, len(src)) if src[el] > src[el-1]])
