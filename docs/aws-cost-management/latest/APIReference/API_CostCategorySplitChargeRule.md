---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategorySplitChargeRule.html
---

# CostCategorySplitChargeRule
<a name="API_CostCategorySplitChargeRule"></a>

Use the split charge rule to split the cost of one cost category value across several other target values.

## Contents
<a name="API_CostCategorySplitChargeRule_Contents"></a>

 ** Method **   <a name="awscostmanagement-Type-CostCategorySplitChargeRule-Method"></a>
The method that's used to define how to split your source costs across your targets.
 `Proportional` - Allocates charges across your targets based on the proportional weighted cost of each target.
 `Fixed` - Allocates charges across your targets based on your defined allocation percentage.
>`Even` - Allocates costs evenly across all targets.
Type: String
Valid Values: `FIXED | PROPORTIONAL | EVEN`
Required: Yes

 ** Source **   <a name="awscostmanagement-Type-CostCategorySplitChargeRule-Source"></a>
The cost category value that you want to split. That value can't be used as a source or a target in other split charge rules. To indicate uncategorized costs, you can use an empty string as the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** Targets **   <a name="awscostmanagement-Type-CostCategorySplitChargeRule-Targets"></a>
The cost category values that you want to split costs across. These values can't be used as a source in other split charge rules.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** Parameters **   <a name="awscostmanagement-Type-CostCategorySplitChargeRule-Parameters"></a>
The parameters for a split charge method. This is only required for the `FIXED` method.
Type: Array of [CostCategorySplitChargeRuleParameter](API_CostCategorySplitChargeRuleParameter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CostCategorySplitChargeRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostCategorySplitChargeRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostCategorySplitChargeRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostCategorySplitChargeRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
