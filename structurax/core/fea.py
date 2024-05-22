import pyfeaplusplus as fea


class FEA:
    def __init__(self):
        self.fea = fea.FEA()

    def setup_model(self, mesh):
        self.fea.setupModel(mesh.mesh)

    def analyze(self):
        self.fea.analyze()
