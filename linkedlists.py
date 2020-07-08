class ListNode:
    def __init__(self, value):
        self._val = value
        self._next = None

class singlyLinkedList:
	
	def __init__(self):
		self._head = None
		self._size = 0

	def __len__(self):
		return self._size
	
	def add(self, value):
		newNode = ListNode(value)
		if self._size == 0:
			self._head = newNode
		
		else:
			newNode._next = self._head
			self._head = newNode
		self._size += 1
		
	def remove(self, index):
		assert index < self._size and self._size != 0
		i = 0
		curNode = self._head
		while i < index and curNode._next is not None:
			preNode = curNode
			curNode = curNode._next
			i += 1
		preNode._next = curNode._next
		self._size -=1
	
	def display_list(self):
		curNode = self._head
		for node in self:
		    print(node._val)
	
	def __iter__(self):
		return _LinkedListIterator(self._head)

		
class _LinkedListIterator:
	def __init__(self, head):
		self._curNode = head
	
	def __iter__(self):
		return self

	def __next__(self):
	    if self._curNode is None:
	    	raise StopIteration
	    else:
	    	item = self._curNode
	    	self._curNode = self._curNode._next
	    	return item
	 
lList = singlyLinkedList()
lList.add(5)
lList.add(4)
lList.add(6)
lList.add(9)
lList.display_list()