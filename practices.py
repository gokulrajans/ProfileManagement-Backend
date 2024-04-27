print("Hi Hellow World.....")

## list

list_name = ["Apple", "Mango", "Orange", "Pinapple", "Banana"]

print(list_name[1])
print(list_name[2])
print(list_name[3])

### In this we can use negative index also, if we apply negative index it will take it from the reverse.

print("negative index = -1 ", list_name[-1])
print("negative index = -2 ", list_name[-2])
print("negative index = -3 ", list_name[-3])

#Try except 

animalName = ['dog', 'cat','Tiger', 'lion']

try:
    tigerIndex = animalName.index('Tiger')
except:
    tigerIndex = 'Tiger is not available in the list'

print(tigerIndex)

## for loop

for animal in animalName:
    print("This is a " + animal)

