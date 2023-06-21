# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def get_node_by_index(node, index):
        while index:
                node = node.next
                index -= 1
        return node

def solution(head, idx):
    if idx == 0:
            new_head = head.next
            del(head)
            return new_head
    previous_node = get_node_by_index(node, idx-1)
    node = previous_node.next
    previous_node.next = node.next
    del(node)
    return head

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3

if __name__ == '__main__':
    test()