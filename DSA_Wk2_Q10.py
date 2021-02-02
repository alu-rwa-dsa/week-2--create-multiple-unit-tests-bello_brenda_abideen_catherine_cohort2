#Brenda

def show_ocurrence(num):
    final_list = []
    user_value = num
    occurrence = 1

    while user_value != 0:  # O(N) for going through the number the user provides
        adds_to_final_list = num - (user_value - 1)
        final_list.append(adds_to_final_list)

        if occurrence == adds_to_final_list:
            user_value = user_value - 1  # calculates next number
            occurrence = 1
        else:
            occurrence = occurrence + 1  # O(logn) for the if..else

    return final_list

print("The final list will be: " + str(show_ocurrence(4)))

# Time Complexity : O(nlogn)
# Space Complexity : O(1)