import torch
import torch.nn as nn

class CrimeMapNetwork(nn.Module):

  def __init__(self, num_classes: int=1000) -> None:
    super(CrimeMapNetwork, self).__init__()
    self.features = nn.Sequential(
        nn.Conv2d(3, 16, (5, 5)),
        nn.ReLU(),
        nn.MaxPool2d(3),
        nn.Conv2d(16, 48, (5, 5)),
        nn.ReLU(),
        nn.MaxPool2d(2)
    )
    self.classifier = nn.Sequential(
        nn.Linear(48 * 8 * 8, 256),
        nn.ReLU(),
        nn.Linear(256, num_classes),
        nn.ReLU(),
        nn.Softmax(dim=1)
    )

  def forward(self, x: torch.Tensor) -> torch.Tensor:
    x = self.features(x)
    x = torch.flatten(x, 1)
    x = self.classifier(x)
    
    return x
