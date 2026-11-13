---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Trend.html
---

# Trend
<a name="API_Trend"></a>

Contains information about the number of findings over time.

## Contents
<a name="API_Trend_Contents"></a>

 ** byTimeWindow **   <a name="guardduty-Type-Trend-byTimeWindow"></a>
The number of findings in each time window.
Type: Array of [TimeWindowGroup](API_TimeWindowGroup.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** endTime **   <a name="guardduty-Type-Trend-endTime"></a>
The timestamp at which the period of the trend ends.
Type: Timestamp
Required: No

 ** granularity **   <a name="guardduty-Type-Trend-granularity"></a>
The length of each time window in the trend. Possible values are `DAY`, `WEEK`, and `MONTH`.
Type: String
Valid Values: `DAY | WEEK | MONTH`
Required: No

 ** startTime **   <a name="guardduty-Type-Trend-startTime"></a>
The timestamp at which the period of the trend starts.
Type: Timestamp
Required: No

 ** totalFindings **   <a name="guardduty-Type-Trend-totalFindings"></a>
The total number of findings in the period.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Trend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Trend)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Trend)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Trend)
