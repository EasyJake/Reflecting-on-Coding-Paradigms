def flatten_and_sort(array):
  # Flatten the nested array using a list comprehension
  flattened = [item for sublist in array for item in sublist]

  # Sort the flattened list
  sorted_list = sorted(flattened)

  return sorted_list

# Example usage:
nested_arrays = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
result = flatten_and_sort(nested_arrays)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


#QUESTION: How does this solution ensure data immutability?
#ANSWER:  
# The solution ensures data immutability by not modifying any of the input data directly.

# The input array array is never altered; instead, a new list flattened is created to store the flattened version of the array.

# The sorting operation also respects immutability by using the sorted() function, which returns a new list rather than sorting the list in place. This is contrary to methods like .sort() which would modify the list on which it is called.



#QUESTION: Is this solution a pure function? Why or why not?
#ANSWER:  
# The solution is a pure function because it takes an input array and returns a sorted list without modifying the input data


#QUESTION: Is this solution a higher order function? Why or why not?
#ANSWER:  No, this solution is not a higher order function. A higher order function is defined as a function that takes a function as an argument or returns a function as its result. In this case, the flatten_and_sort function is not a higher order function.


#QUESTION: Would it have been easier to solve this problem using a different programming style?
#ANSWER:
# It depends. Using a procedural approach may have been more straightforward, but would involve more in-place modifications. OOP would be more complex and  would involve changes that wouldn't have additional benefits for such a simple function.


#QUESTION: Why in particular is functional programming a helpful paradigm when solving this problem?
#ANSWER:  
# Functional programming is good for this because it makes things clear and simple, focusing only on needed changes like flattening and sorting. It's easy to test and understand because it uses functions that rely only on what you give them and don't change anything else. This approach is safe and predictable, avoiding unwanted changes and mistakes,

