---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessAfterToolCallHook.html
---

# HarnessAfterToolCallHook
<a name="API_HarnessAfterToolCallHook"></a>

The configuration for a hook that runs after a tool call completes.

## Contents
<a name="API_HarnessAfterToolCallHook_Contents"></a>

 ** name **   <a name="bedrockagentcorecontrol-Type-HarnessAfterToolCallHook-name"></a>
The name of the hook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** target **   <a name="bedrockagentcorecontrol-Type-HarnessAfterToolCallHook-target"></a>
The target that receives the hook event.
Type: [HarnessHookTarget](API_HarnessHookTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_HarnessAfterToolCallHook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessAfterToolCallHook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessAfterToolCallHook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessAfterToolCallHook)
