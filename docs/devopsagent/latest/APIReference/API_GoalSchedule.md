---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GoalSchedule.html
---

# GoalSchedule
<a name="API_GoalSchedule"></a>

Schedule configuration for goal evaluations

## Contents
<a name="API_GoalSchedule_Contents"></a>

 ** state **   <a name="devopsagent-Type-GoalSchedule-state"></a>
Whether the schedule is enabled or disabled
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** expression **   <a name="devopsagent-Type-GoalSchedule-expression"></a>
Schedule expression (e.g., 'rate(7 days)')
Type: String
Required: No

## See Also
<a name="API_GoalSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/GoalSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/GoalSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/GoalSchedule)
