---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_MappingParameters.html
---

# MappingParameters
<a name="API_MappingParameters"></a>

When you configure a SQL-based Kinesis Data Analytics application's input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

## Contents
<a name="API_MappingParameters_Contents"></a>

 ** CSVMappingParameters **   <a name="APIReference-Type-MappingParameters-CSVMappingParameters"></a>
Provides additional mapping information when the record format uses delimiters (for example, CSV).
Type: [CSVMappingParameters](API_CSVMappingParameters.md) object
Required: No

 ** JSONMappingParameters **   <a name="APIReference-Type-MappingParameters-JSONMappingParameters"></a>
Provides additional mapping information when JSON is the record format on the streaming source.
Type: [JSONMappingParameters](API_JSONMappingParameters.md) object
Required: No

## See Also
<a name="API_MappingParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/MappingParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/MappingParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/MappingParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
