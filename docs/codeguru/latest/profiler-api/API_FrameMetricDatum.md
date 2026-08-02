---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FrameMetricDatum.html
---

# FrameMetricDatum
<a name="API_FrameMetricDatum"></a>

 Information about a frame metric and its values.

## Contents
<a name="API_FrameMetricDatum_Contents"></a>

 ** frameMetric **   <a name="profiler-Type-FrameMetricDatum-frameMetric"></a>
 The frame name, metric type, and thread states. These are used to derive the value of the metric for the frame.
Type: [FrameMetric](API_FrameMetric.md) object
Required: Yes

 ** values **   <a name="profiler-Type-FrameMetricDatum-values"></a>
 A list of values that are associated with a frame metric.
Type: Array of doubles
Required: Yes

## See Also
<a name="API_FrameMetricDatum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/FrameMetricDatum)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/FrameMetricDatum)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/FrameMetricDatum)
