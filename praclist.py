######################## Practice on list variable
# define a list
fishes = ['shark', 'marlin', 'turtle', 'octopus', 'squid']

# define a list of zoo animals
animals = ['lion', 'tiger','panda','horse','donkey']

#### retrieve a specific index from the list
fish1 = fishes[2]
#print(fish1)

# retrieve panda from your list
animals1 = animals[2]
#print(animals1)

# change the value of an item in the list
fishes[2] = 'jellyfish'
#print(fishes)

# change horse to monkey
animals[3] = 'monkey'
#print(animals)

# add an item to the list .append
fishes.append('whale')
#print(fishes)

# add elephant to your animals
animals.append("elephant")
#print(animals)

# to delete an item from the list del(), .remove()
del(fishes[0]) # delete by index
#print(fishes)

# delete lion
del(animals[0])
#print(animals)

# remove a value from the list 
fishes.remove('whale')
#print(fishes)

# remove donkey from your animals
animals.remove("donkey")
#print(animals)

# loop through a list
for fish in fishes:
  print(fish)

# print all the animals in your list
for animal in animals:
  print(animal)