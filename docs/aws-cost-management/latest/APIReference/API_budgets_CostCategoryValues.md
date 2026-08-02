---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CostCategoryValues.html
---

# CostCategoryValues
<a name="API_budgets_CostCategoryValues"></a>

The cost category values used for filtering the costs.

## Contents
<a name="API_budgets_CostCategoryValues_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-budgets_CostCategoryValues-Key"></a>
The unique name of the cost category.
Type: String
Required: No

 ** MatchOptions **   <a name="awscostmanagement-Type-budgets_CostCategoryValues-MatchOptions"></a>
The match options that you can use to filter your results.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | GREATER_THAN_OR_EQUAL | CASE_SENSITIVE | CASE_INSENSITIVE`
Required: No

 ** Values **   <a name="awscostmanagement-Type-budgets_CostCategoryValues-Values"></a>
The specific value of the cost category.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_budgets_CostCategoryValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/CostCategoryValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/CostCategoryValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/CostCategoryValues)
