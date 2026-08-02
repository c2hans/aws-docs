---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryValues.html
---

# CostCategoryValues
<a name="API_CostCategoryValues"></a>

The Cost Categories values used for filtering the costs.

If `Values` and `Key` are not specified, the `ABSENT` `MatchOption` is applied to all Cost Categories. That is, it filters on resources that aren't mapped to any Cost Categories.

If `Values` is provided and `Key` isn't specified, the `ABSENT` `MatchOption` is applied to the Cost Categories `Key` only. That is, it filters on resources without the given Cost Categories key.

## Contents
<a name="API_CostCategoryValues_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-CostCategoryValues-Key"></a>
The unique name of the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

 ** MatchOptions **   <a name="awscostmanagement-Type-CostCategoryValues-MatchOptions"></a>
The match options that you can use to filter your results. MatchOptions is only applicable for actions related to cost category. The default values for `MatchOptions` is `EQUALS` and `CASE_SENSITIVE`.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | CASE_SENSITIVE | CASE_INSENSITIVE | GREATER_THAN_OR_EQUAL`
Required: No

 ** Values **   <a name="awscostmanagement-Type-CostCategoryValues-Values"></a>
The specific value of the cost category.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_CostCategoryValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CostCategoryValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CostCategoryValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CostCategoryValues)
