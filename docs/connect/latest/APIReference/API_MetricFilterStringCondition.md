---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricFilterStringCondition.html
---

# MetricFilterStringCondition
<a name="API_MetricFilterStringCondition"></a>

A string comparison condition for metric filters.

## Contents
<a name="API_MetricFilterStringCondition_Contents"></a>

 ** Comparison **   <a name="connect-Type-MetricFilterStringCondition-Comparison"></a>
The comparison operator. Valid values: `MATCHES_ANY` (matches any of the specified values) \| `MATCHES_NONE` (matches none of the specified values).
Type: String
Valid Values: `MATCHES_ANY | MATCHES_NONE`
Required: Yes

 ** Values **   <a name="connect-Type-MetricFilterStringCondition-Values"></a>
The string values to compare against.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_MetricFilterStringCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricFilterStringCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricFilterStringCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricFilterStringCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
