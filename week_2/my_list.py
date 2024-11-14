
# step 1
my_list = [];

# step 2
# my_list.append(10,20,30,40);

my_list.extend([10,20,30,40]);

# step 3
my_list.insert(1,15)

# step 4
my_list.extend([50,60,70]);

# step 5
# my_list.remove(70)
my_list.pop();

# step 6
my_list.sort();

# step 7
index_find = my_list.index(30)

print(index_find);

print(my_list);