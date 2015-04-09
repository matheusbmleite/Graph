import unittest
from graph import Graph

class GraphTestCase(unittest.TestCase):
	def setUp(self):
		self.g = Graph()

	def test_insert_vertex(self):
		for i in range(1, 7):
			self.g.insert(i)
		
		vertexes = [1, 2, 3, 4, 5, 6] 
		self.assertEqual(vertexes, list(self.g._vertexes.keys())) 

	def test_remove_vertex(self):
		for i in range(1,7):
			self.g.insert(i)
		self.g.remove(1)
		vertexes = [2, 3, 4, 5, 6]
		self.assertEqual(vertexes, list(self.g._vertexes.keys()))

	def test_connect(self):
		self.g.insert(1)
		self.g.insert(2)
		self.g.connect(1,2)
		adjacents = {2}
		self.assertEqual(adjacents, self.g._vertexes[1])
		adjacents = {1}
		self.assertEqual(adjacents, self.g._vertexes[2])
	
	def test_disconnect(self):
		self.g.insert(1)
		self.g.insert(2)
		self.g.connect(1,2)
		self.g.disconnect(1,2)
		adjacents = set()
		self.assertEqual(adjacents, self.g._vertexes[1])
		self.assertEqual(adjacents, self.g._vertexes[2])

	def test_order(self):
		for i in range (1,100):
			self.g.insert(i)
		self.assertEqual(99, self.g.order())
	
	def test_vertixes(self):
		for i in range (1,5):
                        self.g.insert(i)
		vertexes = {1, 2, 3, 4}
		self.assertEqual(vertexes, self.g.vertexes())
		
	def test_a_vertex(self):
		for i in range (1,5):
			self.g.insert(i)
		self.assertTrue(self.g.a_vertex() == 1 or 2 or 3 or 4)
	
	def test_adjacents(self):
		for i in range (1,5):
			self.g.insert(i)
		self.g.connect(1,2)
		self.g.connect(1,3)
		self.g.connect(1,4)
		adjacents = {2, 3, 4}
		self.assertEqual(adjacents, self.g.adjacents(1))
	
	def test_degree(self):
		for i in range (1,5):
			self.g.insert(i)
		self.g.connect(1,2)
		self.g.connect(1,3)
		self.g.connect(1,4)
		degree = 3
		self.assertEqual(degree, self.g.degree(1))
		degree = 1
		self.assertEqual(degree, self.g.degree(2))
		self.assertEqual(degree, self.g.degree(3))

	def test_is_regular(self):
		for i in range(1,5):
			self.g.insert(i)
		self.g.connect(1,2)
		self.g.connect(1,3)
		self.g.connect(2,3)
		self.g.connect(1,4)
		self.g.connect(2,4)
		self.g.connect(3,4)
		self.assertTrue(self.g.is_regular())
		self.g.disconnect(3,4)
		self.assertFalse(self.g.is_regular())

	def test_is_full(self):
		for i in range(1,5):
			self.g.insert(i)
		self.g.connect(1,2)
		self.g.connect(1,3)
		self.g.connect(2,3)
		self.g.connect(1,4)
		self.g.connect(2,4)
		self.g.connect(3,4)
		self.assertTrue(self.g.is_full())
		self.g.disconnect(3,4)
		self.assertFalse(self.g.is_full())

	def test_transitive_closure(self):
		for i in range(1,5):
			self.g.insert(i)
		self.g.connect(1,2)
		self.g.connect(1,3)
		self.g.connect(2,3)
		self.g.connect(1,4)
		self.g.connect(2,4)
		self.g.connect(3,4)
		transitive = {1,2,3,4} 
		self.assertEqual(transitive, self.g.transitive_closure(1))
		self.g.insert(5)
		self.assertEqual(transitive, self.g.transitive_closure(1))

	def test_is_connected(self):
		for i in range(1,5):
			self.g.insert(i)
		self.g.connect(1,2)
		self.g.connect(1,3)
		self.g.connect(2,3)
		self.g.connect(1,4)
		self.g.connect(2,4)
		self.g.connect(3,4)
		self.assertTrue(self.g.is_connected())
		self.g.insert(5)
		self.assertFalse(self.g.is_connected())


	def test_is_tree(self):
		for i in range(1,5):
			self.g.insert(i)
		self.g.connect(1,2)
		self.g.connect(1,3)
		self.g.connect(2,3)
		self.g.connect(1,4)
		self.g.connect(2,4)
		self.g.connect(3,4)
		self.assertFalse(self.g.is_tree())
		self.g.disconnect(2,4)
		self.g.disconnect(3,4)
		self.g.disconnect(2,3)
		self.assertTrue(self.g.is_tree())
			

if __name__ == '__main__': 
	unittest.main()
