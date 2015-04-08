class Graph:
	def __init__(self):
		self.vertexes = {}

	def insert(self, vertex):
		self.vertexes[vertex] = set()

	def remove(self, vertex):
		del self.vertexes[vertex]

	def connect(self, vertex1, vertex2):
		if vertex1 in self.vertexes and vertex2 in self.vertexes:
			self.vertexes[vertex1].add(vertex2)
			self.vertexes[vertex2].add(vertex1)
		else:	
			raise Exception("vertex doesn't exist")
	
	def disconnect(self, vertex1, vertex2):
		self.vertexes[vertex1].discard(vertex2)
		self.vertexes[vertex2].discard(vertex1)

	def order(self):
		return len(self.vertexes)

	def vertexes(self):
		return self.vertexes.keys()

	def a_vertex(self):
		return next(iter(self.vertexes.keys()))

	def adjacents(self, vertex):
		if vertex in self.vertexes:
			return self.vertexes[vertex]
		else:
			raise Exception("vertex doesn't exist")
	
	def degree(self, vertex):
		return len(self.adjacents(vertex))

	def is_regular(self):
		degree = self.order(self.a_vertex())
		for vertex in self.vertex:
			if self.order(vertex) != degree:
				return False
		else:
			return True

	def is_full(self):
		vertexes = self.vertexes
		order = self.order
		for vertex in vertexes:
			if self.degree(vertex) == (order - 1):
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
		return len(self.vertexes) == len(self.transitive_closure(self.a_vertex()))

	def is_tree(self):
		def _is_tree_(actual_vertex, visited):
			for vertex in self.adjacents(actual_vertex):
				if vertex in visited:
					return False
				visited.add(vertex)
				_is_tree_(vertex, visited)
			return True

		
