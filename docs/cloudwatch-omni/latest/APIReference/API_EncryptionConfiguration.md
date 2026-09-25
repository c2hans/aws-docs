---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

How a resource's data at rest is encrypted.

 `kmsKeyArn` is required when `encryptionStrategy` is CUSTOMER\_MANAGED and must be absent when it is AWS\_OWNED; a mismatch is a ValidationException rather than a silently ignored field, so a caller that selects AWS\_OWNED while still passing a key learns that the key was not applied.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** encryptionStrategy **   <a name="cloudwatchomni-Type-EncryptionConfiguration-encryptionStrategy"></a>
Which kind of key to use. Required.
Type: String
Valid Values: `AWS_OWNED | CUSTOMER_MANAGED`
Required: Yes

 ** kmsKeyArn **   <a name="cloudwatchomni-Type-EncryptionConfiguration-kmsKeyArn"></a>
Customer managed KMS key ARN. Required when `encryptionStrategy` is CUSTOMER\_MANAGED, and must be omitted when it is AWS\_OWNED. Must be a symmetric ENCRYPT\_DECRYPT key in the caller's account and region.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/(mrk-)?[a-f0-9-]+`
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/EncryptionConfiguration)
