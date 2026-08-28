---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_OutputUpdate.html
---

# OutputUpdate
<a name="API_OutputUpdate"></a>

 For a SQL-based Kinesis Data Analytics application, describes updates to the output configuration identified by the `OutputId`.

## Contents
<a name="API_OutputUpdate_Contents"></a>

 ** OutputId **   <a name="APIReference-Type-OutputUpdate-OutputId"></a>
Identifies the specific output configuration that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** DestinationSchemaUpdate **   <a name="APIReference-Type-OutputUpdate-DestinationSchemaUpdate"></a>
Describes the data format when records are written to the destination.
Type: [DestinationSchema](API_DestinationSchema.md) object
Required: No

 ** KinesisFirehoseOutputUpdate **   <a name="APIReference-Type-OutputUpdate-KinesisFirehoseOutputUpdate"></a>
Describes a Kinesis Data Firehose delivery stream as the destination for the output.
Type: [KinesisFirehoseOutputUpdate](API_KinesisFirehoseOutputUpdate.md) object
Required: No

 ** KinesisStreamsOutputUpdate **   <a name="APIReference-Type-OutputUpdate-KinesisStreamsOutputUpdate"></a>
Describes a Kinesis data stream as the destination for the output.
Type: [KinesisStreamsOutputUpdate](API_KinesisStreamsOutputUpdate.md) object
Required: No

 ** LambdaOutputUpdate **   <a name="APIReference-Type-OutputUpdate-LambdaOutputUpdate"></a>
Describes an Amazon Lambda function as the destination for the output.
Type: [LambdaOutputUpdate](API_LambdaOutputUpdate.md) object
Required: No

 ** NameUpdate **   <a name="APIReference-Type-OutputUpdate-NameUpdate"></a>
If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^-\s<>&]*`
Required: No

## See Also
<a name="API_OutputUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/OutputUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/OutputUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/OutputUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
