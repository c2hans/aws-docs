---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BGW_MaintenanceStartTime.html
---

# MaintenanceStartTime
<a name="API_BGW_MaintenanceStartTime"></a>

This is your gateway's weekly maintenance start time including the day and time of the week. Note that values are in terms of the gateway's time zone. Can be weekly or monthly.

## Contents
<a name="API_BGW_MaintenanceStartTime_Contents"></a>

 ** HourOfDay **   <a name="Backup-Type-BGW_MaintenanceStartTime-HourOfDay"></a>
The hour component of the maintenance start time represented as *hh*, where *hh* is the hour (0 to 23). The hour of the day is in the time zone of the gateway.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: Yes

 ** MinuteOfHour **   <a name="Backup-Type-BGW_MaintenanceStartTime-MinuteOfHour"></a>
The minute component of the maintenance start time represented as *mm*, where *mm* is the minute (0 to 59). The minute of the hour is in the time zone of the gateway.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 59.
Required: Yes

 ** DayOfMonth **   <a name="Backup-Type-BGW_MaintenanceStartTime-DayOfMonth"></a>
The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month and 28 represents the last day of the month.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 31.
Required: No

 ** DayOfWeek **   <a name="Backup-Type-BGW_MaintenanceStartTime-DayOfWeek"></a>
An ordinal number between 0 and 6 that represents the day of the week, where 0 represents Sunday and 6 represents Saturday. The day of week is in the time zone of the gateway.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6.
Required: No

## See Also
<a name="API_BGW_MaintenanceStartTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/MaintenanceStartTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/MaintenanceStartTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/MaintenanceStartTime)
