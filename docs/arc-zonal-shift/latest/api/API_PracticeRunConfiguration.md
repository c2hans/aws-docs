---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_PracticeRunConfiguration.html
---

# PracticeRunConfiguration
<a name="API_PracticeRunConfiguration"></a>

A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run. When a resource has a practice run configuration, ARC shifts traffic for the resource weekly for practice runs.

Practice runs are required for zonal autoshift. The zonal shifts that ARC starts for practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application.

You can update or delete a practice run configuration. Before you delete a practice run configuration, you must disable zonal autoshift for the resource. A practice run configuration is required when zonal autoshift is enabled.

## Contents
<a name="API_PracticeRunConfiguration_Contents"></a>

 ** outcomeAlarms **   <a name="zonalshift-Type-PracticeRunConfiguration-outcomeAlarms"></a>
 *Outcome alarms* for practice runs are alarms that you specify that end a practice run when one or more of the alarms is in an `ALARM` state.
Type: Array of [ControlCondition](API_ControlCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** allowedWindows **   <a name="zonalshift-Type-PracticeRunConfiguration-allowedWindows"></a>
An array of one or more windows of days and times that you can allow ARC to start practice runs for a resource.
For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: `Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00`.
The `allowedWindows` have to start and end on the same day. Windows that span multiple days aren't supported.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Fixed length of 19.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}`
Required: No

 ** blockedDates **   <a name="zonalshift-Type-PracticeRunConfiguration-blockedDates"></a>
An array of one or more dates that you can specify when AWS does not start practice runs for a resource.
Specify blocked dates, in UTC, in the format `YYYY-MM-DD`, separated by spaces.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Fixed length of 10.
Pattern: `[0-9]{4}-[0-9]{2}-[0-9]{2}`
Required: No

 ** blockedWindows **   <a name="zonalshift-Type-PracticeRunConfiguration-blockedWindows"></a>
An array of one or more windows of days and times that you can block ARC from starting practice runs for a resource.
Specify the blocked windows in UTC, using the format `DAY:HH:MM-DAY:HH:MM`, separated by spaces. For example, `MON:18:30-MON:19:30 TUE:18:30-TUE:19:30`.
The `blockedWindows` have to start and end on the same day. Windows that span multiple days aren't supported.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Fixed length of 19.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}-(Mon|Tue|Wed|Thu|Fri|Sat|Sun):[0-9]{2}:[0-9]{2}`
Required: No

 ** blockingAlarms **   <a name="zonalshift-Type-PracticeRunConfiguration-blockingAlarms"></a>
 *Blocking alarms* for practice runs are optional alarms that you can specify that block practice runs when one or more of the alarms is in an `ALARM` state.
Type: Array of [ControlCondition](API_ControlCondition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_PracticeRunConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/PracticeRunConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/PracticeRunConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/PracticeRunConfiguration)
