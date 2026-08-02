---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RecurrencePattern.html
---

# RecurrencePattern
<a name="API_RecurrencePattern"></a>

Specifies the detailed pattern for event recurrence. Use this to define complex scheduling rules such as "every 2nd Tuesday of the month" or "every 3 months on the 15th".

## Contents
<a name="API_RecurrencePattern_Contents"></a>

 ** Frequency **   <a name="connect-Type-RecurrencePattern-Frequency"></a>
Defines how often the pattern repeats. This is the base unit for the recurrence schedule and works in conjunction with the Interval field to determine the exact repetition sequence.
Type: String
Valid Values: `WEEKLY | MONTHLY | YEARLY`
Required: Yes

 ** Interval **   <a name="connect-Type-RecurrencePattern-Interval"></a>
Specifies the number of frequency units between each occurrence. Must be a positive integer.
 Examples: To repeat every week, set Interval=1 with WEEKLY frequency. To repeat every two months, set Interval=2 with MONTHLY frequency.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.
Required: Yes

 ** ByMonth **   <a name="connect-Type-RecurrencePattern-ByMonth"></a>
Specifies which month the event should occur in (1-12, where 1=January, 12=December). Used with YEARLY frequency to schedule events in specific month.
Note: It does not accept multiple values in the same list
Type: Array of integers
Valid Range: Minimum value of 1. Maximum value of 12.
Required: No

 ** ByMonthDay **   <a name="connect-Type-RecurrencePattern-ByMonthDay"></a>
Specifies which day of the month the event should occur on (1-31). Used with MONTHLY or YEARLY frequency to schedule events on specific date within a month.
 Examples: [15] for events on the 15th of each month, [-1] for events on the last day of month.
Note: It does not accept multiple values in the same list. If a specified day doesn't exist in a particular month (e.g., day 31 in February), the event will be skipped for that month. This field cannot be used simultaneously with ByWeekdayOccurrence as they represent different scheduling approaches (specific dates vs. relative weekday positions).
Type: Array of integers
Valid Range: Minimum value of -1. Maximum value of 31.
Required: No

 ** ByWeekdayOccurrence **   <a name="connect-Type-RecurrencePattern-ByWeekdayOccurrence"></a>
Specifies which occurrence of a weekday within the month the event should occur on. Must be used with MONTHLY or YEARLY frequency.
Example: 2 corresponds to second occurrence of the weekday in the month. -1 corresponds to last occurrence of the weekday in the month
The weekday itself is specified separately in the HoursOfOperationConfig. Example: To schedule the recurring event for the 2nd Thursday of April every year, set ByWeekdayOccurrence=[2], Day=THURSDAY, ByMonth=[4], Frequency: YEARLY and INTERVAL=1.
Type: Array of integers
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Range: Minimum value of -1. Maximum value of 4.
Required: No

## See Also
<a name="API_RecurrencePattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RecurrencePattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RecurrencePattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RecurrencePattern)
