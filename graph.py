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

