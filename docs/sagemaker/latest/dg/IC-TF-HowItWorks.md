---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/IC-TF-HowItWorks.html
---

# How Image Classification - TensorFlow Works
<a name="IC-TF-HowItWorks"></a>

The Image Classification - TensorFlow algorithm takes an image as input and classifies it into one of the output class labels. Various deep learning networks such as MobileNet, ResNet, Inception, and EfficientNet are highly accurate for image classification. There are also deep learning networks that are trained on large image datasets, such as ImageNet, which has over 11 million images and almost 11,000 classes. After a network is trained with ImageNet data, you can then fine-tune the network on a dataset with a particular focus to perform more specific classification tasks. The Amazon SageMaker Image Classification - TensorFlow algorithm supports transfer learning on many pretrained models that are available in the TensorFlow Hub.

According to the number of class labels in your training data, a classification layer is attached to the pretrained TensorFlow Hub model of your choice. The classification layer consists of a dropout layer, a dense layer, and a fully-connected layer with 2-norm regularizer that is initialized with random weights. The model has hyperparameters for the dropout rate of the dropout layer and the L2 regularization factor for the dense layer. You can then fine-tune either the entire network (including the pretrained model) or only the top classification layer on new training data. With this method of transfer learning, training with smaller datasets is possible.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
