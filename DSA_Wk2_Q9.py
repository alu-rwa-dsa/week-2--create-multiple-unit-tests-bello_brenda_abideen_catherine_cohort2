
def question9(listA,listB):
    for i in listA:
        if i not in listB:
            return i

list1 = [9,5,3,2,6]
list2 = [9,5,2,6]

print(question9(list1,list2))

# Time Complexity : O(A * B)
# Space Complexity : O(1)