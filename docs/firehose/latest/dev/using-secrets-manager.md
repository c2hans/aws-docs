---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/using-secrets-manager.html
---

# Authenticate with AWS Secrets Manager in Amazon Data Firehose
<a name="using-secrets-manager"></a>

Amazon Data Firehose integrates with AWS Secrets Manager to provide secure access to your secrets and automate credential rotation. This integration allows Firehose to retrieve a secret from Secrets Manager at runtime to connect to previously mentioned streaming destinations and deliver your data streams. With this, your secrets are not visible in plain text during stream creation workflow either in AWS Management Console or API parameters. It provides a secure practice to manage your secrets and relieves you from complex credential management activities such as setting up custom Lambda functions to manage password rotations.

For more information, see the [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide).

**Topics**
+ [Understand secrets](secrets-manager-whats-secret.md)
+ [Create a secret](secrets-manager-create.md)
+ [Use the secret](secrets-manager-how.md)
+ [Rotate the secret](secrets-manager-rotate.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
