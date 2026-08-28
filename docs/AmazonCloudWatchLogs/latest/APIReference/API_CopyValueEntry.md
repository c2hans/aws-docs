---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CopyValueEntry.html
---

# CopyValueEntry
<a name="API_CopyValueEntry"></a>

This object defines one value to be copied with the [ copyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-copoyValue) processor.

## Contents
<a name="API_CopyValueEntry_Contents"></a>

 ** source **   <a name="CWL-Type-CopyValueEntry-source"></a>
The key to copy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** target **   <a name="CWL-Type-CopyValueEntry-target"></a>
The key of the field to copy the value to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** overwriteIfExists **   <a name="CWL-Type-CopyValueEntry-overwriteIfExists"></a>
Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_CopyValueEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CopyValueEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CopyValueEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CopyValueEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
