#q1
def get_value(dictionary, key, default=None):
    return dictionary.get(key, default)
data = {"name": "Aygul", "age": 19,  "city": "Nukus"}
print(get_value(data, "name"))
print(get_value(data, "age"))       
print(get_value(data, "city"))     
print(get_value(data, "country"))  

#q2
def check_key(dictionary, key):
    return key in dictionary
data = {"name": "ygul", "age": 19, "city": "Nukus"}
print(check_key(data, "age"))  
print(check_key(data, "country"))

#q3
def count_keys(dictionary):
    return len(dictionary)
data = {"name": "ygul", "age": 19, "city": "Nukus"}
print(count_keys(data)) 

#q4
def get_all_keys(dictionary):
    return list(dictionary.keys())
data = {"name": "Aygul", "age": 19, "city": "Nukus"}
print(get_all_keys(data))  

#q5
def get_all_values(dictionary):
    return list(dictionary.values())
data = {"name": "Aygul", "age": 19, "city": "Nukus"}
print(get_all_values(data)) 

#q6
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}
dict_a = {"name": "Aygul", "age": 19}
dict_b = {"city": "Nukus", "age": 20} 
merged_dict = merge_dictionaries(dict_a, dict_b)
print(merged_dict) 

#q7
def remove_key(dictionary, key):
    dictionary.pop(key, None)
    return dictionary
sample_dict = {"name": "Aygul", "age": 19, "city": "Nukus"}
updated_dict = remove_key(sample_dict, "age")
print(updated_dict)  

#q8
def clear_dictionary(dictionary):
    return {}  
sample_dict = {"name": "Aygul", "age": 19, "city": "Nukus"}
empty_dict = clear_dictionary(sample_dict)
print(empty_dict)  

#q9
def is_dictionary_empty(dictionary):
    return not bool(dictionary)  
empty_dict = {}
non_empty_dict = {"key": "value"}
print(is_dictionary_empty(empty_dict))   
print(is_dictionary_empty(non_empty_dict)) 

#q10
def get_key_value_pair(dictionary, key):
    if key in dictionary:
        return {key: dictionary[key]} 
    return None  
data = {"name": "Aygul", "age": 19, "city": "Nukus"}
print(get_key_value_pair(data, "age"))
print(get_key_value_pair(data, "country"))  

#q11
def update_value(dictionary, key, new_value):
    dictionary[key] = new_value 
    return dictionary
data = {"name": "Aygul", "age": 19, "city": "Nukus"}
print(update_value(data, "age", 19))  
print(update_value(data, "country", "Karakalpakstan"))  

#q12
def count_value_occurrences(dictionary, target_value):
    return list(dictionary.values()).count(target_value)
data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 10}
print(count_value_occurrences(data, 10))
print(count_value_occurrences(data, 20)) 
print(count_value_occurrences(data, 50))  

#q13
def invert_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}
data = {"a": 1, "b": 2, "c": 3}
print(invert_dictionary(data))  

#q14
def find_keys_with_value(dictionary, target_value):
    return [key for key, value in dictionary.items() if value == target_value]
data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 10}
print(find_keys_with_value(data, 10)) 
print(find_keys_with_value(data, 20))  
print(find_keys_with_value(data, 50))  

#q15
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))
keys = ["name", "age", "city"]
values = ["Aygul", 19, "Nukus"]
result = create_dict_from_lists(keys, values)
print(result)  

#q16
def has_nested_dict(d):
    return any(isinstance(value, dict) for value in d.values())
data = {
    "name": "Aygul",
    "age": 19,
    "details": {
        "city": "Nukus",
        "university": "New Uzbekistan University"
    }
}
print(has_nested_dict(data)) 
data2 = {
    "name": "Aygul",
    "age": 19
}
print(has_nested_dict(data2))  

#q17
def get_nested_value(d, keys, default=None):
    for key in keys:
        if isinstance(d, dict) and key in d:
            d = d[key]  
        else:
            return default 
    return d

nested_dict = {
    "user": {
        "profile": {
            "name": "Aygul",
            "age": 19
        }
    }
}
print(get_nested_value(nested_dict, ["user", "profile", "name"]))  
print(get_nested_value(nested_dict, ["user", "profile", "age"]))   
print(get_nested_value(nested_dict, ["user", "profile", "city"], "Not Found"))

#q18
from collections import defaultdict
default_dict = defaultdict(int)
print(default_dict["score"]) 
default_dict["score"] += 10
print(default_dict["score"])  

#q19
def count_unique_values(dictionary):
    return len(set(dictionary.values()))
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
result = count_unique_values(data)
print(result)  

#q20
def sort_dict_by_key(dictionary):
    return dict(sorted(dictionary.items()))
data = {
    "b": 2,
    "a": 1,
    "d": 4,
    "c": 3
}
sorted_dict = sort_dict_by_key(data)
print(sorted_dict)

#q21
def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))
data = {
    "b": 20,
    "a": 10,
    "d": 40,
    "c": 30
}
sorted_dict = sort_dict_by_value(data)
print(sorted_dict)

#q22
def filter_dict_by_value(dictionary, condition):
    return {key: value for key, value in dictionary.items() if condition(value)}
data = {
    "a": 10,
    "b": 25,
    "c": 30,
    "d": 5
}
filtered_dict = filter_dict_by_value(data, lambda x: x > 15)
print(filtered_dict)

#q23
def have_common_keys(dict1, dict2):
    return bool(set(dict1.keys()) & set(dict2.keys()))  
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 10, "d": 20, "e": 30}
result = have_common_keys(dict1, dict2)
print(result)  

#q24
def tuple_to_dict(tuples):
    return dict(tuples) 
tuple_data = (("a", 1), ("b", 2), ("c", 3))
result = tuple_to_dict(tuple_data)
print(result)  

#q25
def get_first_pair(dictionary):
    if not dictionary:  
        return None  
    return next(iter(dictionary.items())) 
data = {"a": 1, "b": 2, "c": 3}
result = get_first_pair(data)
print(result)  