---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ScheduleSpec.html
---

# ScheduleSpec
<a name="API_ScheduleSpec"></a>

Structured schedule specification. Select exactly one schedule form.

## Contents
<a name="API_ScheduleSpec_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cron **   <a name="devopsagent-Type-ScheduleSpec-cron"></a>
Runs on an EventBridge cron or rate cadence
Type: [CronSchedule](API_CronSchedule.md) object
Required: No

 ** timeRange **   <a name="devopsagent-Type-ScheduleSpec-timeRange"></a>
Runs within a recurring time-of-day window
Type: [TimeRangeSchedule](API_TimeRangeSchedule.md) object
Required: No

## See Also
<a name="API_ScheduleSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ScheduleSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ScheduleSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ScheduleSpec)
