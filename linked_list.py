class Node(object):
    """create Node objects"""

    def __init__(self,init_data, next=None):
        """set attributes of Node object """
        
        self.data = init_data
        self.next = next

    def get_data(self):
        """Return Node's data value"""
        
        return self.data

    def get_next(self):
        """Return Node's next pointee"""

        return self.next

    def set_data(self, new_data):
        """Set data value"""

        self.data = new_data

    def set_next(self, new_next):
        """Set new next pointer"""
        self.next = new_next

class Linked_lst(object):
    """initialize Linked List"""

    def __init__(self):
        self.head = None
        self.tail = None

    def is_Empty(self):
        return self.head == None

    def add_node(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def ll_length(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def delete_node(self, item):
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        if previous == None:
            self.head = current.get_data()

        else:
            previous.set_next(current.get_next())
