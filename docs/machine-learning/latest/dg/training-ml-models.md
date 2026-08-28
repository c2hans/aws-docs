---
source_url: https://docs.aws.amazon.com/machine-learning/latest/dg/training-ml-models.html
---

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Training ML Models
<a name="training-ml-models"></a>

 The process of training an ML model involves providing an ML algorithm (that is, the *learning algorithm*) with training data to learn from. The term *ML model* refers to the model artifact that is created by the training process.

 The training data must contain the correct answer, which is known as a *target* or *target attribute*. The learning algorithm finds patterns in the training data that map the input data attributes to the target (the answer that you want to predict), and it outputs an ML model that captures these patterns.

 You can use the ML model to get predictions on new data for which you do not know the target. For example, let's say that you want to train an ML model to predict if an email is spam or not spam. You would provide Amazon ML with training data that contains emails for which you know the target (that is, a label that tells whether an email is spam or not spam). Amazon ML would train an ML model by using this data, resulting in a model that attempts to predict whether new email will be spam or not spam.

 For general information about ML models and ML algorithms, see [Machine Learning Concepts](machine-learning-concepts.md).

**Topics**
+ [Types of ML Models](types-of-ml-models.md)
+ [Training Process](training-process.md)
+ [Training Parameters](training-parameters.md)
+ [create an ML model](creating-ml-model-on-the-amazon-ml-console.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Machine Learning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
