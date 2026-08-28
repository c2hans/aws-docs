---
source_url: https://docs.aws.amazon.com/machine-learning/latest/dg/about-batch-predictions.html
---

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Batch Predictions
<a name="about-batch-predictions"></a>

Batch prediction is useful when you want to generate predictions for a set of observations all at once, and then take action on a certain percentage or number of the observations. Typically, you do not have a low latency requirement for such an application. For example, when you want to decide which customers to target as part of an advertisement campaign for a product, you will get prediction scores for all customers, sort your model’s predictions to identify which customers are most likely to purchase, and then target maybe the top 5% customers that are most likely to purchase.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Machine Learning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
