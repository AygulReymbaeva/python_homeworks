#q1
def count_occurrences(tpl, element):
    return tpl.count(element)
if __name__ == "__main__":
    my_tuple = (1, 2, 3, 2, 4, 2, 5)
    print("Occurrences of 2:", count_occurrences(my_tuple, 2))  
    print("Occurrences of 4:", count_occurrences(my_tuple, 4))  
    print("Occurrences of 6 (not in tuple):", count_occurrences(my_tuple, 6))  

#q2
def max_element(tpl):
    return max(tpl)
if __name__ == "__main__":
    my_tuple = (1, 5, 3, 9, 2)
    print("Max element:", max_element(my_tuple)) 
    print("Max element:", max_element((-10, -5, -2, -1)))  

#q3
def min_element(tpl):
    return min(tpl)
if __name__ == "__main__":
    my_tuple = (1, 5, 3, 9, 2)
    print("Min element:", min_element(my_tuple))  
    print("Min element:", min_element((-10, -5, -2, -1)))  

#q4
def check_element(tpl, element):
    return element in tpl
if __name__ == "__main__":
    my_tuple = (1, 5, 3, 9, 2)
    print("Is 3 in tuple?", check_element(my_tuple, 3))  
    print("Is 7 in tuple?", check_element(my_tuple, 7))  

#q5
def first_element(tpl):
    return tpl[0] if tpl else None
if __name__ == "__main__":
    my_tuple = (1, 5, 3, 9, 2)
    empty_tuple = ()
    print("First element:", first_element(my_tuple))  
    print("First element (empty tuple):", first_element(empty_tuple))  

#q6
def last_element(tpl):
    return tpl[-1] if tpl else None
if __name__ == "__main__":
    my_tuple = (1, 5, 3, 9, 2)
    empty_tuple = ()
    print("Last element:", last_element(my_tuple))  
    print("Last element (empty tuple):", last_element(empty_tuple))  

#q7
def tuple_length(tpl):
    return len(tpl)
if __name__ == "__main__":
    my_tuple = (1, 5, 3, 9, 2)
    empty_tuple = ()
    print("Tuple length:", tuple_length(my_tuple))  
    print("Tuple length (empty tuple):", tuple_length(empty_tuple))  

#q8
def slice_tuple(tpl):
    return tpl[:3]
if __name__ == "__main__":
    my_tuple = (1, 5, 3, 9, 2)
    short_tuple = (7, 8)
    empty_tuple = ()
    print("Sliced tuple:", slice_tuple(my_tuple))  
    print("Sliced tuple (less than 3 elements):", slice_tuple(short_tuple))  
    print("Sliced tuple (empty tuple):", slice_tuple(empty_tuple))  

#q9
def concatenate_tuples(tpl1, tpl2):
    return tpl1 + tpl2
if __name__ == "__main__":
    tuple1 = (1, 5, 3)
    tuple2 = (9, 2, 7)
    empty_tuple = ()
    print("Concatenated tuple:", concatenate_tuples(tuple1, tuple2))  
    print("Concatenated with empty tuple:", concatenate_tuples(tuple1, empty_tuple))  
    print("Concatenated empty tuples:", concatenate_tuples(empty_tuple, empty_tuple))  

#q10
def is_tuple_empty(tpl):
    return not tpl
if __name__ == "__main__":
    my_tuple = (1, 5, 3)
    empty_tuple = ()
    print("Is tuple empty?", is_tuple_empty(my_tuple))  
    print("Is tuple empty?", is_tuple_empty(empty_tuple))  

#q11
def get_all_indices(tpl, element):
    return [i for i, val in enumerate(tpl) if val == element]
if __name__ == "__main__":
    my_tuple = (1, 2, 3, 2, 4, 2, 5)
    print("Indices of 2:", get_all_indices(my_tuple, 2))  
    print("Indices of 4:", get_all_indices(my_tuple, 4))  
    print("Indices of 6 (not in tuple):", get_all_indices(my_tuple, 6))  

#q12
def second_largest(tpl):
    unique_elements = sorted(set(tpl), reverse=True)  
    return unique_elements[1] if len(unique_elements) > 1 else None
if __name__ == "__main__":
    my_tuple = (1, 5, 3, 9, 2, 9)
    print("Second largest element:", second_largest(my_tuple))  
    print("Second largest element (single element tuple):", second_largest((8,)))  
    print("Second largest element (all same values):", second_largest((4, 4, 4, 4)))  

#q13
def second_smallest(tpl):
    unique_elements = sorted(set(tpl))  
    return unique_elements[1] if len(unique_elements) > 1 else None
if __name__ == "__main__":
    my_tuple = (1, 5, 3, 9, 2, 1)
    print("Second smallest element:", second_smallest(my_tuple))  
    print("Second smallest element (single element tuple):", second_smallest((8,)))  
    print("Second smallest element (all same values):", second_smallest((4, 4, 4, 4)))  

#q14
def single_element_tuple(element):
    return (element,)
if __name__ == "__main__":
    single_tuple = single_element_tuple(5)
    print("Single-element tuple:", single_tuple)  
    print("Type check:", type(single_tuple))  

#q15
def list_to_tuple(lst):
    return tuple(lst)
if __name__ == "__main__":
    my_list = [1, 5, 3, 9, 2]
    empty_list = []
    print("Converted tuple:", list_to_tuple(my_list))  
    print("Converted tuple (empty list):", list_to_tuple(empty_list))  

