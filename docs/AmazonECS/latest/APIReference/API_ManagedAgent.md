---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedAgent.html
---

# ManagedAgent
<a name="API_ManagedAgent"></a>

Details about the managed agent status for the container.

## Contents
<a name="API_ManagedAgent_Contents"></a>

 ** lastStartedAt **   <a name="ECS-Type-ManagedAgent-lastStartedAt"></a>
The Unix timestamp for the time when the managed agent was last started.
Type: Timestamp
Required: No

 ** lastStatus **   <a name="ECS-Type-ManagedAgent-lastStatus"></a>
The last known status of the managed agent.
Type: String
Required: No

 ** name **   <a name="ECS-Type-ManagedAgent-name"></a>
The name of the managed agent. When the execute command feature is turned on, the managed agent name is `ExecuteCommandAgent`.
Type: String
Valid Values: `ExecuteCommandAgent`
Required: No

 ** reason **   <a name="ECS-Type-ManagedAgent-reason"></a>
The reason for why the managed agent is in the state it is in.
Type: String
Required: No

## See Also
<a name="API_ManagedAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedAgent)
