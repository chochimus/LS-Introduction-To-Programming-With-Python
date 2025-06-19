foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# prints bar as the foo inside of the set_foo function isn't in scope
# when print is called and instead ignored