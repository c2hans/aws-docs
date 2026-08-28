---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputSchemaUpdate.html
---

# InputSchemaUpdate
<a name="API_InputSchemaUpdate"></a>

Describes updates for an SQL-based Kinesis Data Analytics application's input schema.

## Contents
<a name="API_InputSchemaUpdate_Contents"></a>

 ** RecordColumnUpdates **   <a name="APIReference-Type-InputSchemaUpdate-RecordColumnUpdates"></a>
A list of `RecordColumn` objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream.
Type: Array of [RecordColumn](API_RecordColumn.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

 ** RecordEncodingUpdate **   <a name="APIReference-Type-InputSchemaUpdate-RecordEncodingUpdate"></a>
Specifies the encoding of the records in the streaming source; for example, UTF-8.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `UTF-8`
Required: No

 ** RecordFormatUpdate **   <a name="APIReference-Type-InputSchemaUpdate-RecordFormatUpdate"></a>
Specifies the format of the records on the streaming source.
Type: [RecordFormat](API_RecordFormat.md) object
Required: No

## See Also
<a name="API_InputSchemaUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/InputSchemaUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/InputSchemaUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/InputSchemaUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
