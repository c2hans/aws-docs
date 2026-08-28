---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Filter.html
---

# Filter
<a name="API_automation_Filter"></a>

A filter used to narrow down results based on specific criteria.

## Contents
<a name="API_automation_Filter_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-automation_Filter-name"></a>
The name of the filter field to apply.
Type: String
Valid Values: `Name | RecommendedActionType | Status | RuleType | OrganizationConfigurationRuleApplyOrder | AccountId`
Required: Yes

 ** values **   <a name="computeoptimizer-Type-automation_Filter-values"></a>
The list of values to filter by for the specified filter field.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-_\.\*\?\s]+`
Required: Yes

## See Also
<a name="API_automation_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
