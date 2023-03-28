# Important keywords in python

#1. Continue

for m in range(21, 55):
    if m % 2 == 0 or m % 3 == 0:
        continue
    print(m, end='-')
print(end="\n")

# 2. Not
for n in range(1, 11):
    if not(n%2 == 0):
        print(n, sep="-", end="-")
print(end="\n")


#3. Assert
# assert will give assertion error if a condtion fails
#example 1
assert 10>5
# assert 5>10
#example 2
try:
    assert 10 < 5
except AssertionError:
    print("enter correct number")