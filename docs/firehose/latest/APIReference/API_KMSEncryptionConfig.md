---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_KMSEncryptionConfig.html
---

# KMSEncryptionConfig
<a name="API_KMSEncryptionConfig"></a>

Describes an encryption key for a destination in Amazon S3.

## Contents
<a name="API_KMSEncryptionConfig_Contents"></a>

 ** AWSKMSKeyARN **   <a name="Firehose-Type-KMSEncryptionConfig-AWSKMSKeyARN"></a>
The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:kms:[a-zA-Z0-9\-]+:\d{12}:(key|alias)/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

## See Also
<a name="API_KMSEncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/KMSEncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/KMSEncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/KMSEncryptionConfig)
