---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ComparisonMetricValue.html
---

# ComparisonMetricValue
<a name="API_ComparisonMetricValue"></a>

Contains cost or usage metric values for comparing two time periods. Each value includes amounts for the baseline and comparison time periods, their difference, and the unit of measurement.

## Contents
<a name="API_ComparisonMetricValue_Contents"></a>

 ** BaselineTimePeriodAmount **   <a name="awscostmanagement-Type-ComparisonMetricValue-BaselineTimePeriodAmount"></a>
The numeric value for the baseline time period measurement.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ComparisonTimePeriodAmount **   <a name="awscostmanagement-Type-ComparisonMetricValue-ComparisonTimePeriodAmount"></a>
The numeric value for the comparison time period measurement.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Difference **   <a name="awscostmanagement-Type-ComparisonMetricValue-Difference"></a>
The calculated difference between `ComparisonTimePeriodAmount` and `BaselineTimePeriodAmount`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Unit **   <a name="awscostmanagement-Type-ComparisonMetricValue-Unit"></a>
The unit of measurement applicable to all numeric values in this comparison.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ComparisonMetricValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ComparisonMetricValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ComparisonMetricValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ComparisonMetricValue)
