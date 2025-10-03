# #

# def consecutive_range(l, k, s):
#   res = []
#   st, en = 0, 0
#   for i, n in enumerate(l):
#     if i < en:
#       continue
#     if n == k:
#       st = i
#       for j in range(i+1, len(l)):
#         if l[j] != k:
#             break
#       en = j-1
#       if (en-st >= s-1):
#         res.append((st, en))
#   return res


# consecutive_range(
#     l=[2, 6, 6, 6, 6, 5, 4, 6, 6, 8, 4, 6, 6, 6, 2, 6],
#     k=6,
#     s=3)


# def consecutive_sim(l):
#   idx = 0
#   res = []

#   while idx < len(l):
#     start = idx
#     val = l[idx]
#     while idx < len(l) and l[idx] == val:
#       idx += 1
#     end = idx-1
#     res.append((val, start, end))
#   return res
  


# consecutive_sim([2, 3, 3, 3, 8, 8, 6, 7, 7])


def consecutive_sim(lst):
    """
    Takes a list and returns a list of tuples (value, start_index, end_index)
    representing consecutive sequences of the same value.
    """
    idx = 0
    res = []


    while idx < len(lst):
        start = idx
        val = lst[idx]

        # Move index forward while the value remains the same
        while idx < len(lst) and lst[idx] == val:
            idx += 1

        end = idx - 1
        res.append((val, start, end))

    return res




# Eample 


print(consecutive_sim([2, 3, 3, 3, 8, 8, 6, 7, 7]))
