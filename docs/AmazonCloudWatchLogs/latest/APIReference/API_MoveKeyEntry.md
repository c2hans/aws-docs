---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_MoveKeyEntry.html
---

# MoveKeyEntry
<a name="API_MoveKeyEntry"></a>

This object defines one key that will be moved with the [ moveKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-moveKey) processor.

## Contents
<a name="API_MoveKeyEntry_Contents"></a>

 ** source **   <a name="CWL-Type-MoveKeyEntry-source"></a>
The key to move.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** target **   <a name="CWL-Type-MoveKeyEntry-target"></a>
The key to move to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** overwriteIfExists **   <a name="CWL-Type-MoveKeyEntry-overwriteIfExists"></a>
Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_MoveKeyEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/MoveKeyEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/MoveKeyEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/MoveKeyEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
