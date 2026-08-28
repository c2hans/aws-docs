---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/create-flow-logs-role.html
---

# Create or update an IAM role for AWS Transit Gateway Flow Logs
<a name="create-flow-logs-role"></a>

You can update an existing role or use the following procedure to create a new role for use with flow logs using the AWS Identity and Access Management console.

**To create an IAM role for flow logs**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, **Create role**.

1. For **Select type of trusted entity**, choose **AWS service**. For **Use case**, choose **EC2**. Choose **Next**.

1. On the **Add permissions** page, choose **Next: Tags** and optionally add tags. Choose **Next**.

1. On the Name, review, and create page enter a name for your role and optionally provide a **Description**. Choose **Create role**.

1. Choose the name of your role. For **Add permissions**, choose **Create inline policy**, and then choose the **JSON** tab.

1. Copy the first policy from [IAM roles for publishing flow logs to CloudWatch Logs](flow-logs-cwl.md#flow-logs-iam) and paste it in the window. Choose **Review policy**.

1. Enter a name for your policy, and choose **Create policy**.

1. Select the name of your role. For **Trust relationships**, choose **Edit trust relationship**. In the existing policy document, change the service from `ec2.amazonaws.com` to `vpc-flow-logs.amazonaws.com`. Choose **Update Trust Policy**.

1. On the **Summary** page, note the ARN for your role. You need this ARN when you create your flow log.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
