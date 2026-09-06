---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_SyncSchedule.html
---

# SyncSchedule
<a name="API_agent_SyncSchedule"></a>

The recurring schedule on which a managed knowledge base connector automatically syncs its data source. Specify exactly one of `daily`, `weekly`, or `monthly`.

## Contents
<a name="API_agent_SyncSchedule_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** daily **   <a name="bedrock-Type-agent_SyncSchedule-daily"></a>
A daily sync that runs once a day at a system-chosen off-peak time. The run time is not configurable.
Type: [DailySchedule](API_agent_DailySchedule.md) object
Required: No

 ** monthly **   <a name="bedrock-Type-agent_SyncSchedule-monthly"></a>
A monthly sync that runs once a month on the specified day of the month.
Type: [MonthlySchedule](API_agent_MonthlySchedule.md) object
Required: No

 ** weekly **   <a name="bedrock-Type-agent_SyncSchedule-weekly"></a>
A weekly sync that runs once a week on the specified day of the week.
Type: [WeeklySchedule](API_agent_WeeklySchedule.md) object
Required: No

## See Also
<a name="API_agent_SyncSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/SyncSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/SyncSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/SyncSchedule)
