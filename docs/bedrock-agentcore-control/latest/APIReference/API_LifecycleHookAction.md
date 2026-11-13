---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_LifecycleHookAction.html
---

# LifecycleHookAction
<a name="API_LifecycleHookAction"></a>

The action that a lifecycle hook runs. Specify exactly one member. Currently, `httpPost` is the only supported action.

## Contents
<a name="API_LifecycleHookAction_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** httpPost **   <a name="bedrockagentcorecontrol-Type-LifecycleHookAction-httpPost"></a>
Sends an HTTP `POST` request to your agent's container on the specified port and path to run the hook. The hook succeeds if your container returns a `2xx` response. The hook fails if your container returns any other response or doesn't respond before the hook times out.
Type: [HttpPostLifecycleHookAction](API_HttpPostLifecycleHookAction.md) object
Required: No

## See Also
<a name="API_LifecycleHookAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LifecycleHookAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LifecycleHookAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LifecycleHookAction)
