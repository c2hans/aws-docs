---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/sam-delete.html
---

# Deleting an AWS serverless application by using the AWS Toolkit for JetBrains
<a name="sam-delete"></a>

Before deleting an AWS serverless application, you must first deploy it.

1. Open AWS Explorer, if it isn't already open. If you need to switch to a different AWS Region that contains the serverless application, do that now.

1. Expand **CloudFormation**.

1. Right-click the name of the AWS CloudFormation stack that contains the serverless application you want to delete, and then choose **Delete CloudFormation Stack**.
![Choosing to delete the AWS CloudFormation stack for an AWS serverless application starting from AWS Explorer](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/sam-delete.png)

1. Enter the stack's name to confirm the deletion, and then choose **OK**. If the stack deletion succeeds, the AWS Toolkit for JetBrains removes the stack name from the **CloudFormation** list in **AWS Explorer**. If the stack deletion fails, you can try to determine why by viewing event logs for the stack.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
