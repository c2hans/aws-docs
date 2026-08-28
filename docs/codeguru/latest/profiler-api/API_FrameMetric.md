---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FrameMetric.html
---

# FrameMetric
<a name="API_FrameMetric"></a>

 The frame name, metric type, and thread states. These are used to derive the value of the metric for the frame.

## Contents
<a name="API_FrameMetric_Contents"></a>

 ** frameName **   <a name="profiler-Type-FrameMetric-frameName"></a>
 Name of the method common across the multiple occurrences of a frame in an application profile.
Type: String
Required: Yes

 ** threadStates **   <a name="profiler-Type-FrameMetric-threadStates"></a>
List of application runtime thread states used to get the counts for a frame a derive a metric value.
Type: Array of strings
Required: Yes

 ** type **   <a name="profiler-Type-FrameMetric-type"></a>
 A type of aggregation that specifies how a metric for a frame is analyzed. The supported value `AggregatedRelativeTotalTime` is an aggregation of the metric value for one frame that is calculated across the occurrences of all frames in a profile.
Type: String
Valid Values: `AggregatedRelativeTotalTime`
Required: Yes

## See Also
<a name="API_FrameMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/FrameMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/FrameMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/FrameMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Profiler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
