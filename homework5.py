immutable_var = tuple = 1, 2, "город", True
print("immutable_var:", immutable_var)
 # Кортеж не поддерживает изменение по элементам


mutable_list = tuple = [1, 2, "город", True], 3, 4
print("Mutable_list:", mutable_list )
mutable_list[0][3] = False
print("Mutable_list_changed:", mutable_list )


