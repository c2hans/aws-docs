---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-increase-instance-limit.html
---

# Increase Amazon EC2 Instance Limit
<a name="data-wrangler-increase-instance-limit"></a>

You might see the following error message when you're using Data Wrangler: `The following instance type is not available: ml.m5.4xlarge. Try selecting a different instance below.`

The message can indicate that you need to select a different instance type, but it can also indicate that you don't have enough Amazon EC2 instances to successfully run Data Wrangler on your workflow. You can increase the number of instances by using the following procedure.

To increase the number of instances, do the following.

1. Open the AWS Management Console.

1. In the search bar, specify **Services Quotas**.

1. Choose **Service Quotas**.

1. Choose **AWS services**.

1. In the search bar, specify **Amazon SageMaker AI**.

1. Choose **Amazon SageMaker AI**.

1. Under **Service quotas**, specify **Studio KernelGateway Apps running on {{ml.m5.4xlarge}} instance**.
**Note**
ml.m5.4xlarge is the default instance type for Data Wrangler. You can use other instance types and request quota increases for them. For more information, see [Instances](data-wrangler-data-flow.md#data-wrangler-data-flow-instances).

1. Select **Studio KernelGateway Apps running on {{ml.m5.4xlarge}} instance**.

1. Choose **Request quota increase**.

1. For **Change quota value**, specify a value greater than **Applied quota value**.

1. Choose **Request**.

If your request is approved, AWS sends a notification to the email address associated with your account. You can also check the status of your request by choosing **Quota request history** on the **Service Quotas** page. Processed requests have a **Status** of **Closed**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
