---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awssecretsmanager.html
---

# Data retrieval APIs for AWS Secrets Manager
<a name="awssecretsmanager"></a>

AWS Secrets Manager provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="secretsmanager-BatchGetSecretValue"></a>[BatchGetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_BatchGetSecretValue.html) | Retrieve and decrypt a list of secrets | Read |
| <a name="secretsmanager-DescribeSecret"></a>[DescribeSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html) | Retrieve the metadata about a secret, but not the encrypted data | Read |
| <a name="secretsmanager-GetRandomPassword"></a>[GetRandomPassword](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html) | Generate a random string for use in password creation | Read |
| <a name="secretsmanager-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetResourcePolicy.html) | Get the resource policy attached to a secret | Read |
| <a name="secretsmanager-GetSecretValue"></a>[GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) | Retrieve and decrypt the encrypted data | Read |
| <a name="secretsmanager-ListSecretVersionIds"></a>[ListSecretVersionIds](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecretVersionIds.html) | List the available versions of a secret | Read |
| <a name="secretsmanager-ListSecrets"></a>[ListSecrets](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecrets.html) | List the available secrets | List |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
