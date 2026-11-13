---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3PrefixLocation.html
---

# S3PrefixLocation
<a name="API_S3PrefixLocation"></a>

Specifies an Amazon S3 bucket and key prefix.

## Contents
<a name="API_S3PrefixLocation_Contents"></a>

 ** BucketARN **   <a name="APIReference-Type-S3PrefixLocation-BucketARN"></a>
The ARN of the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** KeyPrefix **   <a name="APIReference-Type-S3PrefixLocation-KeyPrefix"></a>
The key prefix in the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## See Also
<a name="API_S3PrefixLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/S3PrefixLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/S3PrefixLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/S3PrefixLocation)
