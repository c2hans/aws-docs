---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryValues.html
---

# CostCategoryValues

The Cost Categories values used for filtering the costs.

In operations that support `ABSENT`, such as `GetCostAndUsage`, you can filter on resources that aren't mapped to any Cost Categories. Set `MatchOptions` to `ABSENT` and omit `Key` and `Values`. Not all operations support `ABSENT`. For example, `GetReservationCoverage`, `GetSavingsPlansCoverage`, and cost category rules don't.

To filter on resources without a given Cost Categories key, set `MatchOptions` to `ABSENT`, specify the `Key`, and omit `Values`.

A `Key` without `Values` doesn't apply `ABSENT`. In Cost Explorer operations such as `GetCostAndUsage`, unless `MatchOptions` includes `ABSENT`, you must specify both `Key` and `Values`, or the request fails with a `ValidationException`.

If `MatchOptions` includes `ABSENT` and you also specify `Values`, the request fails with a `ValidationException`.

## Contents
<a name="API_CostCategoryValues_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-CostCategoryValues-Key"></a>
The unique name of the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

 ** MatchOptions **   <a name="awscostmanagement-Type-CostCategoryValues-MatchOptions"></a>
The match options that you can use to filter your results. The supported values depend on the operation. Refer to the documentation for each specific API to see what is supported. For example, `GetCostAndUsage` supports the following values:
+  `EQUALS` - Matches values exactly.
+  `ABSENT` - Matches costs that don't have a value for the key.
+  `CASE_SENSITIVE` - Matches values with case sensitivity.
The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE`.
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
