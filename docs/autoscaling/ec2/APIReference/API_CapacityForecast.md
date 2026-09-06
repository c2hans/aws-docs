---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CapacityForecast.html
---

# CapacityForecast
<a name="API_CapacityForecast"></a>

A `GetPredictiveScalingForecast` call returns the capacity forecast for a predictive scaling policy. This structure includes the data points for that capacity forecast, along with the timestamps of those data points.

## Contents
<a name="API_CapacityForecast_Contents"></a>

 ** Timestamps.member.N **
The timestamps for the data points, in UTC format.
Type: Array of timestamps
Required: Yes

 ** Values.member.N **
The values of the data points.
Type: Array of doubles
Required: Yes

## See Also
<a name="API_CapacityForecast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/CapacityForecast)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/CapacityForecast)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/CapacityForecast)
