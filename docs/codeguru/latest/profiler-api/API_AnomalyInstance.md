---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AnomalyInstance.html
---

# AnomalyInstance
<a name="API_AnomalyInstance"></a>

The specific duration in which the metric is flagged as anomalous.

## Contents
<a name="API_AnomalyInstance_Contents"></a>

 ** id **   <a name="profiler-Type-AnomalyInstance-id"></a>
 The universally unique identifier (UUID) of an instance of an anomaly in a metric.
Type: String
Required: Yes

 ** startTime **   <a name="profiler-Type-AnomalyInstance-startTime"></a>
 The start time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: Yes

 ** endTime **   <a name="profiler-Type-AnomalyInstance-endTime"></a>
 The end time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: No

 ** userFeedback **   <a name="profiler-Type-AnomalyInstance-userFeedback"></a>
Feedback type on a specific instance of anomaly submitted by the user.
Type: [UserFeedback](API_UserFeedback.md) object
Required: No

## See Also
<a name="API_AnomalyInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/AnomalyInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/AnomalyInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/AnomalyInstance)
