---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_KinesisStreamSourceDescription.html
---

# KinesisStreamSourceDescription
<a name="API_KinesisStreamSourceDescription"></a>

Details about a Kinesis data stream used as the source for a Firehose stream.

## Contents
<a name="API_KinesisStreamSourceDescription_Contents"></a>

 ** DeliveryStartTimestamp **   <a name="Firehose-Type-KinesisStreamSourceDescription-DeliveryStartTimestamp"></a>
Firehose starts retrieving records from the Kinesis data stream starting with this timestamp.
Type: Timestamp
Required: No

 ** KinesisStreamARN **   <a name="Firehose-Type-KinesisStreamSourceDescription-KinesisStreamARN"></a>
The Amazon Resource Name (ARN) of the source Kinesis data stream. For more information, see [Amazon Kinesis Data Streams ARN Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:kinesis:[a-zA-Z0-9\-]+:\d{12}:stream/[a-zA-Z0-9_.-]+`
Required: No

 ** RoleARN **   <a name="Firehose-Type-KinesisStreamSourceDescription-RoleARN"></a>
The ARN of the role used by the source Kinesis data stream. For more information, see [AWS Identity and Access Management (IAM) ARN Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## See Also
<a name="API_KinesisStreamSourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/KinesisStreamSourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/KinesisStreamSourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/KinesisStreamSourceDescription)
