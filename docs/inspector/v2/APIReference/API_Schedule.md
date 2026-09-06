---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Schedule.html
---

# Schedule
<a name="API_Schedule"></a>

A schedule.

## Contents
<a name="API_Schedule_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** daily **   <a name="inspector2-Type-Schedule-daily"></a>
The schedule's daily.
Type: [DailySchedule](API_DailySchedule.md) object
Required: No

 ** monthly **   <a name="inspector2-Type-Schedule-monthly"></a>
The schedule's monthly.
Type: [MonthlySchedule](API_MonthlySchedule.md) object
Required: No

 ** oneTime **   <a name="inspector2-Type-Schedule-oneTime"></a>
The schedule's one time.
Type: [OneTimeSchedule](API_OneTimeSchedule.md) object
Required: No

 ** weekly **   <a name="inspector2-Type-Schedule-weekly"></a>
The schedule's weekly.
Type: [WeeklySchedule](API_WeeklySchedule.md) object
Required: No

## See Also
<a name="API_Schedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Schedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Schedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Schedule)
