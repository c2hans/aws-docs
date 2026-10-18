---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Recurrence.html
---

# Recurrence
<a name="API_Recurrence"></a>

Recurrence cadence for a time-range schedule

## Contents
<a name="API_Recurrence_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** daily **   <a name="devopsagent-Type-Recurrence-daily"></a>
The window recurs every day
Type: [DailyRecurrence](API_DailyRecurrence.md) object
Required: No

 ** monthly **   <a name="devopsagent-Type-Recurrence-monthly"></a>
The window recurs once per month
Type: [MonthlyRecurrence](API_MonthlyRecurrence.md) object
Required: No

 ** weekly **   <a name="devopsagent-Type-Recurrence-weekly"></a>
The window recurs once per week
Type: [WeeklyRecurrence](API_WeeklyRecurrence.md) object
Required: No

## See Also
<a name="API_Recurrence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Recurrence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Recurrence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Recurrence)
