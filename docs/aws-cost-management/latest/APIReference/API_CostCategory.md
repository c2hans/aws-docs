---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html
---

# CostCategory
<a name="API_CostCategory"></a>

The structure of Cost Categories. This includes detailed metadata and the set of rules for the `CostCategory` object.

## Contents
<a name="API_CostCategory_Contents"></a>

 ** CostCategoryArn **   <a name="awscostmanagement-Type-CostCategory-CostCategoryArn"></a>
The unique identifier for your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

 ** EffectiveStart **   <a name="awscostmanagement-Type-CostCategory-EffectiveStart"></a>
The effective start date of your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: Yes

 ** Name **   <a name="awscostmanagement-Type-CostCategory-Name"></a>
The unique name of the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: Yes

 ** Rules **   <a name="awscostmanagement-Type-CostCategory-Rules"></a>
The rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that cost category value.
Type: Array of [CostCategoryRule](API_CostCategoryRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: Yes

 ** RuleVersion **   <a name="awscostmanagement-Type-CostCategory-RuleVersion"></a>
The rule schema version in this particular cost category.
Type: String
Valid Values: `CostCategoryExpression.v1`
Required: Yes

 ** DefaultValue **   <a name="awscostmanagement-Type-CostCategory-DefaultValue"></a>
The default value for the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

 ** EffectiveEnd **   <a name="awscostmanagement-Type-CostCategory-EffectiveEnd"></a>
The effective end date of your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** ProcessingStatus **   <a name="awscostmanagement-Type-CostCategory-ProcessingStatus"></a>
The list of processing statuses for Cost Management products for a specific cost category.
Type: Array of [CostCategoryProcessingStatus](API_CostCategoryProcessingStatus.md) objects
Required: No

 ** SplitChargeRules **   <a name="awscostmanagement-Type-CostCategory-SplitChargeRules"></a>
 The split charge rules that are used to allocate your charges between your cost category values.
Type: Array of [CostCategorySplitChargeRule](API_CostCategorySplitChargeRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CostCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostCategory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostCategory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostCategory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
