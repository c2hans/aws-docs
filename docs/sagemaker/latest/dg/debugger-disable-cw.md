---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-disable-cw.html
---

# Disable the CloudWatch Events rule to stop using the automated training job termination
<a name="debugger-disable-cw"></a>

**Note**
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md).

If you want to disable the automated training job termination, you need to disable the CloudWatch Events rule. In the Lambda **Designer** panel, choose the **EventBridge (CloudWatch Events)** block linked to the Lambda function. This shows an **EventBridge** panel below the **Designer** panel (for example, see the previous screen shot). Select the check box next to **EventBridge (CloudWatch Events): debugger-cw-event-rule**, and then choose **Disable**. If you want to use the automated termination functionality later, you can enable the CloudWatch Events rule again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
