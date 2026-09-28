---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessBeforeInvocationHook.html
---

# HarnessBeforeInvocationHook
<a name="API_HarnessBeforeInvocationHook"></a>

The configuration for a hook that runs before an invocation begins.

## Contents
<a name="API_HarnessBeforeInvocationHook_Contents"></a>

 ** name **   <a name="bedrockagentcorecontrol-Type-HarnessBeforeInvocationHook-name"></a>
The name of the hook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** target **   <a name="bedrockagentcorecontrol-Type-HarnessBeforeInvocationHook-target"></a>
The target that receives the hook event.
Type: [HarnessHookTarget](API_HarnessHookTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_HarnessBeforeInvocationHook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessBeforeInvocationHook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessBeforeInvocationHook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessBeforeInvocationHook)
