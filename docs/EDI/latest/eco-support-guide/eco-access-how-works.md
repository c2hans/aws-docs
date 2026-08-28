---
source_url: https://docs.aws.amazon.com/EDI/latest/eco-support-guide/eco-access-how-works.html
---

# EDI customer account access
<a name="eco-access-how-works"></a>

**Important**
During the EDI account onboarding and deployment, ECO requests root user permission.

When you first create an AWS account, you begin with one sign-in identity that has complete access to all AWS services and resources in the account. This identity is called the AWS account *root user* and is accessed by signing in with the email address and password that you used to create the account.

**Important**
We strongly recommend that you don't use the root user for your everyday tasks. Safeguard your root user credentials and use them to perform the tasks that only the root user can perform. For the complete list of tasks that require you to sign in as the root user, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*.

ECO uses a predefined access model to access your EDI account. For more information, see [How AMS accesses your account](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-access-operator.html).

For more information about ECO customer account access, see [Why and when AMS accesses your account](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/access-justification.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Energy Data Insights on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query EDI` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
