---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_SubstituteStringEntry.html
---

# SubstituteStringEntry
<a name="API_SubstituteStringEntry"></a>

This object defines one log field key that will be replaced using the [ substituteString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-substituteString) processor.

## Contents
<a name="API_SubstituteStringEntry_Contents"></a>

 ** from **   <a name="CWL-Type-SubstituteStringEntry-from"></a>
The regular expression string to be replaced. Special regex characters such as [ and ] must be escaped using \\\\ when using double quotes and with \\ when using single quotes. For more information, see [ Class Pattern](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html) on the Oracle web site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** source **   <a name="CWL-Type-SubstituteStringEntry-source"></a>
The key to modify
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** to **   <a name="CWL-Type-SubstituteStringEntry-to"></a>
The string to be substituted for each match of `from`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_SubstituteStringEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/SubstituteStringEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/SubstituteStringEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/SubstituteStringEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
