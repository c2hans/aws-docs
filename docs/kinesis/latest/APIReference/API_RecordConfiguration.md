---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RecordConfiguration.html
---

# RecordConfiguration
<a name="API_RecordConfiguration"></a>

Specifies the format of records read from the source stream.

## Contents
<a name="API_RecordConfiguration_Contents"></a>

 ** RecordFormatType **   <a name="Streams-Type-RecordConfiguration-RecordFormatType"></a>
The format of records on the source stream. Valid values:
+  `GSR_JSON` - Supported only for streaming table (Amazon S3 Tables) destinations.
+  `JSON` - Supported for both general purpose Amazon S3 and streaming table destinations.
+  `STRING` - Supported only for general purpose Amazon S3 destinations.
+  `BYTE_ARRAY` - Supported only for general purpose Amazon S3 destinations.
Type: String
Valid Values: `GSR_JSON | JSON | STRING | BYTE_ARRAY`
Required: Yes

 ** GSRSchemaARN **   <a name="Streams-Type-RecordConfiguration-GSRSchemaARN"></a>
The Amazon Resource Name (ARN) of the AWS Glue Schema Registry schema used to validate records. Required when the channel destination is a streaming table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[-a-z0-9]*:glue:[-a-z0-9]+:\d{12}:schema/[-a-zA-Z0-9_$#.]+/[-a-zA-Z0-9_$#.]+`
Required: No

## See Also
<a name="API_RecordConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/RecordConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/RecordConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/RecordConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
