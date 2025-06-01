class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def show(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        print("Linked List:", end=" ")
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

    def delete_at(self, pos):
        if pos <= 0:
            print("Error: Position must be a positive integer.")
            return
        if not self.head:
            print("Error: List is empty.")
            return
        if pos == 1:
            deleted = self.head.value
            self.head = self.head.next
            print(f"Deleted node at position 1 with value {deleted}.")
            return
        curr = self.head
        for _ in range(pos - 2):
            if not curr.next:
                print("Error: Position out of range.")
                return
            curr = curr.next
        if not curr.next:
            print("Error: Position out of range.")
            return
        deleted = curr.next.value
        curr.next = curr.next.next
        print(f"Deleted node at position {pos} with value {deleted}.")

if __name__ == "__main__":
    ll = LinkedList()
    for val in [10, 20, 30, 40]:
        ll.add(val)

    print("\nInitial list:")
    ll.show()

    print("\nDelete node at position 3:")
    ll.delete_at(3)
    ll.show()

    print("\nDelete node at position 10:")
    ll.delete_at(10)

    print("\nDelete node at position 1:")
    ll.delete_at(1)
    ll.show()

    print("\nDelete remaining nodes:")
    ll.delete_at(1)
    ll.delete_at(1)
    ll.show()

    print("\nDelete from empty list:")
    ll.delete_at(1)
