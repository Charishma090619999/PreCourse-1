class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=None
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        Space: O(1)
        """
        if not self.head:
            self.head=ListNode(data)
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next= ListNode(data)

        
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        Space : O(1)
        """
        curr = self.head
        while curr:
            if curr.data==key:
                return curr.data
        if not curr:
            return None
        
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        Space O(1).
        """
        curr=self.head
        while curr.next:
            if curr.next.data == key:
                curr.next=curr.next.next
            curr=curr.next
            




