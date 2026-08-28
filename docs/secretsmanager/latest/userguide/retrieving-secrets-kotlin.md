---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-kotlin.html
---

# Get a Secrets Manager secret value using the Kotlin AWS SDK
<a name="retrieving-secrets-kotlin"></a>

For Kotlin applications, call the SDK directly with [GetSecretValue](https://github.com/awslabs/aws-sdk-kotlin#generating-api-documentation) or [BatchGetSecretValue](https://github.com/awslabs/aws-sdk-kotlin#generating-api-documentation).

The following code example shows how to get a Secrets Manager secret value.

**Required permissions: **`secretsmanager:GetSecretValue`

```
suspend fun getValue(secretName: String?) {
    val valueRequest =
        GetSecretValueRequest {
            secretId = secretName
        }

    SecretsManagerClient.fromEnvironment { region = "us-east-1" }.use { secretsClient ->
        val response = secretsClient.getSecretValue(valueRequest)
        val secret = response.secretString
        println("The secret value is $secret")
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
