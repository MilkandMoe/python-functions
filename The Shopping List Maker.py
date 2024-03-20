items = []

def add_items_to_list(items):
    item = input("What item to add?")
    items.append(item)
    print(items)
    
   
def remove_items(items):
    item2 = input("What item to discard?")
    items.remove(item2)
    print(items)    
    


 
def list_format(items):
    print(items)
    
add_items_to_list(items)
remove_items(items)
list_format(items)