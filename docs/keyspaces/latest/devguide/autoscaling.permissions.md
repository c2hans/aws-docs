---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.permissions.html
---

# Configure permissions for Amazon Keyspaces automatic scaling
<a name="autoscaling.permissions"></a>

To get started, confirm that the principal has the appropriate permissions to create and manage automatic scaling settings. In AWS Identity and Access Management (IAM), the AWS managed policy `AmazonKeyspacesFullAccess` is required to manage Amazon Keyspaces scaling policies.

**Important**
 `application-autoscaling:*` permissions are required to disable automatic scaling on a table. You must turn off auto scaling for a table before you can delete it.

To set up an IAM user or role for Amazon Keyspaces console access and Amazon Keyspaces automatic scaling, add the following policy.

**To attach the `AmazonKeyspacesFullAccess` policy**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. On the IAM console dashboard, choose **Users**, and then choose your IAM user or role from the list.

1. On the **Summary** page, choose **Add permissions**.

1. Choose **Attach existing policies directly**.

1. From the list of policies, choose **AmazonKeyspacesFullAccess**, and then choose **Next: Review**.

1. Choose **Add permissions**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
