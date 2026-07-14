# n = int(input())
# s=input().split()
# code = []
# for i in s:
#     if len(i)%2 != 0:
#         code.append(i)
# if code:
#     print(max(code, key=len))
# else:
#     print("Better luck next time")

# s = input()
# count = 0
# maximum = 0
# for i in s:
#     count += 1
#     if i == '@' or i == '$':
#         if count > maximum:
#             maximum = count
#         count = 0
# if count > maximum:
#     maximum = count
# print(maximum)



n = int(input())
prices = list(map(int, input().split()))
min_price = prices[0]
max_profit = 0
for price in prices:
    if price < min_price:
        min_price = price
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit
print(max_profit)






