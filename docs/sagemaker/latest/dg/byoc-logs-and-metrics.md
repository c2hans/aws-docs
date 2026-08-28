---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/byoc-logs-and-metrics.html
---

# How Amazon SageMaker Processing Provides Logs and Metrics for Your Processing Container
<a name="byoc-logs-and-metrics"></a>

When your processing container writes to `stdout` or `stderr`, Amazon SageMaker Processing saves the output from each processing container and puts it in Amazon CloudWatch logs. For information about logging, see [CloudWatch Logs for Amazon SageMaker AI](logging-cloudwatch.md).

Amazon SageMaker Processing also provides CloudWatch metrics for each instance running your processing container. For information about metrics, see [Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
