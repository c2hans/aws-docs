---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstancePropertyStringFilter.html
---

# InstancePropertyStringFilter
<a name="API_InstancePropertyStringFilter"></a>

The filters to describe or get information about your managed nodes.

## Contents
<a name="API_InstancePropertyStringFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-InstancePropertyStringFilter-Key"></a>
The filter key name to describe your managed nodes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Pattern: `^.{1,100000}$`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-InstancePropertyStringFilter-Values"></a>
The filter key name to describe your managed nodes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Length Constraints: Minimum length of 1. Maximum length of 100000.
Pattern: `^.{1,100000}$`
Required: Yes

 ** Operator **   <a name="systemsmanager-Type-InstancePropertyStringFilter-Operator"></a>
The operator used by the filter call.
Type: String
Valid Values: `Equal | NotEqual | BeginWith | LessThan | GreaterThan`
Required: No

## See Also
<a name="API_InstancePropertyStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstancePropertyStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstancePropertyStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstancePropertyStringFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
