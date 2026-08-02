---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_KinesisStreamConfig.html
---

# KinesisStreamConfig
<a name="API_KinesisStreamConfig"></a>

Contains information about the Amazon Kinesis data stream where you are sending real-time log data.

## Contents
<a name="API_KinesisStreamConfig_Contents"></a>

 ** RoleARN **   <a name="cloudfront-Type-KinesisStreamConfig-RoleARN"></a>
The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that CloudFront can use to send real-time log data to your Kinesis data stream.
For more information the IAM role, see [Real-time log configuration IAM role](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-iam-role) in the *Amazon CloudFront Developer Guide*.
Type: String
Required: Yes

 ** StreamARN **   <a name="cloudfront-Type-KinesisStreamConfig-StreamARN"></a>
The Amazon Resource Name (ARN) of the Kinesis data stream where you are sending real-time log data.
Type: String
Required: Yes

## See Also
<a name="API_KinesisStreamConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/KinesisStreamConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/KinesisStreamConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/KinesisStreamConfig)
