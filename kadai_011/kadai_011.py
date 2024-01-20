# for

my_list = ["水","金","地","火","木","土","天","海","冥"]

for num in range(0,2):
  for i in range(0,9):
    print(my_list[i])

my_list = ["水","金","地","火","木","土","天","海","冥"]

# while

num = 0
while num < 2:
  index = 0
  while index < 9:
    print(my_list[index])
    index = index + 1
  
  num = num + 1