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
