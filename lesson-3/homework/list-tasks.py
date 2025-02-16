#q1
def count_occurrences(lst, element):
    return lst.count(element)
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 2, 2, 5, 2]
    element = 2
    print("Occurrences of", element, ":", count_occurrences(my_list, element))

#q2
def sum_of_elements(lst):
    return sum(lst)

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print("Sum of elements:", sum_of_elements(my_list))

#q3
def max_element(lst):
    return max(lst)
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2]
    print("Largest element:", max_element(my_list))

#q4
def min_element(lst):
    return min(lst)
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2]
    print("Smallest element:", min_element(my_list))

#q5
def check_element(lst, element):
    return element in lst
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2]
    element = 3
    print("Element found:", check_element(my_list, element))

#q6
def first_element(lst):
    return lst[0] if lst else None
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2]
    print("First element:", first_element(my_list))
    empty_list = []
    print("First element of empty list:", first_element(empty_list))

#q7
def last_element(lst):
    return lst[-1] if lst else None
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2]
    print("Last element:", last_element(my_list))
    empty_list = []
    print("Last element of empty list:", last_element(empty_list))

#q8
def slice_list(lst):
    return lst[:3]
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2, 7]
    print("Sliced list:", slice_list(my_list))
    short_list = [8, 4]  # Less than 3 elements
    print("Sliced short list:", slice_list(short_list))

#q9
def reverse_list(lst):
    return lst[::-1]
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2]
    print("Reversed list:", reverse_list(my_list))
    empty_list = []
    print("Reversed empty list:", reverse_list(empty_list))

#q10
def sort_list(lst):
    return sorted(lst)
if __name__ == "__main__":
    my_list = [5, 1, 9, 3, 2]
    print("Sorted list:", sort_list(my_list))
    empty_list = []
    print("Sorted empty list:", sort_list(empty_list))

#q11
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
if __name__ == "__main__":
    my_list = [5, 1, 9, 3, 2, 1, 5, 3, 9]
    print("List without duplicates:", remove_duplicates(my_list))
    empty_list = []
    print("Empty list without duplicates:", remove_duplicates(empty_list))

#q12
def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2]
    print("List after insertion:", insert_element(my_list, 7, 2))  
    empty_list = []
    print("Empty list after insertion:", insert_element(empty_list, 10, 0)) 

#q13
def index_of_element(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1  # Return -1 if the element is not found
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2, 3]
    print("Index of 3:", index_of_element(my_list, 3))  
    print("Index of 7:", index_of_element(my_list, 7))

#q14
def is_empty(lst):
    return len(lst) == 0
if __name__ == "__main__":
    my_list = [1, 2, 3]
    empty_list = []
    print("Is my_list empty?", is_empty(my_list)) 
    print("Is empty_list empty?", is_empty(empty_list)) 

#q15
def count_even_numbers(lst):
    return sum(1 for num in lst if num % 2 == 0)
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Count of even numbers:", count_even_numbers(my_list))  
    empty_list = []
    print("Count of even numbers in empty list:", count_even_numbers(empty_list))

#q16
def count_odd_numbers(lst):
    return sum(1 for num in lst if num % 2 != 0)
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Count of odd numbers:", count_odd_numbers(my_list)) 
    empty_list = []
    print("Count of odd numbers in empty list:", count_odd_numbers(empty_list))

#q17
def concatenate_lists(lst1, lst2):
    return lst1 + lst2
if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print("Concatenated list:", concatenate_lists(list1, list2)) 
    empty_list = []
    print("Concatenated with empty list:", concatenate_lists(list1, empty_list)) 

#q18
def is_sublist(lst, sublst):
    if not sublst:
        return True  
    n, m = len(lst), len(sublst)
    for i in range(n - m + 1):
        if lst[i:i + m] == sublst:
            return True
    return False
if __name__ == "__main__":
    main_list = [1, 2, 3, 4, 5, 6]
    print("Is [3, 4, 5] a sublist?", is_sublist(main_list, [3, 4, 5]))  
    print("Is [4, 6] a sublist?", is_sublist(main_list, [4, 6]))  
    print("Is [] a sublist?", is_sublist(main_list, [])) 

