---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_CapacityForecast.html
---

# CapacityForecast
<a name="API_CapacityForecast"></a>

 A `GetPredictiveScalingForecast` call returns the capacity forecast for a predictive scaling policy. This structure includes the data points for that capacity forecast, along with the timestamps of those data points.

## Contents
<a name="API_CapacityForecast_Contents"></a>

 ** Timestamps **   <a name="autoscaling-Type-CapacityForecast-Timestamps"></a>
 The timestamps for the data points, in UTC format.
Type: Array of timestamps
Required: Yes

 ** Values **   <a name="autoscaling-Type-CapacityForecast-Values"></a>
 The values of the data points.
Type: Array of doubles
Required: Yes

## See Also
<a name="API_CapacityForecast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/CapacityForecast)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/CapacityForecast)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/CapacityForecast)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
