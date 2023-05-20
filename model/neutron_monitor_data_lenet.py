# This Python file uses the following encoding: utf-8
from torch import nn
from torch.nn import functional as F


class NeutronMonitorDataLeNet(nn.Module):
    def __init__(self):
        super(NeutronMonitorDataLeNet, self).__init__()
        self.feature_extractor = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3),
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3),
            nn.Flatten(0)
        )
        self.classifier = nn.Sequential(
            nn.Linear(in_features=63600, out_features=120),
            nn.ReLU(),
            nn.Linear(in_features=120, out_features=84),
            nn.ReLU(),
            nn.Linear(in_features=84, out_features=3)
        )

    def forward(self, x):
        x = self.feature_extractor(x)
        # print(x.shape)
        logits = self.classifier(x)
        probs = F.softmax(logits, dim=0)
        return logits, probs
