---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DifferentialPrivacySensitivityParameters.html
---

# DifferentialPrivacySensitivityParameters
<a name="API_DifferentialPrivacySensitivityParameters"></a>

Provides the sensitivity parameters.

## Contents
<a name="API_DifferentialPrivacySensitivityParameters_Contents"></a>

 ** aggregationExpression **   <a name="API-Type-DifferentialPrivacySensitivityParameters-aggregationExpression"></a>
The aggregation expression that was run.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** aggregationType **   <a name="API-Type-DifferentialPrivacySensitivityParameters-aggregationType"></a>
The type of aggregation function that was run.
Type: String
Valid Values: `AVG | COUNT | COUNT_DISTINCT | SUM | STDDEV`
Required: Yes

 ** userContributionLimit **   <a name="API-Type-DifferentialPrivacySensitivityParameters-userContributionLimit"></a>
The maximum number of rows contributed by a user in a SQL query.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** maxColumnValue **   <a name="API-Type-DifferentialPrivacySensitivityParameters-maxColumnValue"></a>
The upper bound of the aggregation expression.
Type: Float
Required: No

 ** minColumnValue **   <a name="API-Type-DifferentialPrivacySensitivityParameters-minColumnValue"></a>
The lower bound of the aggregation expression.
Type: Float
Required: No

## See Also
<a name="API_DifferentialPrivacySensitivityParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DifferentialPrivacySensitivityParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DifferentialPrivacySensitivityParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DifferentialPrivacySensitivityParameters)
