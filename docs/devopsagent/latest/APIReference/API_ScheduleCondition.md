---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ScheduleCondition.html
---

# ScheduleCondition
<a name="API_ScheduleCondition"></a>

Expression-based schedule condition. CreateTrigger callers using this condition supply expression and omit spec. Trigger responses always use this condition, include the persisted or derived expression, and also include spec when the trigger was created from a structured schedule.

## Contents
<a name="API_ScheduleCondition_Contents"></a>

 ** expression **   <a name="devopsagent-Type-ScheduleCondition-expression"></a>
EventBridge cron or rate expression. Required for existing request and response compatibility. For a structured schedule response, this is the expression derived by Backlog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** spec **   <a name="devopsagent-Type-ScheduleCondition-spec"></a>
Structured schedule source of truth (cron \| timeRange). On CreateTrigger supply exactly one of spec or expression. Present in responses together with the derived expression for structured triggers.
Type: [ScheduleSpec](API_ScheduleSpec.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ScheduleCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ScheduleCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ScheduleCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ScheduleCondition)
