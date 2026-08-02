---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RecordFormat.html
---

# RecordFormat
<a name="API_RecordFormat"></a>

 For a SQL-based Kinesis Data Analytics application, describes the record format and relevant mapping information that should be applied to schematize the records on the stream.

## Contents
<a name="API_RecordFormat_Contents"></a>

 ** RecordFormatType **   <a name="APIReference-Type-RecordFormat-RecordFormatType"></a>
The type of record format.
Type: String
Valid Values: `JSON | CSV`
Required: Yes

 ** MappingParameters **   <a name="APIReference-Type-RecordFormat-MappingParameters"></a>
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
Type: [MappingParameters](API_MappingParameters.md) object
Required: No

## See Also
<a name="API_RecordFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/RecordFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/RecordFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/RecordFormat)
