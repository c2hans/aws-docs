---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ScheduledInstanceRecurrenceRequest.html
---

# ScheduledInstanceRecurrenceRequest
<a name="API_ScheduledInstanceRecurrenceRequest"></a>

Describes the recurring schedule for a Scheduled Instance.

## Contents
<a name="API_ScheduledInstanceRecurrenceRequest_Contents"></a>

 ** Frequency **
The frequency (`Daily`, `Weekly`, or `Monthly`).
Type: String
Required: No

 ** Interval **
The interval quantity. The interval unit depends on the value of `Frequency`. For example, every 2 weeks or every 2 months.
Type: Integer
Required: No

 ** OccurrenceDay.N **
The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday). You can't specify this value with a daily schedule. If the occurrence is relative to the end of the month, you can specify only a single day.
Type: Array of integers
Required: No

 ** OccurrenceRelativeToEnd **
Indicates whether the occurrence is relative to the end of the specified week or month. You can't specify this value with a daily schedule.
Type: Boolean
Required: No

 ** OccurrenceUnit **
The unit for `OccurrenceDays` (`DayOfWeek` or `DayOfMonth`). This value is required for a monthly schedule. You can't specify `DayOfWeek` with a weekly schedule. You can't specify this value with a daily schedule.
Type: String
Required: No

## See Also
<a name="API_ScheduledInstanceRecurrenceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ScheduledInstanceRecurrenceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ScheduledInstanceRecurrenceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ScheduledInstanceRecurrenceRequest)
