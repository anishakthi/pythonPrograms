class Node:


    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node



def add(data):
    global pre_node
    global head
    pre_node = None
    new_node = Node()
    new_node.data = data
    new_node.next = pre_node
    if pre_node == None :
        head = new_node
    else :
        pre_node.next = new_node
    pre_node = new_node


def list_print(node):
    print node.data
    if node.next != None :
        list_print(node.next)


add(5)
add(6)
add(7)
print head.data
print head.next
list_print(head)
