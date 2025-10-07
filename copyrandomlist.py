class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if head is None:
            return None
        cur = head
        while cur: # copy nodes
            node = Node(cur.val, cur.next)
            cur.next = node
            cur = node.next

        cur = head
        while cur: # copy random pointers
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        ans = head.next
        cur = head
        while cur: # cut into 2 lists
            nxt = cur.next
            if nxt:
                cur.next = nxt.next
            cur = nxt
        return ans


class Solution: # with a map
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        node_map = {}

        # Create the copy nodes without next and random connections
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next

        # Assign next and random connections for the copy nodes
        current = head
        while current:
            copy_node = node_map[current]
            copy_node.next = node_map.get(current.next)
            copy_node.random = node_map.get(current.random)
            current = current.next

        return node_map[head]
