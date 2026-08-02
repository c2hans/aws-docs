---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ForecastResult.html
---

# ForecastResult
<a name="API_ForecastResult"></a>

The forecast that's created for your query.

## Contents
<a name="API_ForecastResult_Contents"></a>

 ** MeanValue **   <a name="awscostmanagement-Type-ForecastResult-MeanValue"></a>
The mean value of the forecast.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** PredictionIntervalLowerBound **   <a name="awscostmanagement-Type-ForecastResult-PredictionIntervalLowerBound"></a>
The lower limit for the prediction interval.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** PredictionIntervalUpperBound **   <a name="awscostmanagement-Type-ForecastResult-PredictionIntervalUpperBound"></a>
The upper limit for the prediction interval.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** TimePeriod **   <a name="awscostmanagement-Type-ForecastResult-TimePeriod"></a>
The period of time that the forecast covers.
Type: [DateInterval](API_DateInterval.md) object
Required: No

## See Also
<a name="API_ForecastResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ForecastResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ForecastResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ForecastResult)
