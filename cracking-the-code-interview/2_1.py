'''
David Dalisay
Problem 2.1 - Remove duplicates from a linked list.
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class LinkedList:
	def __init__(self, node_data):
		self.head = Node(node_data[0])
		self.curr = self.head.prev
		self.curr_count = 0
		prev = self.head
		for n in range(1,len(node_data)):
			data = node_data[n]
			n = Node(data)
			n.prev = prev
			n.prev.next = n
			prev = n		
	def next(self):
		if self.curr_count == 0:
			self.curr_count += 1
			return self.head
		self.curr_count += 1
		return self.curr.next		
def print_ll(l):
	curr = l.head
	while curr:
		print(curr.data)
		curr = curr.next

def print_h(h):
	curr = h
	while curr:
		print(curr.data)
		curr = curr.next

# Solution 1: Use a hash set.
def delete_dups_hash(l):
	from collections import defaultdict
	node_hash = defaultdict(lambda: False)
	while l.next():
		if node_hash[curr]:
			curr.prev.next = curr.next
			curr.next.prev = curr.prev
		node_hash[curr] = True
		curr = curr.next	
	return head	
l = LinkedList([1,2,3,4,5,3,2])
h = delete_dups_hash(l.head)
print_h(h)
