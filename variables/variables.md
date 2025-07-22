idomatic variables use snake_case
idomatic constants use SCREAMING_SNAKE_CASE
class use PascalCase

when creating a variable in python, first the value
is stored at mem address then the variable is created somewhere
else in mem, the variable stores the address to where the value
is in memory and the variable (ptr) has its own address

when reassigning a new value, the variable still exists,
the ptr now just points to the other value in memory
