---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/text-classification-tensorflow-HowItWorks.html
---

# How Text Classification - TensorFlow Works
<a name="text-classification-tensorflow-HowItWorks"></a>

The Text Classification - TensorFlow algorithm takes text as classifies it into one of the output class labels. Deep learning networks such as [BERT](https://arxiv.org/pdf/1810.04805.pdf) are highly accurate for text classification. There are also deep learning networks that are trained on large text datasets, such as TextNet, which has more than 11 million texts with about 11,000 categories. After a network is trained with TextNet data, you can then fine-tune the network on a dataset with a particular focus to perform more specific text classification tasks. The Amazon SageMaker AI Text Classification - TensorFlow algorithm supports transfer learning on many pretrained models that are available in the TensorFlow Hub.

According to the number of class labels in your training data, a text classification layer is attached to the pretrained TensorFlow model of your choice. The classification layer consists of a dropout layer, a dense layer, and a fully connected layer with 2-norm regularization, and is initialized with random weights. You can change the hyperparameter values for the dropout rate of the dropout layer and the L2 regularization factor for the dense layer.

You can fine-tune either the entire network (including the pretrained model) or only the top classification layer on new training data. With this method of transfer learning, training with smaller datasets is possible.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
