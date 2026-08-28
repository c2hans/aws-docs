---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Anomaly.html
---

# Anomaly
<a name="API_Anomaly"></a>

 Details about an anomaly in a specific metric of application profile. The anomaly is detected using analysis of the metric data over a period of time.

## Contents
<a name="API_Anomaly_Contents"></a>

 ** instances **   <a name="profiler-Type-Anomaly-instances"></a>
 A list of the instances of the detected anomalies during the requested period.
Type: Array of [AnomalyInstance](API_AnomalyInstance.md) objects
Required: Yes

 ** metric **   <a name="profiler-Type-Anomaly-metric"></a>
 Details about the metric that the analysis used when it detected the anomaly. The metric includes the name of the frame that was analyzed with the type and thread states used to derive the metric value for that frame.
Type: [Metric](API_Metric.md) object
Required: Yes

 ** reason **   <a name="profiler-Type-Anomaly-reason"></a>
The reason for which metric was flagged as anomalous.
Type: String
Required: Yes

## See Also
<a name="API_Anomaly_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/Anomaly)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/Anomaly)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/Anomaly)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Profiler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
