---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ExternalSecretRotationMetadataItem.html
---

# ExternalSecretRotationMetadataItem
<a name="API_ExternalSecretRotationMetadataItem"></a>

The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information, see [Managed external secret partners](https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html).

## Contents
<a name="API_ExternalSecretRotationMetadataItem_Contents"></a>

 ** Key **   <a name="SecretsManager-Type-ExternalSecretRotationMetadataItem-Key"></a>
The key that identifies the item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Value **   <a name="SecretsManager-Type-ExternalSecretRotationMetadataItem-Value"></a>
The value of the specified item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ExternalSecretRotationMetadataItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/ExternalSecretRotationMetadataItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/ExternalSecretRotationMetadataItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/ExternalSecretRotationMetadataItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
