import copy
import peak_ir

class Backend:
    def __init__(self, ir : peak_ir.Ir):
        self._ir = copy.deepcopy(ir)

    def generate(self):
        raise NotImplementedError("Can not call generate() on abstract class "
                                  "Backend")