---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputUpdate.html
---

# InputUpdate
<a name="API_InputUpdate"></a>

For a SQL-based Kinesis Data Analytics application, describes updates to a specific input configuration (identified by the `InputId` of an application).

## Contents
<a name="API_InputUpdate_Contents"></a>

 ** InputId **   <a name="APIReference-Type-InputUpdate-InputId"></a>
The input ID of the application input to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** InputParallelismUpdate **   <a name="APIReference-Type-InputUpdate-InputParallelismUpdate"></a>
Describes the parallelism updates (the number of in-application streams Kinesis Data Analytics creates for the specific streaming source).
Type: [InputParallelismUpdate](API_InputParallelismUpdate.md) object
Required: No

 ** InputProcessingConfigurationUpdate **   <a name="APIReference-Type-InputUpdate-InputProcessingConfigurationUpdate"></a>
Describes updates to an [InputProcessingConfiguration](API_InputProcessingConfiguration.md).
Type: [InputProcessingConfigurationUpdate](API_InputProcessingConfigurationUpdate.md) object
Required: No

 ** InputSchemaUpdate **   <a name="APIReference-Type-InputUpdate-InputSchemaUpdate"></a>
Describes the data format on the streaming source, and how record elements on the streaming source map to columns of the in-application stream that is created.
Type: [InputSchemaUpdate](API_InputSchemaUpdate.md) object
Required: No

 ** KinesisFirehoseInputUpdate **   <a name="APIReference-Type-InputUpdate-KinesisFirehoseInputUpdate"></a>
If a Kinesis Data Firehose delivery stream is the streaming source to be updated, provides an updated stream ARN.
Type: [KinesisFirehoseInputUpdate](API_KinesisFirehoseInputUpdate.md) object
Required: No

 ** KinesisStreamsInputUpdate **   <a name="APIReference-Type-InputUpdate-KinesisStreamsInputUpdate"></a>
If a Kinesis data stream is the streaming source to be updated, provides an updated stream Amazon Resource Name (ARN).
Type: [KinesisStreamsInputUpdate](API_KinesisStreamsInputUpdate.md) object
Required: No

 ** NamePrefixUpdate **   <a name="APIReference-Type-InputUpdate-NamePrefixUpdate"></a>
The name prefix for in-application streams that Kinesis Data Analytics creates for the specific streaming source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^-\s<>&]*`
Required: No

## See Also
<a name="API_InputUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/InputUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/InputUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/InputUpdate)
