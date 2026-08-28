---
source_url: https://docs.aws.amazon.com/machine-learning/latest/dg/types-of-ml-models.html
---

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Types of ML Models
<a name="types-of-ml-models"></a>

 Amazon ML supports three types of ML models: binary classification, multiclass classification, and regression. The type of model you should choose depends on the type of target that you want to predict.

## Binary Classification Model
<a name="binary-classification-model"></a>

ML models for binary classification problems predict a binary outcome (one of two possible classes). To train binary classification models, Amazon ML uses the industry-standard learning algorithm known as logistic regression.

### Examples of Binary Classification Problems
<a name="examples-of-binary-classification-problems"></a>
+  "Is this email spam or not spam?"
+  "Will the customer buy this product?"
+  "Is this product a book or a farm animal?"
+  "Is this review written by a customer or a robot?"

## Multiclass Classification Model
<a name="multiclass-classification-model"></a>

 ML models for multiclass classification problems allow you to generate predictions for multiple classes (predict one of more than two outcomes). For training multiclass models, Amazon ML uses the industry-standard learning algorithm known as multinomial logistic regression.

### Examples of Multiclass Problems
<a name="examples-of-multiclass-problems"></a>
+  "Is this product a book, movie, or clothing?"
+  "Is this movie a romantic comedy, documentary, or thriller?"
+  "Which category of products is most interesting to this customer?"

## Regression Model
<a name="regression-model"></a>

 ML models for regression problems predict a numeric value. For training regression models, Amazon ML uses the industry-standard learning algorithm known as linear regression.

### Examples of Regression Problems
<a name="examples-of-regression-problems"></a>
+  "What will the temperature be in Seattle tomorrow?"
+  "For this product, how many units will sell?"
+  "What price will this house sell for?"

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Machine Learning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
