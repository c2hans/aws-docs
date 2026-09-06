---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowIdentity.html
---

# MaintenanceWindowIdentity
<a name="API_MaintenanceWindowIdentity"></a>

Information about the maintenance window.

## Contents
<a name="API_MaintenanceWindowIdentity_Contents"></a>

 ** Cutoff **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-Cutoff"></a>
The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: No

 ** Description **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-Description"></a>
A description of the maintenance window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Duration **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-Duration"></a>
The duration of the maintenance window in hours.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: No

 ** Enabled **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-Enabled"></a>
Indicates whether the maintenance window is enabled.
Type: Boolean
Required: No

 ** EndDate **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-EndDate"></a>
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.
Type: String
Required: No

 ** Name **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-Name"></a>
The name of the maintenance window.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** NextExecutionTime **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-NextExecutionTime"></a>
The next time the maintenance window will actually run, taking into account any specified times for the maintenance window to become active or inactive.
Type: String
Required: No

 ** Schedule **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-Schedule"></a>
The schedule of the maintenance window in the form of a cron or rate expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ScheduleOffset **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-ScheduleOffset"></a>
The number of days to wait to run a maintenance window after the scheduled cron expression date and time.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.
Required: No

 ** ScheduleTimezone **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-ScheduleTimezone"></a>
The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.
Type: String
Required: No

 ** StartDate **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-StartDate"></a>
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active.
Type: String
Required: No

 ** WindowId **   <a name="systemsmanager-Type-MaintenanceWindowIdentity-WindowId"></a>
The ID of the maintenance window.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: No

## See Also
<a name="API_MaintenanceWindowIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowIdentity)
