---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_DimensionValues.html
---

# DimensionValues
<a name="API_freetier_DimensionValues"></a>

Contains the specifications for the filters to use for your request.

## Contents
<a name="API_freetier_DimensionValues_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-freetier_DimensionValues-Key"></a>
The name of the dimension that you want to filter on.
Type: String
Valid Values: `SERVICE | OPERATION | USAGE_TYPE | REGION | FREE_TIER_TYPE | DESCRIPTION | USAGE_PERCENTAGE`
Required: Yes

 ** MatchOptions **   <a name="awscostmanagement-Type-freetier_DimensionValues-MatchOptions"></a>
The match options that you can use to filter your results. You can specify only one of these values in the array.
Type: Array of strings
Valid Values: `EQUALS | STARTS_WITH | ENDS_WITH | CONTAINS | GREATER_THAN_OR_EQUAL`
Required: Yes

 ** Values **   <a name="awscostmanagement-Type-freetier_DimensionValues-Values"></a>
The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[ a-zA-Z0-9\-\:\.\_\/\,\$\(\)]*`
Required: Yes

## See Also
<a name="API_freetier_DimensionValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/freetier-2023-09-07/DimensionValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/freetier-2023-09-07/DimensionValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/freetier-2023-09-07/DimensionValues)
