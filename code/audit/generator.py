# generator function form : gen--
def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)

# next() : access the next element
g = gencubes(10)
for i in range(10):
    print(next(g))

# iter() : personally make an object into iterator
s = "hello"
s_iter = iter(s)
print(next(s_iter))
