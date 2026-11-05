---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_Environment.html
---

# Environment
<a name="API_Environment"></a>

Contains the environment variables that tasks in a workflow use during execution.

## Contents
<a name="API_Environment_Contents"></a>

 ** Variables **   <a name="mwaaserverless-Type-Environment-Variables"></a>
A map of environment variable names to values. Your workflow tasks use these variables while they run. You can specify up to 50 environment variables. Each name must be between 1 and 128 characters, start with a letter, and contain only letters, numbers, and underscores. Each value can be up to 255 characters.
Names that start with `AWS_` or `AIRFLOW__` are reserved. You can use the following Apache Airflow secrets backend settings, which are exceptions:
+  `AIRFLOW__WORKERS__SECRETS_BACKEND` – The secrets backend class that workers use.
+  `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS` – The keyword arguments for the secrets backend, as a JSON string.
+  `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARG__*` – Names with this prefix, for additional secrets backend configuration.
If you set `EncryptionConfiguration` to use a customer managed AWS KMS key, we encrypt the environment variables with that key. Otherwise, we store them with default encryption at rest.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_Environment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/Environment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/Environment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/Environment)
