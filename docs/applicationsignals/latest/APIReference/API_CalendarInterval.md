---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CalendarInterval.html
---

# CalendarInterval
<a name="API_CalendarInterval"></a>

If the interval for this service level objective is a calendar interval, this structure contains the interval specifications.

## Contents
<a name="API_CalendarInterval_Contents"></a>

 ** Duration **   <a name="applicationsignals-Type-CalendarInterval-Duration"></a>
Specifies the duration of each calendar interval. For example, if `Duration` is `1` and `DurationUnit` is `MONTH`, each interval is one month, aligned with the calendar.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** DurationUnit **   <a name="applicationsignals-Type-CalendarInterval-DurationUnit"></a>
Specifies the calendar interval unit.
Type: String
Valid Values: `MINUTE | HOUR | DAY | MONTH`
Required: Yes

 ** StartTime **   <a name="applicationsignals-Type-CalendarInterval-StartTime"></a>
The date and time when you want the first interval to start. Be sure to choose a time that configures the intervals the way that you want. For example, if you want weekly intervals starting on Mondays at 6 a.m., be sure to specify a start time that is a Monday at 6 a.m.
When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
As soon as one calendar interval ends, another automatically begins.
Type: Timestamp
Required: Yes

## See Also
<a name="API_CalendarInterval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/CalendarInterval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/CalendarInterval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/CalendarInterval)
