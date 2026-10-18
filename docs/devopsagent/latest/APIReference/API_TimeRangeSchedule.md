---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_TimeRangeSchedule.html
---

# TimeRangeSchedule
<a name="API_TimeRangeSchedule"></a>

Recurring time-of-day window in UTC. The service derives an EventBridge expression anchored at startAfter and a flexible-window width from the interval to startBefore. A startBefore earlier than startAfter wraps past midnight.

## Contents
<a name="API_TimeRangeSchedule_Contents"></a>

 ** recurrence **   <a name="devopsagent-Type-TimeRangeSchedule-recurrence"></a>
How the window recurs
Type: [Recurrence](API_Recurrence.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** startAfter **   <a name="devopsagent-Type-TimeRangeSchedule-startAfter"></a>
Earliest time of day the trigger may fire
Type: String
Length Constraints: Fixed length of 5.
Pattern: `([01]\d|2[0-3]):[0-5]\d`
Required: Yes

 ** startBefore **   <a name="devopsagent-Type-TimeRangeSchedule-startBefore"></a>
Latest time of day the trigger may fire
Type: String
Length Constraints: Fixed length of 5.
Pattern: `([01]\d|2[0-3]):[0-5]\d`
Required: Yes

## See Also
<a name="API_TimeRangeSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/TimeRangeSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/TimeRangeSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/TimeRangeSchedule)
