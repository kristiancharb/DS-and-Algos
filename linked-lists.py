class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def add(self, data):
        cursor = self
        while cursor.next != None:
            cursor = cursor.next
        new_node = Node()
        new_node.data = data
        cursor.next = new_node
        return self

    def remove_dups(self):
        cursor = self
        vals = set()
        while cursor and cursor.next:
            vals.add(cursor.data)
            if cursor.next.data in vals:
                cursor.next = cursor.next.next 
            cursor = cursor.next
        return self

    def remove_dups2(self):
        cursor = self
        while cursor and cursor.next:
            if cursor.next.data == cursor.data:
                cursor.next = cursor.next.next
            else:
                curr = cursor.next
                while curr and curr.next:
                    if curr.next.data == cursor.data:
                        curr.next = curr.next.next
                    curr = curr.next

            cursor = cursor.next
        return self

    def get_kth_to_last(self, k):
        def get_helper(head, k, i):
            if head == None:
                return head, 0

            node, index = get_helper(head.next, k, i)
            index += 1
            if index == k:
                return head, index
            else:
                return node, index

        node, _ = get_helper(self, k, 0)
        return node

    def partition(self, n):
        left, right = Node(), Node()

        cursor = self
        while cursor:
            if cursor.data < n:
                if left.data == None:
                    left.data = cursor.data
                else:
                    left.add(cursor.data)
            else:
                if right.data == None:
                    right.data = cursor.data
                else:
                    right.add(cursor.data)
            cursor = cursor.next

        cursor = left
        while cursor.next:
            cursor = cursor.next
        cursor.next = right
        return left

    def is_palindrome(self):
        stack = []
        fast = self
        slow = self
        while fast and fast.next:
            stack.append(slow.data)
            fast = fast.next.next
            slow = slow.next

        print(stack)
        if stack[-1] != slow.data:
            slow = slow.next
        
        while slow:
            if slow.data != stack.pop():
                return False
            slow = slow.next

        return len(stack) == 0

    def __str__(self):
        cursor = self
        s = ''
        while cursor.next:
            s += str(cursor.data) + '-->'
            cursor = cursor.next
        s += str(cursor.data)
        return s

if __name__ == "__main__":
    head = Node()
    head.data = 1
    head.add(2).add(3).add(4).add(4).add(3).add(2).add(1)
    print(head.is_palindrome())