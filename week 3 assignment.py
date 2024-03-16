price = input('Original Price: ')
discount_percent = input('Discount: ')

def calculate_discount(price, discount_percent):
    sale_price = (float(discount_percent) / 100) * float(price)
    return sale_price

if float(discount_percent) >= 20:
    print(f'Final price: {calculate_discount(price, discount_percent)}')
else:
    print(f'Final Price: {price}')