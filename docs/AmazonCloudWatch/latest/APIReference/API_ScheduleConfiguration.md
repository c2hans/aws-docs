---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ScheduleConfiguration.html
---

# ScheduleConfiguration
<a name="API_ScheduleConfiguration"></a>

Contains the schedule expression and time-range offsets that define when a scheduled query runs and what time range each execution covers.

## Contents
<a name="API_ScheduleConfiguration_Contents"></a>

 ** ScheduleExpression **   <a name="ACW-Type-ScheduleConfiguration-ScheduleExpression"></a>
The schedule expression that defines how often the underlying CloudWatch Logs scheduled query runs. Specify a `rate()` expression, for example `rate(5 minutes)`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** EndTimeOffset **   <a name="ACW-Type-ScheduleConfiguration-EndTimeOffset"></a>
The offset, in seconds, before the scheduled execution time at which the query time range ends. Must be non-negative and less than `StartTimeOffset`. The default is 0.
Type: Long
Required: No

 ** StartTimeOffset **   <a name="ACW-Type-ScheduleConfiguration-StartTimeOffset"></a>
The offset, in seconds, before the scheduled execution time at which the query time range begins. For example, an offset of 360 (6 minutes) on a query running at 12:05:00 starts the query time range at 11:59:00.
Type: Long
Required: No

## See Also
<a name="API_ScheduleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ScheduleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ScheduleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ScheduleConfiguration)
