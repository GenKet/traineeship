#функция для поиска фальшивой корзины
def find_fake_basket(N, w, d, P):
    total_weight = N * (w - d)
    chosen_weight = P * (P + 1) // 2 * w
    fake_weight = total_weight - chosen_weight
    fake_basket = (fake_weight - d) // (w - d) + 1
    if 1 <= fake_basket <= N:
        return fake_basket #возвращает номер фальшивой корзины
    else:
        return -1  #фальшивая корзина не найдена

N = 5
w = 10
d = 4
P = 3
fake_basket = find_fake_basket(N, w, d, P)
print(fake_basket)