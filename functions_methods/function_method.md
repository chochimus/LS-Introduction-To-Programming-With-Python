falsy values include
- False
- None
- all 0 values
- empty collections

any returns true if any value is trthy all returns true
if all values return true in a collection

mostly any object with the same value will have a distinct 
id(object), however Interning makes this not necessarily true
for integers -5 - 256 and some strings

variable shadowing is when using two variables in different scope,
the lowest level of scope takes precedence

Python has function scope, but not block scope

Arguments are passed to a function call, parameters are the
variables in function definitions (placeholders for 
potential arguments)

functions by default have None as an Implicit return value,
otherwise you can return any value with Explicit return value 
using the return keyword

default parameters can be set in function definitions,
e.g. def function(number=2), you can define defaults for any
or all parameters, however, once you specify a default all
subsequent parameters must also have a default

it is also worth noting that if one default parameter is used,
you can't follow it with an explicit subsequent parameter

methods are a type of function that works with specific objects
defined in the class

functions that refer to modules such as math.sqrt are NOT
methods, they don't operate on the math Object it is solely
to tell python where to find the function

some functions mutate the caller , list.pop()
and some mutate the argument:
```python
def add_new_number(my_list):
    my_list.append(9)

numbers = [1, 2, 3, 4, 5]
add_new_number(numbers)
print(numbers) # [1, 2, 3, 4, 5, 9]
```

mutating the caller is normal, while mutating arguments
should be avoided BAD PRACTICE