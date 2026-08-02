---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_MetricKeyDataPoints.html
---

# MetricKeyDataPoints
<a name="API_MetricKeyDataPoints"></a>

A time-ordered series of data points, corresponding to a dimension of a Performance Insights metric.

## Contents
<a name="API_MetricKeyDataPoints_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataPoints **   <a name="performanceinsights-Type-MetricKeyDataPoints-DataPoints"></a>
An array of timestamp-value pairs, representing measurements over a period of time.
Type: Array of [DataPoint](API_DataPoint.md) objects
Required: No

 ** Key **   <a name="performanceinsights-Type-MetricKeyDataPoints-Key"></a>
The dimensions to which the data points apply.
Type: [ResponseResourceMetricKey](API_ResponseResourceMetricKey.md) object
Required: No

## See Also
<a name="API_MetricKeyDataPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/MetricKeyDataPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/MetricKeyDataPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/MetricKeyDataPoints)
