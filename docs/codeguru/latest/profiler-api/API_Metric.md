---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Metric.html
---

# Metric
<a name="API_Metric"></a>

 Details about the metric that the analysis used when it detected the anomaly. The metric what is analyzed to create recommendations. It includes the name of the frame that was analyzed and the type and thread states used to derive the metric value for that frame.

## Contents
<a name="API_Metric_Contents"></a>

 ** frameName **   <a name="profiler-Type-Metric-frameName"></a>
 The name of the method that appears as a frame in any stack in a profile.
Type: String
Required: Yes

 ** threadStates **   <a name="profiler-Type-Metric-threadStates"></a>
 The list of application runtime thread states that is used to calculate the metric value for the frame.
Type: Array of strings
Required: Yes

 ** type **   <a name="profiler-Type-Metric-type"></a>
 A type that specifies how a metric for a frame is analyzed. The supported value `AggregatedRelativeTotalTime` is an aggregation of the metric value for one frame that is calculated across the occurences of all frames in a profile.
Type: String
Valid Values: `AggregatedRelativeTotalTime`
Required: Yes

## See Also
<a name="API_Metric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/Metric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/Metric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/Metric)
