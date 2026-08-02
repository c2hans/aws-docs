---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ParseJSON.html
---

# ParseJSON
<a name="API_ParseJSON"></a>

This processor parses log events that are in JSON format. It can extract JSON key-value pairs and place them under a destination that you specify.

Additionally, because you must have at least one parse-type processor in a transformer, you can use `ParseJSON` as that processor for JSON-format logs, so that you can also apply other processors, such as mutate processors, to these logs.

For more information about this processor including examples, see [ parseJSON](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseJSON) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_ParseJSON_Contents"></a>

 ** destination **   <a name="CWL-Type-ParseJSON-destination"></a>
The location to put the parsed key value pair into. If you omit this parameter, it is placed under the root node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** source **   <a name="CWL-Type-ParseJSON-source"></a>
Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, `store.book`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ParseJSON_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ParseJSON)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ParseJSON)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ParseJSON)
