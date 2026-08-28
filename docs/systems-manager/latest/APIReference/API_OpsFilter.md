---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsFilter.html
---

# OpsFilter
<a name="API_OpsFilter"></a>

A filter for viewing OpsData summaries.

## Contents
<a name="API_OpsFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-OpsFilter-Key"></a>
The name of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** Values **   <a name="systemsmanager-Type-OpsFilter-Values"></a>
The filter value.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** Type **   <a name="systemsmanager-Type-OpsFilter-Type"></a>
The type of filter.
Type: String
Valid Values: `Equal | NotEqual | BeginWith | LessThan | GreaterThan | Exists`
Required: No

## See Also
<a name="API_OpsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
