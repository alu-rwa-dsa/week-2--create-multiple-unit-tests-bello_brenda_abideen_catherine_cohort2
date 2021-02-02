
def merged_list(ls):
    newlist = []
    for ls in ls:
        newlist.extend(ls)
        without_duplicates = set(newlist)
        list_without_duplicates = list(without_duplicates)

    return list_without_duplicates

mylist = [[1,1,8,8,3,7], ["Jane", "Doe", "Mark","Doe", "Chris"]]

print(merged_list(mylist))

# time complexity : O(N)
# space complexity : O(1)
