class Graph:
	def __init__(self):
		self._vertexes = {}

	def insert(self, vertex):
		self._vertexes[vertex] = set()

	def remove(self, vertex):
		del self._vertexes[vertex]

	def connect(self, vertex1, vertex2):
		if vertex1 in self._vertexes and vertex2 in self._vertexes:
			self._vertexes[vertex1].add(vertex2)
			self._vertexes[vertex2].add(vertex1)
		else:	
			raise Exception("vertex doesn't exist")
	
	def disconnect(self, vertex1, vertex2):
		self._vertexes[vertex1].discard(vertex2)
		self._vertexes[vertex2].discard(vertex1)

	def order(self):
		return len(self._vertexes)

	def vertexes(self):
		return self._vertexes.keys()

	def a_vertex(self):
		return next(iter(self._vertexes.keys()))

	def adjacents(self, vertex):
		if vertex in self._vertexes:
			return self._vertexes[vertex]
		else:
			raise Exception("vertex doesn't exist")
	
	def degree(self, vertex):
		return len(self.adjacents(vertex))

	def is_regular(self):
		degree = self.degree(self.a_vertex())
		for vertex in self._vertexes:
			if self.degree(vertex) != degree:
				return False
		else:
			return True

	def is_full(self):
		vertexes = self._vertexes
		order = self.order()
		for vertex in vertexes:
			if not self.degree(vertex) == (order - 1):
				return False
		else:
			return True
	def transitive_closure(self, vertex): 
		def _transitive_closure_(vertex, visited):
			visited.add(vertex)
			for vertex_aux in self.adjacents(vertex):
				if not vertex_aux in visited:
					_transitive_closure_(vertex_aux, visited)
			return visited
		return _transitive_closure_(vertex, set())

	def is_connected(self):	
		return len(self._vertexes) == len(self.transitive_closure(self.a_vertex()))

	def is_tree(self):
		def _is_tree_(actual_vertex, visited):
			for vertex in self.adjacents(actual_vertex):
				if vertex in visited:
					return False
				visited.add(vertex)
				if not _is_tree_(vertex, visited):
					return False
			return True

		return self.is_connected() and _is_tree_(self.a_vertex(), set())		
