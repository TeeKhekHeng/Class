#Given two lists, l1 and l2, write a program to create a third list l3 by
#picking an odd-index element from the list l1 and even index elements from the list l2.

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

lt1 = []
lt2 = []

for i in range(len(l1)):
    if i % 2 != 0:
        lt1.append(l1[i])

#lt1 = l1[1::2]
#(list1[start : stop : step])

for i in range(len(l2)):
    if i % 2 == 0:
        lt2.append(l2[i])

#lt2 = l2[0::2]

print("Element at odd-index positions from list one:")
print(lt1)
print("Element at even-index positions from list two:")
print(lt2)

l3 = lt1 +lt2

#l3 = []
#l3.extend(lt1)
#l3.extend(lt2)

print("Printing Final third list")
print(l3)

"""
Output:
Element at odd-index positions from list one:
[6, 12, 18]
Element at even-index positions from list two:
[4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""
