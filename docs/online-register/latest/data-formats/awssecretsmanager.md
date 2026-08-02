---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awssecretsmanager.html
---

# Data retrieval APIs for AWS Secrets Manager
<a name="awssecretsmanager"></a>

AWS Secrets Manager provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="secretsmanager-BatchGetSecretValue"></a>[https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_BatchGetSecretValue.html](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_BatchGetSecretValue.html) | Retrieve and decrypt a list of secrets | Read |
| <a name="secretsmanager-DescribeSecret"></a>[https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html) | Retrieve the metadata about a secret, but not the encrypted data | Read |
| <a name="secretsmanager-GetRandomPassword"></a>[https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html) | Generate a random string for use in password creation | Read |
| <a name="secretsmanager-GetResourcePolicy"></a>[https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetResourcePolicy.html](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetResourcePolicy.html) | Get the resource policy attached to a secret | Read |
| <a name="secretsmanager-GetSecretValue"></a>[https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) | Retrieve and decrypt the encrypted data | Read |
| <a name="secretsmanager-ListSecretVersionIds"></a>[https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecretVersionIds.html](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecretVersionIds.html) | List the available versions of a secret | Read |
| <a name="secretsmanager-ListSecrets"></a>[https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecrets.html](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecrets.html) | List the available secrets | List |
