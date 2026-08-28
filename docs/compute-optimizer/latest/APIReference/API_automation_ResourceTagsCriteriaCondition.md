---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ResourceTagsCriteriaCondition.html
---

# ResourceTagsCriteriaCondition
<a name="API_automation_ResourceTagsCriteriaCondition"></a>

Criteria condition for filtering resources based on their tags, including comparison operators and values.

## Contents
<a name="API_automation_ResourceTagsCriteriaCondition_Contents"></a>

 ** comparison **   <a name="computeoptimizer-Type-automation_ResourceTagsCriteriaCondition-comparison"></a>
The comparison operator used to evaluate the tag criteria, such as equals, not equals, or contains.
Type: String
Valid Values: `StringEquals | StringNotEquals | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike | StringNotLike | NumericEquals | NumericNotEquals | NumericLessThan | NumericLessThanEquals | NumericGreaterThan | NumericGreaterThanEquals`
Required: No

 ** key **   <a name="computeoptimizer-Type-automation_ResourceTagsCriteriaCondition-key"></a>
The tag key to use for comparison when filtering resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\s\.\-\:\/\=\+\@\*\?]+`
Required: No

 ** values **   <a name="computeoptimizer-Type-automation_ResourceTagsCriteriaCondition-values"></a>
List of tag values to compare against when filtering resources.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\s\.\-\:\/\=\+\@\*\?]+`
Required: No

## See Also
<a name="API_automation_ResourceTagsCriteriaCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ResourceTagsCriteriaCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ResourceTagsCriteriaCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ResourceTagsCriteriaCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
