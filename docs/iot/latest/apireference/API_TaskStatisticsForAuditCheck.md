---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TaskStatisticsForAuditCheck.html
---

# TaskStatisticsForAuditCheck
<a name="API_TaskStatisticsForAuditCheck"></a>

Provides summary counts of how many tasks for findings are in a particular state. This information is included in the response from DescribeAuditMitigationActionsTask.

## Contents
<a name="API_TaskStatisticsForAuditCheck_Contents"></a>

 ** canceledFindingsCount **   <a name="iot-Type-TaskStatisticsForAuditCheck-canceledFindingsCount"></a>
The number of findings to which the mitigation action task was canceled when applied.
Type: Long
Required: No

 ** failedFindingsCount **   <a name="iot-Type-TaskStatisticsForAuditCheck-failedFindingsCount"></a>
The number of findings for which at least one of the actions failed when applied.
Type: Long
Required: No

 ** skippedFindingsCount **   <a name="iot-Type-TaskStatisticsForAuditCheck-skippedFindingsCount"></a>
The number of findings skipped because of filter conditions provided in the parameters to the command.
Type: Long
Required: No

 ** succeededFindingsCount **   <a name="iot-Type-TaskStatisticsForAuditCheck-succeededFindingsCount"></a>
The number of findings for which all mitigation actions succeeded when applied.
Type: Long
Required: No

 ** totalFindingsCount **   <a name="iot-Type-TaskStatisticsForAuditCheck-totalFindingsCount"></a>
The total number of findings to which a task is being applied.
Type: Long
Required: No

## See Also
<a name="API_TaskStatisticsForAuditCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TaskStatisticsForAuditCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TaskStatisticsForAuditCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TaskStatisticsForAuditCheck)
