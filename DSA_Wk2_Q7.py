
def frequency(S:str):
    dict = {}
    for keys in S:
        dict[keys]=dict.get(keys, 0) + 1
    return dict
    
print(frequency(S="Count-Down"))


""" 
    Time Complexity: O(n)
    Space Complexity: O(1)
"""