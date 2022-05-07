from collections import defaultdict
def has_cycle(head):
    
    visited = defaultdict(int)
    while head:  
        if head in visited:
            return 1
        visited[head] = 1
        head = head.next
    return 0
    
