---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_TriggerCondition.html
---

# TriggerCondition
<a name="API_TriggerCondition"></a>

Defines how a Trigger fires.

## Contents
<a name="API_TriggerCondition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** schedule **   <a name="devopsagent-Type-TriggerCondition-schedule"></a>
Schedule-based firing condition. On CreateTrigger supply exactly one of the schedule condition's expression or spec.
Type: [ScheduleCondition](API_ScheduleCondition.md) object
Required: No

## See Also
<a name="API_TriggerCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/TriggerCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/TriggerCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/TriggerCondition)
