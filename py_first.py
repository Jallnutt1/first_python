def basic_function(name='',repeat=3):
    for i in range (repeat):
        print(f"Hello, {name}")
    return 'done'

print(basic_function(name='remi',repeat=2))
print(basic_function())
print(basic_function(repeat=5,name='luka'))



