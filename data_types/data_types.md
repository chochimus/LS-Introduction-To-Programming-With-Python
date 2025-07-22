# Data Types

### Primatives

primatives are fundamental data types that are used to build
up more complex types

- integers (int)
- floats (float)
- booleaan (bool)
- stings (str)

### Non-primtatives 

these non-primatives are called collections as they are single objects built up of multiple items, but not all non-primatives
are collections (such as functions)

- ranges (range) non-mutable
- tuples (tuples) non-mutable
- lists (list) mutable
- dictionaries (dict) mutable
- sets (set) mutable
- frozen sets (frozenset) non-mutable

# Literals

these are the actual syntactic representation of objects used 
to represent object in source code

```python
'Hello' # str literal
3.1241592 # float literal
True # bool literal
{'a': 1, 'b': 2} # dict literal
[1, 2, 3] # list literal
(4, 5, 6) # tuple literal
{7, 8, 9} # set literal
```
not all objects have literals and instead use constructors to
create an object of that type

```python
range(10) # range from 0-9
range(1, 11) # range from 1-10
set() # Empty set
frozenset([1, 2]) # Frozen set with values 1 and 2
```

# Variables and Assignment

used to identify values, aka identifiers including
variables, constants, function names, class names and more

the syntax when creating variables is known as assignment 
we can say a variable x is assigned a value 1 or 1 is assigned
to the variable x.

The first time a variable is assigned it is referred to as 
initialization.

# Text sequence

strings built up of any types of characters, the main difference 
between other sequences is that they don't contain any objects,
they contain characters but they are not objects, they're
simply apart of the string value

any type of quote can be used to represent strings, but
triple quotes are often used for multiline strings.

you can use the backslash to escape \ special characters in
regular strings, raw strings can represent special characters
without escaping.  ```r"raw string\```

finally you can use formatted strings or f-strings to interpolate
values in a string such as ```f'string {expression}``` where
expression will instead show up as the value of the expression.

# None

None use used to represent the absece of a value