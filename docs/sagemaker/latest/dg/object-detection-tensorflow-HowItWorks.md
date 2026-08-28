---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/object-detection-tensorflow-HowItWorks.html
---

# How Object Detection - TensorFlow Works
<a name="object-detection-tensorflow-HowItWorks"></a>

The Object Detection - TensorFlow algorithm takes an image as input and predicts bounding boxes and object labels. Various deep learning networks such as MobileNet, ResNet, Inception, and EfficientNet are highly accurate for object detection. There are also deep learning networks that are trained on large image datasets, such as Common Objects in Context (COCO), which has 328,000 images. After a network is trained with COCO data, you can then fine-tune the network on a dataset with a particular focus to perform more specific object detection tasks. The Amazon SageMaker AI Object Detection - TensorFlow algorithm supports transfer learning on many pretrained models that are available in the TensorFlow Model Garden.

According to the number of class labels in your training data, an object detection layer is attached to the pretrained TensorFlow model of your choice. You can then fine-tune either the entire network (including the pretrained model) or only the top classification layer on new training data. With this method of transfer learning, training with smaller datasets is possible.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
