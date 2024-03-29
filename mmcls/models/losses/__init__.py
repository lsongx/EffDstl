from torch.nn.modules.loss import *   # noqa: F401,F403
from .cross_entropy_smooth_loss import CrossEntropySmoothLoss
from .kl_loss import KLLoss
from .wsl_loss import WSLLoss