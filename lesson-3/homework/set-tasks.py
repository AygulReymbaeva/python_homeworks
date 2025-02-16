#q1
def union_of_sets(set1, set2):
    return set1 | set2 
if __name__ == "__main__":
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print("Union of sets:", union_of_sets(set_a, set_b))  
    print("Union (with empty set):", union_of_sets(set_a, set()))  
    print("Union (identical sets):", union_of_sets(set_a, set_a))  
  
#q2
def intersection_of_sets(set1, set2):
    return set1 & set2 
if __name__ == "__main__":
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print("Intersection of sets:", intersection_of_sets(set_a, set_b))  
    print("Intersection (no common elements):", intersection_of_sets(set_a, {7, 8}))  
    print("Intersection (with empty set):", intersection_of_sets(set_a, set()))  
    print("Intersection (identical sets):", intersection_of_sets(set_a, set_a))  

#q3
def difference_of_sets(set1, set2):
    return set1 - set2 
if __name__ == "__main__":
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print("Difference (set_a - set_b):", difference_of_sets(set_a, set_b))  
    print("Difference (set_b - set_a):", difference_of_sets(set_b, set_a))  
    print("Difference (with empty set):", difference_of_sets(set_a, set()))  
    print("Difference (identical sets):", difference_of_sets(set_a, set_a))  

#q4
def subset(set1, set2):
    return set1 <= set2 
if __name__ == "__main__":
    set_a = {1, 2}
    set_b = {1, 2, 3, 4}
    set_c = {5, 6}
    print("Is set_a a subset of set_b?:", subset(set_a, set_b))  
    print("Is set_b a subset of set_a?:", subset(set_b, set_a))  
    print("Is set_c a subset of set_b?:", subset(set_c, set_b))  
    print("Is an empty set a subset of set_b?:", subset(set(), set_b))  
    print("Is set_b a subset of itself?:", subset(set_b, set_b))  

#q5
def check_element(s, element):
    return element in s 
if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5}
    print("Is 3 in the set?:", check_element(my_set, 3))  
    print("Is 6 in the set?:", check_element(my_set, 6))  
    print("Check in an empty set:", check_element(set(), 1))  

#q6
def set_length(s):
    return len(s)  
if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5}
    print("Length of the set:", set_length(my_set))  
    print("Length of an empty set:", set_length(set()))  
    print("Length of a set with duplicate elements:", set_length({1, 2, 2, 3, 3, 3, 4}))  

#q7
def list_to_set(lst):
    return set(lst) 
if __name__ == "__main__":
    my_list = [1, 2, 2, 3, 4, 4, 5]
    print("Converted set:", list_to_set(my_list))  
    print("Converted empty list:", list_to_set([]))  
    print("Converted list with all identical elements:", list_to_set([7, 7, 7, 7]))  

#q8
def remove_element(s, element):
    s.discard(element) 
if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5}
    remove_element(my_set, 3)
    print("Set after removing 3:", my_set)  
    remove_element(my_set, 10)  
    print("Set after trying to remove 10:", my_set)  
    empty_set = set()
    remove_element(empty_set, 1)
    print("Empty set after removal attempt:", empty_set)  

#q9
def clear_set(s):
    s.clear()  
if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5}
    print("Original set:", my_set)  
    clear_set(my_set)
    print("Set after clearing:", my_set)  

#q10
def is_set_empty(s):
    return len(s) == 0  
if __name__ == "__main__":
    my_set = {1, 2, 3}
    empty_set = set()
    print("Is my_set empty?:", is_set_empty(my_set))  
    print("Is empty_set empty?:", is_set_empty(empty_set))  

#q11
def symmetric_difference(set1, set2):
    return set1 ^ set2 
if __name__ == "__main__":
    setA = {1, 2, 3, 4}
    setB = {3, 4, 5, 6}
    print("Symmetric difference:", symmetric_difference(setA, setB))  
    print("Symmetric difference with empty set:", symmetric_difference(setA, set()))  
    print("Symmetric difference of identical sets:", symmetric_difference({1, 2}, {1, 2}))  

#q12
def add_element(s, element):
    s.add(element)  
if __name__ == "__main__":
    my_set = {1, 2, 3}
    add_element(my_set, 4)
    print("Set after adding 4:", my_set)  
    add_element(my_set, 2) 
    print("Set after trying to add 2 again:", my_set)  
    empty_set = set()
    add_element(empty_set, 5)
    print("Empty set after adding 5:", empty_set)  

#q13
def pop_element(s):
    return s.pop() if s else None 
if __name__ == "__main__":
    my_set = {10, 20, 30, 40}
    popped = pop_element(my_set)
    print("Popped element:", popped)  
    print("Set after popping:", my_set)  
    empty_set = set()
    print("Popped from empty set:", pop_element(empty_set))  

#q14
def find_max(s):
    return max(s) if s else None 
if __name__ == "__main__":
    num_set = {10, 20, 30, 40, 50}
    print("Maximum element:", find_max(num_set))  
    empty_set = set()
    print("Maximum of empty set:", find_max(empty_set))  

#q15
def find_min(s):
    return min(s) if s else None 
if __name__ == "__main__":
    num_set = {10, 20, 30, 40, 50}
    print("Minimum element:", find_min(num_set))  
    empty_set = set()
    print("Minimum of empty set:", find_min(empty_set))  

#q16
def filter_even_numbers(s):
    return {num for num in s if num % 2 == 0}
if __name__ == "__main__":
    num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print("Even numbers set:", filter_even_numbers(num_set))  
    empty_set = set()
    print("Even numbers from empty set:", filter_even_numbers(empty_set))  

#q17
def filter_odd_numbers(s):
    return {num for num in s if num % 2 != 0}
if __name__ == "__main__":
    num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print("Odd numbers set:", filter_odd_numbers(num_set))  
    empty_set = set()
    print("Odd numbers from empty set:", filter_odd_numbers(empty_set))  

#q18
def create_range_set(start, end):
    return set(range(start, end + 1))
if __name__ == "__main__":
    print("Set of range 1 to 10:", create_range_set(1, 10))  
    print("Set of range 5 to 15:", create_range_set(5, 15))  

#q19
def merge_and_deduplicate(list1, list2):
    return set(list1) | set(list2)  
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    print("Merged and deduplicated set:", merge_and_deduplicate(list1, list2))  

#q20
def check_disjoint(set1, set2):
    return set1.isdisjoint(set2)
if __name__ == "__main__":
    setA = {1, 2, 3, 4}
    setB = {5, 6, 7, 8}
    print("Are the sets disjoint?", check_disjoint(setA, setB))  
    setC = {3, 4, 5}
    print("Are the sets disjoint?", check_disjoint(setA, setC))  
   
#q21
def remove_duplicates(lst):
    return list(set(lst))
lst = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_lst = remove_duplicates(lst)
print(unique_lst) 

#q22
def count_unique_elements(lst):
    return len(set(lst))
lst = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_count = count_unique_elements(lst)
print(unique_count)  

#q23
import random
def generate_random_set(size, start, end):
    return set(random.sample(range(start, end + 1), min(size, end - start + 1)))
random_set = generate_random_set(5, 1, 20)
print(random_set)  
