---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CSVMappingParameters.html
---

# CSVMappingParameters
<a name="API_CSVMappingParameters"></a>

For a SQL-based Kinesis Data Analytics application, provides additional mapping information when the record format uses delimiters, such as CSV. For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter:

 `"name1", "address1"`

 `"name2", "address2"`

## Contents
<a name="API_CSVMappingParameters_Contents"></a>

 ** RecordColumnDelimiter **   <a name="APIReference-Type-CSVMappingParameters-RecordColumnDelimiter"></a>
The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** RecordRowDelimiter **   <a name="APIReference-Type-CSVMappingParameters-RecordRowDelimiter"></a>
The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_CSVMappingParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CSVMappingParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CSVMappingParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CSVMappingParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
