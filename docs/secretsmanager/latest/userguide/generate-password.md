---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/generate-password.html
---

# Generate a password with Secrets Manager
<a name="generate-password"></a>

A common pattern for using Secrets Manager is to generate a password in Secrets Manager and then use that password in your database or service. You can do this using the following methods:
+ CloudFormation – See [Create AWS Secrets Manager secrets in AWS CloudFormation](cloudformation.md).
+ AWS CLI – See [`get-random-password`](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/get-random-password.html).
+ AWS SDKs – See [`GetRandomPassword`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
