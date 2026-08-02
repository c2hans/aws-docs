---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_AnomalousLogGroup.html
---

# AnomalousLogGroup
<a name="API_AnomalousLogGroup"></a>

 An Amazon CloudWatch log group that contains log anomalies and is used to generate an insight.

## Contents
<a name="API_AnomalousLogGroup_Contents"></a>

 ** ImpactEndTime **   <a name="DevOpsGuru-Type-AnomalousLogGroup-ImpactEndTime"></a>
 The time the anomalous log events stopped.
Type: Timestamp
Required: No

 ** ImpactStartTime **   <a name="DevOpsGuru-Type-AnomalousLogGroup-ImpactStartTime"></a>
 The time the anomalous log events began. The impact start time indicates the time of the first log anomaly event that occurs.
Type: Timestamp
Required: No

 ** LogAnomalyShowcases **   <a name="DevOpsGuru-Type-AnomalousLogGroup-LogAnomalyShowcases"></a>
 The log anomalies in the log group. Each log anomaly displayed represents a cluster of similar anomalous log events.
Type: Array of [LogAnomalyShowcase](API_LogAnomalyShowcase.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** LogGroupName **   <a name="DevOpsGuru-Type-AnomalousLogGroup-LogGroupName"></a>
 The name of the CloudWatch log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** NumberOfLogLinesScanned **   <a name="DevOpsGuru-Type-AnomalousLogGroup-NumberOfLogLinesScanned"></a>
 The number of log lines that were scanned for anomalous log events.
Type: Integer
Required: No

## See Also
<a name="API_AnomalousLogGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/AnomalousLogGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/AnomalousLogGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/AnomalousLogGroup)
