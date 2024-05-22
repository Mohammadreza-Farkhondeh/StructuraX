import pyfeaplusplus as fea


class Mesh:
    def __init__(self):
        self.mesh = fea.Mesh()

    def add_node(self, x, y, z):
        self.mesh.addNode(fea.Node(x, y, z))

    def add_element(self):
        self.mesh.addElement()
