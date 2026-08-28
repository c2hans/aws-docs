---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_SecretsManager.html
---

# SecretsManager
<a name="API_SecretsManager"></a>

Configuration for AWS Secrets Manager, used to securely store and manage sensitive information for connector destinations.

## Contents
<a name="API_SecretsManager_Contents"></a>

 ** arn **   <a name="managedintegrations-Type-SecretsManager-arn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:secretsmanager:[0-9a-zA-Z-]{1,32}:\d{12}:secret:[A-Za-z0-9/_+=.@-]{8,520}`
Required: Yes

 ** versionId **   <a name="managedintegrations-Type-SecretsManager-versionId"></a>
The version ID of the AWS Secrets Manager secret.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

## See Also
<a name="API_SecretsManager_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/SecretsManager)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/SecretsManager)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/SecretsManager)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
