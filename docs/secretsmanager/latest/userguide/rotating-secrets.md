---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html
---

# Rotate AWS Secrets Manager secrets
<a name="rotating-secrets"></a>

*Rotation* is the process of periodically updating a secret. When you rotate a secret, you update the credentials in both the secret and the database or service. In Secrets Manager, you can set up automatic rotation for your secrets. There are two forms of rotation:
+ [Managed rotation](rotate-secrets_managed.md) – For most [managed secrets](service-linked-secrets.md), you use managed rotation, where the service configures and manages rotation for you. Managed rotation doesn't use a Lambda function.
+ [Rotate Secrets Manager managed external secrets](rotate-secrets_external.md) – For secrets held by Secrets Manager partners, you use managed external secrets rotation to update the secret on the partner's system. This doesn't require a Lambda function.
+ [Rotation by Lambda function](rotate-secrets_lambda.md) – For other types of secrets, Secrets Manager rotation uses a Lambda function to update the secret and the database or service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
