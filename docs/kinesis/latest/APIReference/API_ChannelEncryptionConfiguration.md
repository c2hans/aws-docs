---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ChannelEncryptionConfiguration.html
---

# ChannelEncryptionConfiguration
<a name="API_ChannelEncryptionConfiguration"></a>

Specifies the AWS KMS key that Amazon Kinesis Data Streams uses to encrypt data delivered to the channel's destination.

## Contents
<a name="API_ChannelEncryptionConfiguration_Contents"></a>

 ** EncryptionType **   <a name="Streams-Type-ChannelEncryptionConfiguration-EncryptionType"></a>
The encryption type. The only valid value is `KMS`.
Type: String
Valid Values: `KMS`
Required: Yes

 ** KeyId **   <a name="Streams-Type-ChannelEncryptionConfiguration-KeyId"></a>
The identifier of the customer managed AWS KMS key. You cannot use the Amazon Kinesis Data Streams service key (`aws/kinesis`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_ChannelEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ChannelEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ChannelEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ChannelEncryptionConfiguration)
