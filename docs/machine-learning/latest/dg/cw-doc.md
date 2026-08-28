---
source_url: https://docs.aws.amazon.com/machine-learning/latest/dg/cw-doc.html
---

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Monitoring Amazon ML with Amazon CloudWatch Metrics
<a name="cw-doc"></a>

Amazon ML automatically sends metrics to Amazon CloudWatch so that you can gather and analyze usage statistics for your ML models. For example, to keep track of batch and real-time predictions, you can monitor the PredictCount metric according to the RequestMode dimension. The metrics are automatically collected and sent to Amazon CloudWatch every five minutes. You can monitor these metrics by using the Amazon CloudWatch console, AWS CLI, or AWS SDKs.

There is no charge for the Amazon ML metrics that are reported through CloudWatch. If you set alarms on the metrics, you will be billed at standard [CloudWatch rates](https://aws.amazon.com/cloudwatch/pricing/).

For more information, see the Amazon ML list of metrics in [Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html) in the Amazon CloudWatch Developer Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Machine Learning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
