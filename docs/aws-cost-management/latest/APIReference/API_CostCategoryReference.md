---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryReference.html
---

# CostCategoryReference
<a name="API_CostCategoryReference"></a>

A reference to a cost category containing only enough information to identify the Cost Category.

You can use this information to retrieve the full cost category information using `DescribeCostCategory`.

## Contents
<a name="API_CostCategoryReference_Contents"></a>

 ** CostCategoryArn **   <a name="awscostmanagement-Type-CostCategoryReference-CostCategoryArn"></a>
The unique identifier for your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: No

 ** DefaultValue **   <a name="awscostmanagement-Type-CostCategoryReference-DefaultValue"></a>
The default value for the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

 ** EffectiveEnd **   <a name="awscostmanagement-Type-CostCategoryReference-EffectiveEnd"></a>
The cost category's effective end date.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** EffectiveStart **   <a name="awscostmanagement-Type-CostCategoryReference-EffectiveStart"></a>
The cost category's effective start date.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** Name **   <a name="awscostmanagement-Type-CostCategoryReference-Name"></a>
The unique name of the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

 ** NumberOfRules **   <a name="awscostmanagement-Type-CostCategoryReference-NumberOfRules"></a>
The number of rules that are associated with a specific cost category.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ProcessingStatus **   <a name="awscostmanagement-Type-CostCategoryReference-ProcessingStatus"></a>
The list of processing statuses for Cost Management products for a specific cost category.
Type: Array of [CostCategoryProcessingStatus](API_CostCategoryProcessingStatus.md) objects
Required: No

 ** SupportedResourceTypes **   <a name="awscostmanagement-Type-CostCategoryReference-SupportedResourceTypes"></a>
 The resource types supported by a specific cost category.
Type: Array of strings
Pattern: `^[-a-zA-Z0-9/_]+:[-a-zA-Z0-9/_]+`
Required: No

 ** Values **   <a name="awscostmanagement-Type-CostCategoryReference-Values"></a>
A list of unique cost category values in a specific cost category.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

## See Also
<a name="API_CostCategoryReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostCategoryReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostCategoryReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostCategoryReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
