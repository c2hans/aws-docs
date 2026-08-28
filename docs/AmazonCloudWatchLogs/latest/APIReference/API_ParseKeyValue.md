---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ParseKeyValue.html
---

# ParseKeyValue
<a name="API_ParseKeyValue"></a>

This processor parses a specified field in the original log event into key-value pairs.

For more information about this processor including examples, see [ parseKeyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseKeyValue) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_ParseKeyValue_Contents"></a>

 ** destination **   <a name="CWL-Type-ParseKeyValue-destination"></a>
The destination field to put the extracted key-value pairs into
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** fieldDelimiter **   <a name="CWL-Type-ParseKeyValue-fieldDelimiter"></a>
The field delimiter string that is used between key-value pairs in the original log events. If you omit this, the ampersand `&` character is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** keyPrefix **   <a name="CWL-Type-ParseKeyValue-keyPrefix"></a>
If you want to add a prefix to all transformed keys, specify it here.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** keyValueDelimiter **   <a name="CWL-Type-ParseKeyValue-keyValueDelimiter"></a>
The delimiter string to use between the key and value in each pair in the transformed log event.
 If you omit this, the equal `=` character is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** nonMatchValue **   <a name="CWL-Type-ParseKeyValue-nonMatchValue"></a>
A value to insert into the value field in the result, when a key-value pair is not successfully split.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** overwriteIfExists **   <a name="CWL-Type-ParseKeyValue-overwriteIfExists"></a>
Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is `false`.
Type: Boolean
Required: No

 ** source **   <a name="CWL-Type-ParseKeyValue-source"></a>
Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, `store.book`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ParseKeyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ParseKeyValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ParseKeyValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ParseKeyValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
