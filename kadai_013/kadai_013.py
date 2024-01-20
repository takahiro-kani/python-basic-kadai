def calculate_total(price:int , tax:int):
  total_price = price * (1 + tax/100 )
  return total_price
result = calculate_total(1000 , 10)
print(result)