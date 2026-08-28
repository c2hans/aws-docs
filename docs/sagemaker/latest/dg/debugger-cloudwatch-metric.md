---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-cloudwatch-metric.html
---

# Access CloudWatch logs for Debugger rules and training jobs
<a name="debugger-cloudwatch-metric"></a>

**Note**
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md).

You can use the training and Debugger rule job status in the CloudWatch logs to take further actions when there are training issues. The following procedure shows how to access the related CloudWatch logs. For more information about monitoring training jobs using CloudWatch, see [Monitor Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-overview.html).

**To access training job logs and Debugger rule job logs**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation pane under the **Log** node, choose **Log Groups**.

1. In the log groups list, do the following:
   + Choose **/aws/sagemaker/TrainingJobs** for training job logs.
   + Choose **/aws/sagemaker/ProcessingJobs** for Debugger rule job logs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
