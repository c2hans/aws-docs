---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_EncryptionConfigurationDetails.html
---

# EncryptionConfigurationDetails
<a name="API_EncryptionConfigurationDetails"></a>

The encryption configuration of your IAM Identity Center instance, including the key type, KMS key ARN, and current encryption status.

## Contents
<a name="API_EncryptionConfigurationDetails_Contents"></a>

 ** EncryptionStatus **   <a name="singlesignon-Type-EncryptionConfigurationDetails-EncryptionStatus"></a>
The current status of encryption configuration.
Type: String
Valid Values: `UPDATING | ENABLED | UPDATE_FAILED`
Required: No

 ** EncryptionStatusReason **   <a name="singlesignon-Type-EncryptionConfigurationDetails-EncryptionStatusReason"></a>
Provides additional context about the current encryption status. This field is particularly useful when the encryption status is UPDATE\_FAILED. When encryption configuration update fails, this field contains information about the cause, which may include KMS key access issues, key not found errors, invalid key configuration, key in an invalid state, or a disabled key.
Type: String
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** KeyType **   <a name="singlesignon-Type-EncryptionConfigurationDetails-KeyType"></a>
The type of KMS key used for encryption.
Type: String
Valid Values: `AWS_OWNED_KMS_KEY | CUSTOMER_MANAGED_KEY`
Required: No

 ** KmsKeyArn **   <a name="singlesignon-Type-EncryptionConfigurationDetails-KmsKeyArn"></a>
The ARN of the KMS key currently used to encrypt data in your IAM Identity Center instance.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:kms:([a-z]{2,}(-[a-z0-9]+)+){1}:[0-9]{12}:key/(mrk-[a-f0-9]{32}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: No

## See Also
<a name="API_EncryptionConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/EncryptionConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/EncryptionConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/EncryptionConfigurationDetails)
