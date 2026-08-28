---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_OutputDescription.html
---

# OutputDescription
<a name="API_OutputDescription"></a>

For a SQL-based Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

## Contents
<a name="API_OutputDescription_Contents"></a>

 ** DestinationSchema **   <a name="APIReference-Type-OutputDescription-DestinationSchema"></a>
The data format used for writing data to the destination.
Type: [DestinationSchema](API_DestinationSchema.md) object
Required: No

 ** KinesisFirehoseOutputDescription **   <a name="APIReference-Type-OutputDescription-KinesisFirehoseOutputDescription"></a>
Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.
Type: [KinesisFirehoseOutputDescription](API_KinesisFirehoseOutputDescription.md) object
Required: No

 ** KinesisStreamsOutputDescription **   <a name="APIReference-Type-OutputDescription-KinesisStreamsOutputDescription"></a>
Describes the Kinesis data stream that is configured as the destination where output is written.
Type: [KinesisStreamsOutputDescription](API_KinesisStreamsOutputDescription.md) object
Required: No

 ** LambdaOutputDescription **   <a name="APIReference-Type-OutputDescription-LambdaOutputDescription"></a>
Describes the Lambda function that is configured as the destination where output is written.
Type: [LambdaOutputDescription](API_LambdaOutputDescription.md) object
Required: No

 ** Name **   <a name="APIReference-Type-OutputDescription-Name"></a>
The name of the in-application stream that is configured as output.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^-\s<>&]*`
Required: No

 ** OutputId **   <a name="APIReference-Type-OutputDescription-OutputId"></a>
A unique identifier for the output configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_OutputDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/OutputDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/OutputDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/OutputDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
