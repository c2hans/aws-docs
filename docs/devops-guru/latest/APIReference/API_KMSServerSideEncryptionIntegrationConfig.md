---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_KMSServerSideEncryptionIntegrationConfig.html
---

# KMSServerSideEncryptionIntegrationConfig
<a name="API_KMSServerSideEncryptionIntegrationConfig"></a>

 Information about whether DevOps Guru is configured to encrypt server-side data using KMS.

## Contents
<a name="API_KMSServerSideEncryptionIntegrationConfig_Contents"></a>

 ** KMSKeyId **   <a name="DevOpsGuru-Type-KMSServerSideEncryptionIntegrationConfig-KMSKeyId"></a>
 Describes the specified KMS key.
To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with "alias/". If you specify a predefined AWS alias (an AWS alias with no key ID), AWS KMS associates the alias with an AWS managed key and returns its KeyId and Arn in the response. To specify a KMS key in a different AWS account, you must use the key ARN or alias ARN.
For example:
Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
Alias name: alias/ExampleAlias
Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^.*$`
Required: No

 ** OptInStatus **   <a name="DevOpsGuru-Type-KMSServerSideEncryptionIntegrationConfig-OptInStatus"></a>
 Specifies if DevOps Guru is enabled for KMS integration.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** Type **   <a name="DevOpsGuru-Type-KMSServerSideEncryptionIntegrationConfig-Type"></a>
 The type of KMS key used. Customer managed keys are the KMS keys that you create. AWS owned keys are keys that are owned and managed by DevOps Guru.
Type: String
Valid Values: `CUSTOMER_MANAGED_KEY | AWS_OWNED_KMS_KEY`
Required: No

## See Also
<a name="API_KMSServerSideEncryptionIntegrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/KMSServerSideEncryptionIntegrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/KMSServerSideEncryptionIntegrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/KMSServerSideEncryptionIntegrationConfig)
