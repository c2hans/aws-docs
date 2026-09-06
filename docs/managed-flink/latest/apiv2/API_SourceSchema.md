---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SourceSchema.html
---

# SourceSchema
<a name="API_SourceSchema"></a>

For a SQL-based Kinesis Data Analytics application, describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

## Contents
<a name="API_SourceSchema_Contents"></a>

 ** RecordColumns **   <a name="APIReference-Type-SourceSchema-RecordColumns"></a>
A list of `RecordColumn` objects.
Type: Array of [RecordColumn](API_RecordColumn.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: Yes

 ** RecordFormat **   <a name="APIReference-Type-SourceSchema-RecordFormat"></a>
Specifies the format of the records on the streaming source.
Type: [RecordFormat](API_RecordFormat.md) object
Required: Yes

 ** RecordEncoding **   <a name="APIReference-Type-SourceSchema-RecordEncoding"></a>
Specifies the encoding of the records in the streaming source. For example, UTF-8.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `UTF-8`
Required: No

## See Also
<a name="API_SourceSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SourceSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SourceSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SourceSchema)
