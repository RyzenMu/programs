inner = 5
def func():
    global inner
    inner += 6

func()

print("the python is ", inner)