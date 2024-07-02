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


# Define the base Podracer class
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

# Define AnakinsPod class inheriting from Podracer
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

# Define SebulbasPod class inheriting from Podracer
class SebulbasPod(Podracer):
    def flame_jet(self, other):
        other.condition = "trashed"

# Example usage
anakin_pod = AnakinsPod(200, "perfect", 1500)
sebulba_pod = SebulbasPod(180, "repaired", 1800)

# Anakin uses boost
anakin_pod.boost()

# Sebulba uses flame_jet on Anakin's podracer
sebulba_pod.flame_jet(anakin_pod)

print(f"Anakin's Pod Speed: {anakin_pod.max_speed}, Condition: {anakin_pod.condition}")
print(f"Sebulba's Pod Speed: {sebulba_pod.max_speed}, Condition: {sebulba_pod.condition}")


# How does this solution demonstrate the four pillars of OOP?

# * Encapsulation: The Podracer class encapsulates elements relevant to all podracer types, such as max_speed, condition, and price. The behaviors like repair(), boost(), and flame_jet() manipulate the state of these objects in a way that ensures the internal states are safe from external interference.

# * Abstraction: The Podracer class provides a base that is a template for all types of pods. It specifies what a podracer should have and do, but t some methods (like boost and flame_jet) are left to the child classes. 

# * Inheritance: AnakinsPod and SebulbasPod inherit from the base Podracer class. They use the same constructor and the repair method from the base class but also extend additional capabilities (boosting speed and damaging others), demonstrating a clear "is-a" relationship.

# * Polymorphism: This principle is demonstrated by the ability of AnakinsPod and SebulbasPod to implement and extend the base class in different ways. Both classes can behave differently (e.g., one can boost speed, and the other can damage other racers) while still being treated as Podracers.

# 2. Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# Using an object-oriented approach works for this because it mirrors real-world entities (podracers) with distinct characteristics and behaviors. While a procedural or functional approach might handle this problem, they could potentially lead to less organized and harder-to-maintain code as the complexity of the system grows (e.g., adding more podracer types with unique behaviors).


# 3. How did Object Oriented Programming assist in solving this problem?
# Object-oriented programming assists in organizing the code by aligning it with the model of the problem. It makes the system scalable, maintainable, and provides clear separation of concerns. 