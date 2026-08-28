---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/neo-supported-devices-edge-frameworks.html
---

# Supported Frameworks
<a name="neo-supported-devices-edge-frameworks"></a>

Amazon SageMaker Neo supports the following frameworks.

| Framework | Framework Version | Model Version | Models | Model Formats (packaged in \*.tar.gz) | Toolkits |
| --- | --- | --- | --- | --- | --- |
| MXNet | 1.8 | Supports 1.8 or earlier | Image Classification, Object Detection, Semantic Segmentation, Pose Estimation, Activity Recognition | One symbol file (.json) and one parameter file (.params) | GluonCV v0.8.0 |
| ONNX | 1.7 | Supports 1.7 or earlier | Image Classification, SVM | One model file (.onnx) |  |
| Keras | 2.2 | Supports 2.2 or earlier | Image Classification | One model definition file (.h5) |  |
| PyTorch | 1.7, 1.8 | Supports 1.7, 1.8 or earlier | Image Classification, Object Detection | One model definition file (.pth) |  |
| TensorFlow | 1.15, 2.4, 2.5 (only for ml.inf1.\* instances) | Supports 1.15, 2.4, 2.5 (only for ml.inf1.\* instances) or earlier | Image Classification, Object Detection | \*For saved models, one .pb or one .pbtxt file and a variables directory that contains variables \*For frozen models, only one .pb or .pbtxt file |  |
| TensorFlow-Lite | 1.15 | Supports 1.15 or earlier | Image Classification, Object Detection | One model definition flatbuffer file (.tflite) |  |
| XGBoost | 1.3 | Supports 1.3 or earlier | Decision Trees | One XGBoost model file (.model) where the number of nodes in a tree is less than 2^31 |  |
| DARKNET |  |  | Image Classification, Object Detection (Yolo model is not supported) | One config (.cfg) file and one weights (.weights) file |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
