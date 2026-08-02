---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowExecution.html
---

# MaintenanceWindowExecution
<a name="API_MaintenanceWindowExecution"></a>

Describes the information about an execution of a maintenance window.

## Contents
<a name="API_MaintenanceWindowExecution_Contents"></a>

 ** EndTime **   <a name="systemsmanager-Type-MaintenanceWindowExecution-EndTime"></a>
The time the execution finished.
Type: Timestamp
Required: No

 ** StartTime **   <a name="systemsmanager-Type-MaintenanceWindowExecution-StartTime"></a>
The time the execution started.
Type: Timestamp
Required: No

 ** Status **   <a name="systemsmanager-Type-MaintenanceWindowExecution-Status"></a>
The status of the execution.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESS | FAILED | TIMED_OUT | CANCELLING | CANCELLED | SKIPPED_OVERLAPPING`
Required: No

 ** StatusDetails **   <a name="systemsmanager-Type-MaintenanceWindowExecution-StatusDetails"></a>
The details explaining the status. Not available for all status values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Required: No

 ** WindowExecutionId **   <a name="systemsmanager-Type-MaintenanceWindowExecution-WindowExecutionId"></a>
The ID of the maintenance window execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: No

 ** WindowId **   <a name="systemsmanager-Type-MaintenanceWindowExecution-WindowId"></a>
The ID of the maintenance window.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: No

## See Also
<a name="API_MaintenanceWindowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowExecution)
