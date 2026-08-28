---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/flow-cross-account-lambda.html
---

# Invoke an AWS Lambda function from an Amazon Bedrock flow in a different AWS account
<a name="flow-cross-account-lambda"></a>

An Amazon Bedrock flow can invoke a AWS Lambda function that is in a different AWS account from the flow. Use the following procedure to configure the Lambda function (*Account A*) and the flow (*Account B*).

**To configure a flow flow to call a Lambda function in a different AWS account**

1. In Account A (Lambda function), add a resource-based policy to the Lambda function, using the Flow Execution Role from Account B as the principal. For more information, see [Granting Lambda function access to other accounts](https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-cross-account.html) in the *AWS Lambda* documentation.

1. In Account B (Amazon Bedrock flow), add permission for the [invoke](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html) operation to the flow execution role for the Lambda function ARN that you are using. For more information, see [Update permissions for a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-permissions.html) in the *AWS Identity and Access Management* documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
