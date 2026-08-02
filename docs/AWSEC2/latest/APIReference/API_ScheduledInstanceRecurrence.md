---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ScheduledInstanceRecurrence.html
---

# ScheduledInstanceRecurrence
<a name="API_ScheduledInstanceRecurrence"></a>

Describes the recurring schedule for a Scheduled Instance.

## Contents
<a name="API_ScheduledInstanceRecurrence_Contents"></a>

 ** frequency **
The frequency (`Daily`, `Weekly`, or `Monthly`).
Type: String
Required: No

 ** interval **
The interval quantity. The interval unit depends on the value of `frequency`. For example, every 2 weeks or every 2 months.
Type: Integer
Required: No

 ** OccurrenceDaySet.N **
The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday).
Type: Array of integers
Required: No

 ** occurrenceRelativeToEnd **
Indicates whether the occurrence is relative to the end of the specified week or month.
Type: Boolean
Required: No

 ** occurrenceUnit **
The unit for `occurrenceDaySet` (`DayOfWeek` or `DayOfMonth`).
Type: String
Required: No

## See Also
<a name="API_ScheduledInstanceRecurrence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ScheduledInstanceRecurrence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ScheduledInstanceRecurrence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ScheduledInstanceRecurrence)
