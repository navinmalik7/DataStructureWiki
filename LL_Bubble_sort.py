class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE BUBBLE_SORT METHOD HERE #
    #                               #
    #                               #
    #                               #
    #                               #
    #################################



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)


print("Linked List Before Sort:")
my_linked_list.print_list()

def bubble_sort(my_linked_list):
    for i in range(len(my_linked_list) - 1, 0, -1):
        for j in range (i):
            if my_linked_list[j] > my_linked_list[j+1]:
                temp = my_linked_list[j]
                my_linked_list[j] = my_linked_list[j+1]
                my_linked_list[j+1] = temp
    return my_linked_list

bubble_sort(my_linked_list)

#my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""