---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

 A structure that specifies the KMS key type and KMS key ARN used to encrypt data in your IAM Identity Center instance.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** KeyType **   <a name="singlesignon-Type-EncryptionConfiguration-KeyType"></a>
The type of KMS key used for encryption.
Type: String
Valid Values: `AWS_OWNED_KMS_KEY | CUSTOMER_MANAGED_KEY`
Required: Yes

 ** KmsKeyArn **   <a name="singlesignon-Type-EncryptionConfiguration-KmsKeyArn"></a>
The ARN of the KMS key used to encrypt data. Required when KeyType is CUSTOMER\_MANAGED\_KEY. Cannot be specified when KeyType is AWS\_OWNED\_KMS\_KEY.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:kms:([a-z]{2,}(-[a-z0-9]+)+){1}:[0-9]{12}:key/(mrk-[a-f0-9]{32}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/EncryptionConfiguration)
