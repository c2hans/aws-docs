---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/create-an-iam-role.html
---

# Create IAM roles for your compute environments and container instances
<a name="create-an-iam-role"></a>

Your AWS Batch compute environments and container instances require AWS account credentials to make calls to other AWS APIs on your behalf. Create an AWS Identity and Access Management role that provides these credentials to your compute environments and container instances, then associate that role with your compute environments.

**Note**
To verify that your AWS account has the required permissions, see [Initial IAM service set up for your account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).
The AWS Batch compute environment and container instance roles are automatically created for you in the console first-run experience. So, if you intend to use the AWS Batch console, you can move ahead to the next section. If you plan to use the AWS CLI instead, complete the procedures in [Using service-linked roles for AWS Batch](using-service-linked-roles.md), [Amazon ECS instance role](instance_IAM_role.md), and [Tutorial: Create the IAM execution role](create-execution-role.md) before creating your first compute environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
