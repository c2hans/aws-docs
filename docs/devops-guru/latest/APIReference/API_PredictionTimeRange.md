---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PredictionTimeRange.html
---

# PredictionTimeRange
<a name="API_PredictionTimeRange"></a>

 The time range during which anomalous behavior in a proactive anomaly or an insight is expected to occur.

## Contents
<a name="API_PredictionTimeRange_Contents"></a>

 ** StartTime **   <a name="DevOpsGuru-Type-PredictionTimeRange-StartTime"></a>
 The time range during which a metric limit is expected to be exceeded. This applies to proactive insights only.
Type: Timestamp
Required: Yes

 ** EndTime **   <a name="DevOpsGuru-Type-PredictionTimeRange-EndTime"></a>
 The time when the behavior in a proactive insight is expected to end.
Type: Timestamp
Required: No

## See Also
<a name="API_PredictionTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/PredictionTimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/PredictionTimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/PredictionTimeRange)
