---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Trigger.html
---

# Trigger
<a name="API_Trigger"></a>

A Trigger fires on a schedule and invokes an agent

## Contents
<a name="API_Trigger_Contents"></a>

 ** action **   <a name="devopsagent-Type-Trigger-action"></a>
The action this Trigger performs when it fires
Type: JSON value
Required: Yes

 ** agentSpaceId **   <a name="devopsagent-Type-Trigger-agentSpaceId"></a>
The agent space this Trigger belongs to
Type: String
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

 ** condition **   <a name="devopsagent-Type-Trigger-condition"></a>
The condition that fires this Trigger
Type: [TriggerCondition](API_TriggerCondition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-Trigger-createdAt"></a>
Timestamp when this Trigger was created
Type: Timestamp
Required: Yes

 ** status **   <a name="devopsagent-Type-Trigger-status"></a>
The status of this Trigger
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** triggerId **   <a name="devopsagent-Type-Trigger-triggerId"></a>
The unique identifier for this Trigger
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** type **   <a name="devopsagent-Type-Trigger-type"></a>
How this Trigger fires
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-Trigger-updatedAt"></a>
Timestamp when this Trigger was last updated
Type: Timestamp
Required: Yes

## See Also
<a name="API_Trigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Trigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Trigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Trigger)