#q16
def is_tuple_sorted(tpl):
    return tpl == tuple(sorted(tpl))
if __name__ == "__main__":
    sorted_tuple = (1, 2, 3, 4, 5)
    unsorted_tuple = (3, 1, 4, 2, 5)
    empty_tuple = ()
    single_element_tuple = (7,)
    print("Is sorted?", is_tuple_sorted(sorted_tuple))  
    print("Is sorted?", is_tuple_sorted(unsorted_tuple))  
    print("Is sorted? (empty tuple)", is_tuple_sorted(empty_tuple))  
    print("Is sorted? (single element)", is_tuple_sorted(single_element_tuple))  

#q17
def max_of_subtuple(tpl, start, end):
    sub_tpl = tpl[start:end] 
    return max(sub_tpl) if sub_tpl else None  
if __name__ == "__main__":
    my_tuple = (3, 8, 1, 7, 2, 9, 5)
    print("Max of subtuple (index 1 to 5):", max_of_subtuple(my_tuple, 1, 5))  
    print("Max of subtuple (index 3 to 6):", max_of_subtuple(my_tuple, 3, 6))  
    print("Max of subtuple (invalid range):", max_of_subtuple(my_tuple, 4, 4))  
    
#q18
def min_of_subtuple(tpl, start, end):
    sub_tpl = tpl[start:end]  
    return min(sub_tpl) if sub_tpl else None  
if __name__ == "__main__":
    my_tuple = (3, 8, 1, 7, 2, 9, 5)
    print("Min of subtuple (index 1 to 5):", min_of_subtuple(my_tuple, 1, 5))  
    print("Min of subtuple (index 3 to 6):", min_of_subtuple(my_tuple, 3, 6))  
    print("Min of subtuple (invalid range):", min_of_subtuple(my_tuple, 4, 4))  

#q19
def remove_element(tpl, element):
    if element in tpl:
        lst = list(tpl)  
        lst.remove(element)  
        return tuple(lst)  
    return tpl 
if __name__ == "__main__":
    my_tuple = (3, 8, 1, 7, 2, 9, 5, 7)
    print("Tuple after removing 7:", remove_element(my_tuple, 7))  
    print("Tuple after removing 3:", remove_element(my_tuple, 3))  
    print("Tuple after removing 10 (not in tuple):", remove_element(my_tuple, 10))  

#20
def create_nested_tuple(tpl, size):
    if size <= 0:
        return ()  
    return tuple(tpl[i:i + size] for i in range(0, len(tpl), size))
if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print("Nested tuple (size 3):", create_nested_tuple(my_tuple, 3))  
    print("Nested tuple (size 4):", create_nested_tuple(my_tuple, 4))  
    print("Nested tuple (size 2):", create_nested_tuple(my_tuple, 2))  
    print("Nested tuple (invalid size 0):", create_nested_tuple(my_tuple, 0))  

#q21
def repeat_elements(tpl, n):
    if n <= 0:
        return ()  
    return tuple(element for element in tpl for _ in range(n))
if __name__ == "__main__":
    my_tuple = (1, 2, 3)
    print("Repeated elements (n=3):", repeat_elements(my_tuple, 3))  
    print("Repeated elements (n=2):", repeat_elements(my_tuple, 2))  
    print("Repeated elements (n=0):", repeat_elements(my_tuple, 0))  
    print("Repeated elements (n=1):", repeat_elements(my_tuple, 1))  

#q22
def create_range_tuple(start, end, step=1):
    return tuple(range(start, end, step))
if __name__ == "__main__":
    print("Range tuple (1 to 10):", create_range_tuple(1, 11))  
    print("Range tuple (5 to 15, step 2):", create_range_tuple(5, 15, 2))  
    print("Range tuple (10 to 0, step -2):", create_range_tuple(10, 0, -2))  
    print("Range tuple (invalid range 5 to 5):", create_range_tuple(5, 5))  

#q23
def reverse_tuple(tpl):
    return tpl[::-1]  
if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 5)
    print("Reversed tuple:", reverse_tuple(my_tuple))  
    print("Reversed tuple (single element):", reverse_tuple((42,)))  
    print("Reversed tuple (empty):", reverse_tuple(()))  

#q24
def is_palindrome(tpl):
    return tpl == tpl[::-1]  
if __name__ == "__main__":
    print("Palindrome check (1, 2, 3, 2, 1):", is_palindrome((1, 2, 3, 2, 1)))  
    print("Palindrome check (4, 5, 6, 7):", is_palindrome((4, 5, 6, 7)))  
    print("Palindrome check (a, b, c, b, a):", is_palindrome(('a', 'b', 'c', 'b', 'a')))  
    print("Palindrome check (empty tuple):", is_palindrome(()))  
    print("Palindrome check (single element):", is_palindrome((42,)))  

#q25
def get_unique_elements(tpl):
    seen = set()
    return tuple(element for element in tpl if element not in seen and not seen.add(element))
if __name__ == "__main__":
    print("Unique elements:", get_unique_elements((1, 2, 3, 2, 4, 1, 5)))  
    print("Unique elements:", get_unique_elements(('a', 'b', 'a', 'c', 'b', 'd')))  
    print("Unique elements (empty tuple):", get_unique_elements(()))  
    print("Unique elements (single element):", get_unique_elements((42,)))  