#q19
def replace_element(lst, old, new):
    try:
        index = lst.index(old)  
        lst[index] = new  
    except ValueError:
        pass  
    return lst
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 2, 5]
    print("List after replacement:", replace_element(my_list, 2, 99))  
    print("List after trying to replace 10:", replace_element(my_list, 10, 50))  

#q20
def second_largest(lst):
    unique_lst = list(set(lst)) 
    if len(unique_lst) < 2:
        return None  
    unique_lst.sort(reverse=True)  
    return unique_lst[1]  
if __name__ == "__main__":
    my_list = [5, 1, 9, 3, 7, 9]
    print("Second largest element:", second_largest(my_list)) 
    short_list = [4]
    print("Second largest element in short list:", second_largest(short_list))  
    duplicate_list = [3, 3, 3]
    print("Second largest element in duplicate list:", second_largest(duplicate_list))  

#q21
def second_smallest(lst):
    unique_lst = list(set(lst))  
    if len(unique_lst) < 2:
        return None  
    unique_lst.sort()  
    return unique_lst[1]  
if __name__ == "__main__":
    my_list = [5, 1, 9, 3, 7, 1]
    print("Second smallest element:", second_smallest(my_list))  
    short_list = [4]
    print("Second smallest element in short list:", second_smallest(short_list))  
    duplicate_list = [3, 3, 3]
    print("Second smallest element in duplicate list:", second_smallest(duplicate_list))  

#q22
def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Even numbers:", filter_even_numbers(my_list))  
    empty_list = []
    print("Even numbers in empty list:", filter_even_numbers(empty_list)) 

#q23
def filter_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Odd numbers:", filter_odd_numbers(my_list)) 
    empty_list = []
    print("Odd numbers in empty list:", filter_odd_numbers(empty_list)) 

#q24
def list_length(lst):
    return len(lst)
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print("Length of the list:", list_length(my_list))  
    empty_list = []
    print("Length of empty list:", list_length(empty_list))  

#q25
def copy_list(lst):
    return lst.copy()
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    copied_list = copy_list(my_list)
    print("Original list:", my_list)  
    print("Copied list:", copied_list)  
    copied_list.append(6)
    print("Modified copied list:", copied_list)  
    print("Original list remains unchanged:", my_list)  

#q26
def get_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None  
    mid = n // 2
    return lst[mid] if n % 2 != 0 else (lst[mid - 1], lst[mid])
if __name__ == "__main__":
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4, 5, 6]
    empty_list = []
    print("Middle of odd list:", get_middle_element(odd_list)) 
    print("Middle of even list:", get_middle_element(even_list)) 
    print("Middle of empty list:", get_middle_element(empty_list))  

#q27
def max_of_sublist(lst, start, end):
    if start < 0 or end > len(lst) or start >= end:
        return None 
    return max(lst[start:end])
if __name__ == "__main__":
    my_list = [3, 7, 2, 9, 5, 1, 8]
    print("Max of sublist [1:5]:", max_of_sublist(my_list, 1, 5))  
    print("Max of sublist [2:6]:", max_of_sublist(my_list, 2, 6))  
    print("Invalid sublist:", max_of_sublist(my_list, 4, 2))  

#q28
def min_of_sublist(lst, start, end):
    if start < 0 or end > len(lst) or start >= end:
        return None
    return min(lst[start:end])
if __name__ == "__main__":
    my_list = [3, 7, 2, 9, 5, 1, 8]
    print("Min of sublist [1:5]:", min_of_sublist(my_list, 1, 5))  
    print("Min of sublist [2:6]:", min_of_sublist(my_list, 2, 6))  
    print("Invalid sublist:", min_of_sublist(my_list, 4, 2))  

#q29
def remove_element_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]  
    return lst
if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    print("List after removing index 2:", remove_element_by_index(my_list, 2))  
    print("Trying to remove index 10:", remove_element_by_index(my_list, 10))  

#q30
def is_sorted(lst):
    return lst == sorted(lst)
if __name__ == "__main__":
    sorted_list = [1, 2, 3, 4, 5]
    unsorted_list = [3, 1, 4, 2, 5]
    print("Is sorted_list sorted?", is_sorted(sorted_list))  
    print("Is unsorted_list sorted?", is_sorted(unsorted_list))  

