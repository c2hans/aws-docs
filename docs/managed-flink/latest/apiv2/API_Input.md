---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_Input.html
---

# Input
<a name="API_Input"></a>

When you configure the application input for a SQL-based Kinesis Data Analytics application, you specify the streaming source, the in-application stream name that is created, and the mapping between the two.

## Contents
<a name="API_Input_Contents"></a>

 ** InputSchema **   <a name="APIReference-Type-Input-InputSchema"></a>
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.
Also used to describe the format of the reference data source.
Type: [SourceSchema](API_SourceSchema.md) object
Required: Yes

 ** NamePrefix **   <a name="APIReference-Type-Input-NamePrefix"></a>
The name prefix to use when creating an in-application stream. Suppose that you specify a prefix "`MyInApplicationStream`." Kinesis Data Analytics then creates one or more (as per the `InputParallelism` count you specified) in-application streams with the names "`MyInApplicationStream_001`," "`MyInApplicationStream_002`," and so on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^-\s<>&]*`
Required: Yes

 ** InputParallelism **   <a name="APIReference-Type-Input-InputParallelism"></a>
Describes the number of in-application streams to create.
Type: [InputParallelism](API_InputParallelism.md) object
Required: No

 ** InputProcessingConfiguration **   <a name="APIReference-Type-Input-InputProcessingConfiguration"></a>
The [InputProcessingConfiguration](API_InputProcessingConfiguration.md) for the input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is [InputLambdaProcessor](API_InputLambdaProcessor.md).
Type: [InputProcessingConfiguration](API_InputProcessingConfiguration.md) object
Required: No

 ** KinesisFirehoseInput **   <a name="APIReference-Type-Input-KinesisFirehoseInput"></a>
If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream's ARN.
Type: [KinesisFirehoseInput](API_KinesisFirehoseInput.md) object
Required: No

 ** KinesisStreamsInput **   <a name="APIReference-Type-Input-KinesisStreamsInput"></a>
If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon Resource Name (ARN).
Type: [KinesisStreamsInput](API_KinesisStreamsInput.md) object
Required: No

## See Also
<a name="API_Input_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/Input)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/Input)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/Input)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
