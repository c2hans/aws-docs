---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SnapshotEncryptionConfiguration.html
---

# SnapshotEncryptionConfiguration
<a name="API_SnapshotEncryptionConfiguration"></a>

Specifies the encryption configuration of snapshot data.

## Contents
<a name="API_SnapshotEncryptionConfiguration_Contents"></a>

 ** KeyType **   <a name="APIReference-Type-SnapshotEncryptionConfiguration-KeyType"></a>
Specifies the type of key used for encryption.
Type: String
Valid Values: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KEY`
Required: Yes

 ** KeyId **   <a name="APIReference-Type-SnapshotEncryptionConfiguration-KeyId"></a>
The KMS key used for encryption. `KeyId` is used only when `KeyType` is `CUSTOMER_MANAGED_KEY`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_SnapshotEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SnapshotEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SnapshotEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SnapshotEncryptionConfiguration)
