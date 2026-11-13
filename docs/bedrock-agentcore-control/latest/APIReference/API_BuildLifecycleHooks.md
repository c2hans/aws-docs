---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_BuildLifecycleHooks.html
---

# BuildLifecycleHooks
<a name="API_BuildLifecycleHooks"></a>

The lifecycle hooks that run when you create or update the AgentCore Runtime, before any sessions are created.

## Contents
<a name="API_BuildLifecycleHooks_Contents"></a>

 ** warmup **   <a name="bedrockagentcorecontrol-Type-BuildLifecycleHooks-warmup"></a>
The hook that warms up your agent before any sessions are created. Use this hook to load the resources that your sessions need, such as models, libraries, or caches. Your hook must complete within 120 seconds.
Type: [LifecycleHook](API_LifecycleHook.md) object
Required: No

## See Also
<a name="API_BuildLifecycleHooks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/BuildLifecycleHooks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/BuildLifecycleHooks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/BuildLifecycleHooks)
