---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_EncryptionKeyConfigurationInput.html
---

# EncryptionKeyConfigurationInput
<a name="API_EncryptionKeyConfigurationInput"></a>

The configuration of the encryption key to use for an Autonomous Database. This is a union, so only one of the following members can be specified.

## Contents
<a name="API_EncryptionKeyConfigurationInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsEncryptionKey **   <a name="odb-Type-EncryptionKeyConfigurationInput-awsEncryptionKey"></a>
The configuration of the AWS Key Management Service (KMS) encryption key to use.
Type: [AwsEncryptionKeyConfigurationInput](API_AwsEncryptionKeyConfigurationInput.md) object
Required: No

## See Also
<a name="API_EncryptionKeyConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/EncryptionKeyConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/EncryptionKeyConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/EncryptionKeyConfigurationInput)
