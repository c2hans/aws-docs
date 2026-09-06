---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_AnomalyTimeRange.html
---

# AnomalyTimeRange
<a name="API_AnomalyTimeRange"></a>

 A time range that specifies when the observed unusual behavior in an anomaly started and ended. This is different from `AnomalyReportedTimeRange`, which specifies the time range when DevOps Guru opens and then closes an anomaly.

## Contents
<a name="API_AnomalyTimeRange_Contents"></a>

 ** StartTime **   <a name="DevOpsGuru-Type-AnomalyTimeRange-StartTime"></a>
 The time when the anomalous behavior started.
Type: Timestamp
Required: Yes

 ** EndTime **   <a name="DevOpsGuru-Type-AnomalyTimeRange-EndTime"></a>
 The time when the anomalous behavior ended.
Type: Timestamp
Required: No

## See Also
<a name="API_AnomalyTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/AnomalyTimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/AnomalyTimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/AnomalyTimeRange)
