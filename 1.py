def swap_bytes(num):
    # Извлекаем младший байт
    low_byte = num & 0xFF
    # Извлекаем старший байт
    high_byte = (num >> 8) & 0xFF
    # Объединяем байты в новое число, поменяв их местами
    new_num = (low_byte << 8) | high_byte
    return new_num
num = 0xABCD  # число в шестнадцатеричном формате
swapped_num = swap_bytes(num)
print(swapped_num)