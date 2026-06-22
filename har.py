#prime
# n = int(input())
# count = 0
# for i in range(1,n+1):
#     if n  % i == 0:
#         count += 1
# if count == 2:
#     print("prime")
# else:
#     print("not prime")

# vovels
# n = input()
# vowels =0
# constant = 0
# for i in n.lower():
#     if i.isalpha():
#         if i in "aeiou":
#             vowels += 1
#         else:
#             constant += 1
# print("vowels", vowels)
# print("constant", constant)

# # second largest number
# arr = list(map(int,input().split()))
# arr = list(set(arr))
# arr.sort()
# print(arr[-2])


# Count Word Frequency in a Sentence
# sen = input()
# word = sen.split()
# freq = {}
# for words in word:
#     if words in freq:
#         freq[words] += 1
#     else:
#         freq[words] = 1
# print(freq)

# Balanced Parenthese
# n = input()
# open_para =0
# close_para = 0
# for ch in n:
#     if ch == "(":
#         open_para += 1
#     elif ch == ")":
#         close_para += 1
# if open_para == close_para:
#     print("balanced")
# else:
#     print("not balanced")
# n = input()
# stack = []
# balanced = True
# for ch in n:
#     if ch == "(":
#         stack.append(ch)
#     elif ch == ")":
#         if not stack:
#             balanced = False
#             break
#         stack.pop()
# if balanced and not stack:
#     print("balanced")
# else:
#     print("not balanced")

# rotating numbers
nums = list(map(int, input().split()))
k = int(input())
k = k % len(nums)
result = nums[-k:] + nums[:-k]
print(*result)

        




