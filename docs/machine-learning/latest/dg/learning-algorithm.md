---
source_url: https://docs.aws.amazon.com/machine-learning/latest/dg/learning-algorithm.html
---

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Learning Algorithm
<a name="learning-algorithm"></a>

The learning algorithm’s task is to learn the weights for the model. The weights describe the likelihood that the patterns that the model is learning reflect actual relationships in the data. A learning algorithm consists of a loss function and an optimization technique. The loss is the penalty that is incurred when the estimate of the target provided by the ML model does not equal the target exactly. A loss function quantifies this penalty as a single value. An optimization technique seeks to minimize the loss. In Amazon Machine Learning, we use three loss functions, one for each of the three types of prediction problems. The optimization technique used in Amazon ML is online Stochastic Gradient Descent (SGD). SGD makes sequential passes over the training data, and during each pass, updates feature weights one example at a time with the aim of approaching the optimal weights that minimize the loss.

Amazon ML uses the following learning algorithms:
+ For binary classification, Amazon ML uses logistic regression (logistic loss function \+ SGD).
+ For multiclass classification, Amazon ML uses multinomial logistic regression (multinomial logistic loss \+ SGD).
+ For regression, Amazon ML uses linear regression (squared loss function \+ SGD).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Machine Learning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
