---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_MaintenanceStartTime.html
---

# MaintenanceStartTime
<a name="API_MaintenanceStartTime"></a>

This is your gateway's weekly maintenance start time including the day and time of the week. Note that values are in terms of the gateway's time zone. Can be weekly or monthly.

## Contents
<a name="API_MaintenanceStartTime_Contents"></a>

 ** HourOfDay **   <a name="bgw-Type-MaintenanceStartTime-HourOfDay"></a>
The hour component of the maintenance start time represented as *hh*, where *hh* is the hour (0 to 23). The hour of the day is in the time zone of the gateway.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: Yes

 ** MinuteOfHour **   <a name="bgw-Type-MaintenanceStartTime-MinuteOfHour"></a>
The minute component of the maintenance start time represented as *mm*, where *mm* is the minute (0 to 59). The minute of the hour is in the time zone of the gateway.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 59.
Required: Yes

 ** DayOfMonth **   <a name="bgw-Type-MaintenanceStartTime-DayOfMonth"></a>
The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month and 28 represents the last day of the month.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 31.
Required: No

 ** DayOfWeek **   <a name="bgw-Type-MaintenanceStartTime-DayOfWeek"></a>
An ordinal number between 0 and 6 that represents the day of the week, where 0 represents Sunday and 6 represents Saturday. The day of week is in the time zone of the gateway.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6.
Required: No

## See Also
<a name="API_MaintenanceStartTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/MaintenanceStartTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/MaintenanceStartTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/MaintenanceStartTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Backup gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bgw` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
