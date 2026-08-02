---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Schedule.html
---

# Schedule
<a name="API_Schedule"></a>

A scheduling object using a `cron` statement to schedule an event.

## Contents
<a name="API_Schedule_Contents"></a>

 ** ScheduleExpression **   <a name="Glue-Type-Schedule-ScheduleExpression"></a>
A `cron` expression used to specify the schedule (see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
Type: String
Required: No

 ** State **   <a name="Glue-Type-Schedule-State"></a>
The state of the schedule.
Type: String
Valid Values: `SCHEDULED | NOT_SCHEDULED | TRANSITIONING`
Required: No

## See Also
<a name="API_Schedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Schedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Schedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Schedule)
