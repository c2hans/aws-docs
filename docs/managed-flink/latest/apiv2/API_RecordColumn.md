---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RecordColumn.html
---

# RecordColumn
<a name="API_RecordColumn"></a>

For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

## Contents
<a name="API_RecordColumn_Contents"></a>

 ** Name **   <a name="APIReference-Type-RecordColumn-Name"></a>
The name of the column that is created in the in-application input stream or reference table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^-\s<>&]*`
Required: Yes

 ** SqlType **   <a name="APIReference-Type-RecordColumn-SqlType"></a>
The type of column created in the in-application input stream or reference table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Mapping **   <a name="APIReference-Type-RecordColumn-Mapping"></a>
A reference to the data element in the streaming input or the reference data source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65535.
Required: No

## See Also
<a name="API_RecordColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/RecordColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/RecordColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/RecordColumn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
