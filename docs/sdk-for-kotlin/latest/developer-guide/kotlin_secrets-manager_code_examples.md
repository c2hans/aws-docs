---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_secrets-manager_code_examples.html
---

# Secrets Manager examples using SDK for Kotlin
<a name="kotlin_secrets-manager_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Kotlin with Secrets Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `GetSecretValue`
<a name="secrets-manager_GetSecretValue_kotlin_topic"></a>

The following code example shows how to use `GetSecretValue`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/secrets-manager#code-examples).

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
+  For API details, see [GetSecretValue](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.
