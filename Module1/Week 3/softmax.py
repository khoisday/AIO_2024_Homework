from torch import Tensor
from torch.nn import Module
import numpy as np

class Softmax(Module):
    def __init__(self, data=None):
        super(Softmax, self).__init__()
        if data is not None:
            self.data = self.forward(data)
        else:
            self.data = None

    def __str__(self):
        return f"{self.data}"

    def forward(self, x):
        """
        Compute the softmax of vector x
        :param x: torch.Tensor
        :return: torch.Tensor
        """
        exp_x = np.exp(x)
        return exp_x / exp_x.sum()


class softmax_stable(Module):
    def __init__(self, data=None):
        super(softmax_stable, self).__init__()
        if data is not None:
            self.data = self.forward(data)
        else:
            self.data = None

    def __str__(self):
        return f"{self.data}"

    def forward(self, x):
        """
        Compute the softmax of vector x
        :param x: torch.Tensor
        :return: torch.Tensor
        """
        c = max(x)
        exp_x = np.exp(x - c)
        return exp_x / exp_x.sum()


if __name__ == "__main__":
    # Examples 1
    data = Tensor([1, 2, 3])
    output = softmax_stable(data)
    print(output)