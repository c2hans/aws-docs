---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/create-execution-role.html
---

# Tutorial: Create the IAM execution role
<a name="create-execution-role"></a>

If your account doesn't already have an IAM execution role, use the following steps to create the role.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. For **Trusted entity type**, choose** AWS service**.

1. For **Service or use case**, choose **Elastic Container Service**. Then choose **Elastic Container Service Task** again.

1. Choose **Next**.

1. For **Permissions policies**, search for **AmazonECSTaskExecutionRolePolicy**.

1. Choose the check box to the left of the **AmazonECSTaskExecutionRolePolicy** policy, and then choose **Next**.

1. For **Role Name**, enter `ecsTaskExecutionRole` and then choose **Create role**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
