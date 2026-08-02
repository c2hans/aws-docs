---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisStreamsOutputDescription.html
---

# KinesisStreamsOutputDescription
<a name="API_KinesisStreamsOutputDescription"></a>

For an SQL-based Kinesis Data Analytics application's output, describes the Kinesis data stream that is configured as its destination.

## Contents
<a name="API_KinesisStreamsOutputDescription_Contents"></a>

 ** ResourceARN **   <a name="APIReference-Type-KinesisStreamsOutputDescription-ResourceARN"></a>
The Amazon Resource Name (ARN) of the Kinesis data stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** RoleARN **   <a name="APIReference-Type-KinesisStreamsOutputDescription-RoleARN"></a>
The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.
Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_KinesisStreamsOutputDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/KinesisStreamsOutputDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/KinesisStreamsOutputDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/KinesisStreamsOutputDescription)
