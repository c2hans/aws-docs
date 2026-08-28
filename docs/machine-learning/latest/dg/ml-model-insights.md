---
source_url: https://docs.aws.amazon.com/machine-learning/latest/dg/ml-model-insights.html
---

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# ML Model Insights
<a name="ml-model-insights"></a>

When you evaluate an ML model, Amazon ML provides an industry-standard metric and a number of insights to review the predictive accuracy of your model. In Amazon ML, the outcome of an evaluation contains the following:
+ A prediction accuracy metric to report on the overall success of the model
+ Visualizations to help explore the accuracy of your model beyond the prediction accuracy metric
+ The ability to review the impact of setting a score threshold (only for binary classification)
+ Alerts on criteria to check the validity of the evaluation

The choice of the metric and visualization depends on the type of ML model that you are evaluating. It is important to review these visualizations to decide if your model is performing well enough to match your business requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Machine Learning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
