---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MetricToRetain.html
---

# MetricToRetain
<a name="API_MetricToRetain"></a>

The metric you want to retain. Dimensions are optional.

## Contents
<a name="API_MetricToRetain_Contents"></a>

 ** metric **   <a name="iot-Type-MetricToRetain-metric"></a>
What is measured by the behavior.
Type: String
Required: Yes

 ** exportMetric **   <a name="iot-Type-MetricToRetain-exportMetric"></a>
The value indicates exporting metrics related to the `MetricToRetain ` when it's true.
Type: Boolean
Required: No

 ** metricDimension **   <a name="iot-Type-MetricToRetain-metricDimension"></a>
The dimension of a metric. This can't be used with custom metrics.
Type: [MetricDimension](API_MetricDimension.md) object
Required: No

## See Also
<a name="API_MetricToRetain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MetricToRetain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MetricToRetain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MetricToRetain)
