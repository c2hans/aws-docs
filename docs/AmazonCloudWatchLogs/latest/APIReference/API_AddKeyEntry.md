---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AddKeyEntry.html
---

# AddKeyEntry
<a name="API_AddKeyEntry"></a>

This object defines one key that will be added with the [ addKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-addKey) processor.

## Contents
<a name="API_AddKeyEntry_Contents"></a>

 ** key **   <a name="CWL-Type-AddKeyEntry-key"></a>
The key of the new entry to be added to the log event
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** value **   <a name="CWL-Type-AddKeyEntry-value"></a>
The value of the new entry to be added to the log event
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** overwriteIfExists **   <a name="CWL-Type-AddKeyEntry-overwriteIfExists"></a>
Specifies whether to overwrite the value if the key already exists in the log event. If you omit this, the default is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_AddKeyEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/AddKeyEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/AddKeyEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/AddKeyEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
