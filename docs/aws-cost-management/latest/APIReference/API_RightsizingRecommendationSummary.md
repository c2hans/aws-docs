---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RightsizingRecommendationSummary.html
---

# RightsizingRecommendationSummary
<a name="API_RightsizingRecommendationSummary"></a>

The summary of rightsizing recommendations

## Contents
<a name="API_RightsizingRecommendationSummary_Contents"></a>

 ** EstimatedTotalMonthlySavingsAmount **   <a name="awscostmanagement-Type-RightsizingRecommendationSummary-EstimatedTotalMonthlySavingsAmount"></a>
The estimated total savings resulting from modifications, on a monthly basis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SavingsCurrencyCode **   <a name="awscostmanagement-Type-RightsizingRecommendationSummary-SavingsCurrencyCode"></a>
The currency code that AWS used to calculate the savings.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SavingsPercentage **   <a name="awscostmanagement-Type-RightsizingRecommendationSummary-SavingsPercentage"></a>
 The savings percentage based on the recommended modifications. It's relative to the total On-Demand costs that are associated with these instances.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** TotalRecommendationCount **   <a name="awscostmanagement-Type-RightsizingRecommendationSummary-TotalRecommendationCount"></a>
The total number of instance recommendations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_RightsizingRecommendationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/RightsizingRecommendationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/RightsizingRecommendationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/RightsizingRecommendationSummary)
