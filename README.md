
# Efficient Distillation

## How to use

1. Install the following packages
    - python >= 3.7.0
    - pytorch >= 1.2.0
    - CUDA >= 10.0
    - nvidia-dali-cuda100 >= 0.23.0
    - mmcv >= 1.0.5
    - mxnet >= 1.6.0 (only used for preparing the dataset)
2. Prepare ImageNet data as `.rec` following ["Create a Dataset Using RecordIO"](https://mxnet.apache.org/api/faq/recordio).
    
## Results
Our pre-trained models and corresponding training logs can be downloaded at [OneDrive](https://1drv.ms/u/s!AqzBcxT1FhwG0R7Ibzdu3fI1CLi6?e=W10QWS).

| Model | Top-1(%) | Training Time (GPU Hours) |
|:---:|:---:|:---:|
| MobileNet V3-Small 0.75 | 67.34 | 93.0 |
| ResNet 18 | 74.07 | 97.7 |
| MobileNet V2 | 74.45 | 130.1 |
| ResNet 18d | 74.98 | 114.0 |
| SKResNet 18 | 75.12 | 127.3 |
| MobileNet V1 | 75.49 | 111.5 |
| ResNet 34 | 77.06 | 160.8 |
| ResNet 34d | 77.62 | 173.4 |

## Acknowledgement
The implementation is based on [MMClassification](https://github.com/open-mmlab/mmclassification) and [dali-pytorch](https://github.com/JaminFong/dali-pytorch).
