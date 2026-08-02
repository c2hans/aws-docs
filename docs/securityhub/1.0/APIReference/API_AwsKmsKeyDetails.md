---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsKmsKeyDetails.html
---

# AwsKmsKeyDetails
<a name="API_AwsKmsKeyDetails"></a>

Contains metadata about an AWS KMS key.

## Contents
<a name="API_AwsKmsKeyDetails_Contents"></a>

 ** AWSAccountId **   <a name="securityhub-Type-AwsKmsKeyDetails-AWSAccountId"></a>
The twelve-digit account ID of the AWS account that owns the KMS key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreationDate **   <a name="securityhub-Type-AwsKmsKeyDetails-CreationDate"></a>
Indicates when the KMS key was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Double
Required: No

 ** Description **   <a name="securityhub-Type-AwsKmsKeyDetails-Description"></a>
A description of the KMS key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeyId **   <a name="securityhub-Type-AwsKmsKeyDetails-KeyId"></a>
The globally unique identifier for the KMS key.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeyManager **   <a name="securityhub-Type-AwsKmsKeyDetails-KeyManager"></a>
The manager of the KMS key. KMS keys in your AWS account are either customer managed or AWS managed.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeyRotationStatus **   <a name="securityhub-Type-AwsKmsKeyDetails-KeyRotationStatus"></a>
Whether the key has key rotation enabled.
Type: Boolean
Required: No

 ** KeyState **   <a name="securityhub-Type-AwsKmsKeyDetails-KeyState"></a>
The state of the KMS key. Valid values are as follows:
+  `Disabled`
+  `Enabled`
+  `PendingDeletion`
+  `PendingImport`
+  `Unavailable`
Type: String
Pattern: `.*\S.*`
Required: No

 ** Origin **   <a name="securityhub-Type-AwsKmsKeyDetails-Origin"></a>
The source of the KMS key material.
When this value is `AWS_KMS`, AWS KMS created the key material.
When this value is `EXTERNAL`, the key material was imported from your existing key management infrastructure or the KMS key lacks key material.
When this value is `AWS_CLOUDHSM`, the key material was created in the AWS CloudHSM cluster associated with a custom key store.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsKmsKeyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsKmsKeyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsKmsKeyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsKmsKeyDetails)
