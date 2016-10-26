grocery_list = ["apple", "orange", "banana"]

def add_to_list():
    choice = raw_input("What would you like to add to the list?")
    if grocery_list.count(choice) >= 1:
        print "Item is already in the list!"
    else:
        grocery_list.append(choice)



def list_alpha_order():
    grocery_list.sort()
    return grocery_list


def remove_item():
    grocery_list.remove(banana)


#create blank list
# only add new items, no duplicates
# if it exists, tell user that it already exists
# make sure it's all lower case
# show an updated list in alpha order after an item is added



# 