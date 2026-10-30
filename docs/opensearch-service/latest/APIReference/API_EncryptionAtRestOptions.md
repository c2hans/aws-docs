---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_EncryptionAtRestOptions.html
---

# EncryptionAtRestOptions
<a name="API_EncryptionAtRestOptions"></a>

Specifies whether the domain should encrypt data at rest, and if so, the Key Management Service (KMS) key to use. Can only be used when creating a new domain or enabling encryption at rest for the first time on an existing domain. You can't modify this parameter after it's already been specified.

## Contents
<a name="API_EncryptionAtRestOptions_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-EncryptionAtRestOptions-Enabled"></a>
True to enable encryption at rest.
Type: Boolean
Required: No

 ** EncryptionMode **   <a name="opensearchservice-Type-EncryptionAtRestOptions-EncryptionMode"></a>
The type of encryption at rest applied to the domain's data. Valid values are `DISK` and `NATIVE`. `DISK` is the default and uses volume-level encryption. `NATIVE` uses engine-native, index-level encryption and requires encryption at rest to be enabled and OpenSearch version 3.3 or later. After the mode is set to `NATIVE`, it can't be changed back to `DISK`.
Type: String
Valid Values: `DISK | NATIVE`
Required: No

 ** KmsKeyId **   <a name="opensearchservice-Type-EncryptionAtRestOptions-KmsKeyId"></a>
The KMS key ID. Takes the form `1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `.*`
Required: No

## See Also
<a name="API_EncryptionAtRestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/EncryptionAtRestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/EncryptionAtRestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/EncryptionAtRestOptions)
