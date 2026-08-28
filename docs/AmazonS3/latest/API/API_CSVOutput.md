---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_CSVOutput.html
---

# CSVOutput
<a name="API_CSVOutput"></a>

Describes how uncompressed comma-separated values (CSV)-formatted results are formatted.

## Contents
<a name="API_CSVOutput_Contents"></a>

 ** FieldDelimiter **   <a name="AmazonS3-Type-CSVOutput-FieldDelimiter"></a>
The value used to separate individual fields in a record. You can specify an arbitrary delimiter.
Type: String
Required: No

 ** QuoteCharacter **   <a name="AmazonS3-Type-CSVOutput-QuoteCharacter"></a>
A single character used for escaping when the field delimiter is part of the value. For example, if the value is `a, b`, Amazon S3 wraps this field value in quotation marks, as follows: `" a , b "`.
Type: String
Required: No

 ** QuoteEscapeCharacter **   <a name="AmazonS3-Type-CSVOutput-QuoteEscapeCharacter"></a>
The single character used for escaping the quote character inside an already escaped value.
Type: String
Required: No

 ** QuoteFields **   <a name="AmazonS3-Type-CSVOutput-QuoteFields"></a>
Indicates whether to use quotation marks around output fields.
+  `ALWAYS`: Always use quotation marks for output fields.
+  `ASNEEDED`: Use quotation marks for output fields when needed.
Type: String
Valid Values: `ALWAYS | ASNEEDED`
Required: No

 ** RecordDelimiter **   <a name="AmazonS3-Type-CSVOutput-RecordDelimiter"></a>
A single character used to separate individual records in the output. Instead of the default value, you can specify an arbitrary delimiter.
Type: String
Required: No

## See Also
<a name="API_CSVOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CSVOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CSVOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CSVOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
