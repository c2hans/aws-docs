---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CSV.html
---

# CSV
<a name="API_CSV"></a>

The `CSV` processor parses comma-separated values (CSV) from the log events into columns.

For more information about this processor including examples, see [ csv](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-csv) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_CSV_Contents"></a>

 ** columns **   <a name="CWL-Type-CSV-columns"></a>
An array of names to use for the columns in the transformed log event.
If you omit this, default column names (`[column_1, column_2 ...]`) are used.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** delimiter **   <a name="CWL-Type-CSV-delimiter"></a>
The character used to separate each column in the original comma-separated value log event. If you omit this, the processor looks for the comma `,` character as the delimiter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2.
Required: No

 ** destination **   <a name="CWL-Type-CSV-destination"></a>
The path to the parent field to put transformed key value pairs under. If you omit this value, the key value pairs will be placed under the root node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** quoteCharacter **   <a name="CWL-Type-CSV-quoteCharacter"></a>
The character used used as a text qualifier for a single column of data. If you omit this, the double quotation mark `"` character is used.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** source **   <a name="CWL-Type-CSV-source"></a>
The path to the field in the log event that has the comma separated values to be parsed. If you omit this value, the whole log message is processed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_CSV_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CSV)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CSV)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CSV)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