#q31
def repeat_elements(lst, n):
    return [elem for elem in lst for _ in range(n)]
if __name__ == "__main__":
    my_list = [1, 2, 3]
    print("Repeated elements (3 times):", repeat_elements(my_list, 3))  
    print("Repeated elements (1 time):", repeat_elements(my_list, 1))  
    print("Repeated elements (0 times):", repeat_elements(my_list, 0))  

#q32
def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)
if __name__ == "__main__":
    list1 = [3, 1, 4]
    list2 = [2, 5, 0]
    print("Merged and sorted list:", merge_and_sort(list1, list2))  

#q33
def find_all_indices(lst, element):
    return [index for index, value in enumerate(lst) if value == element]
if __name__ == "__main__":
    my_list = [1, 2, 3, 2, 4, 2, 5]
    print("Indices of 2:", find_all_indices(my_list, 2))  
    print("Indices of 4:", find_all_indices(my_list, 4))  
    print("Indices of 6 (not in list):", find_all_indices(my_list, 6))  

#q34
def rotate_list(lst, k):
    if not lst:
        return lst 
    k = k % len(lst) 
    return lst[-k:] + lst[:-k]
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print("Rotated by 2:", rotate_list(my_list, 2))  
    print("Rotated by 5 (same as original):", rotate_list(my_list, 5))  
    print("Rotated by 7 (handles large k):", rotate_list(my_list, 7))  
    print("Rotated empty list:", rotate_list([], 3))  

#q35
def create_range_list(start, end):
    return list(range(start, end + 1))
if __name__ == "__main__":
    print("Range from 1 to 10:", create_range_list(1, 10))  
    print("Range from 5 to 15:", create_range_list(5, 15))  
    print("Range from -3 to 3:", create_range_list(-3, 3))  

#q36
def sum_of_positive_numbers(lst):
    return sum(num for num in lst if num > 0)
if __name__ == "__main__":
    my_list = [-5, 10, -3, 7, 0, -2, 8]

    print("Sum of positive numbers:", sum_of_positive_numbers(my_list))  
    print("Sum of positive numbers (all negative):", sum_of_positive_numbers([-1, -2, -3]))  
    print("Sum of positive numbers (empty list):", sum_of_positive_numbers([]))  

#q37
def sum_of_negative_numbers(lst):
    return sum(num for num in lst if num < 0)
if __name__ == "__main__":
    my_list = [-5, 10, -3, 7, 0, -2, 8]
    print("Sum of negative numbers:", sum_of_negative_numbers(my_list))  
    print("Sum of negative numbers (all positive):", sum_of_negative_numbers([1, 2, 3]))  
    print("Sum of negative numbers (empty list):", sum_of_negative_numbers([]))  

#q38
def is_palindrome(lst):
    return lst == lst[::-1]
if __name__ == "__main__":
    print("Is [1, 2, 3, 2, 1] a palindrome?", is_palindrome([1, 2, 3, 2, 1]))  
    print("Is [1, 2, 3, 4, 5] a palindrome?", is_palindrome([1, 2, 3, 4, 5]))  
    print("Is [] a palindrome?", is_palindrome([]))  
    print("Is [7] a palindrome?", is_palindrome([7]))  

#q39
def create_nested_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Nested list (size 3):", create_nested_list(my_list, 3))  
    print("Nested list (size 4):", create_nested_list(my_list, 4))  
    print("Nested list (size 2):", create_nested_list(my_list, 2))  
    print("Nested list (size 10):", create_nested_list(my_list, 10))  

#q40
def get_unique_elements(lst):
    seen = set()
    return [x for x in lst if x not in seen and not seen.add(x)]
if __name__ == "__main__":
    my_list = [1, 2, 3, 2, 4, 1, 5, 3, 6]
    print("Unique elements in order:", get_unique_elements(my_list))  
    print("Unique elements in order:", get_unique_elements([4, 5, 4, 6, 7, 5, 8]))  
    print("Unique elements in order (empty list):", get_unique_elements([]))  
