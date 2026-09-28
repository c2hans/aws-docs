---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessHook.html
---

# HarnessHook
<a name="API_HarnessHook"></a>

A lifecycle hook configuration. Specify one hook type.

## Contents
<a name="API_HarnessHook_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** afterInvocation **   <a name="bedrockagentcorecontrol-Type-HarnessHook-afterInvocation"></a>
A hook that runs after an invocation completes.
Type: [HarnessAfterInvocationHook](API_HarnessAfterInvocationHook.md) object
Required: No

 ** afterToolCall **   <a name="bedrockagentcorecontrol-Type-HarnessHook-afterToolCall"></a>
A hook that runs after a tool call completes.
Type: [HarnessAfterToolCallHook](API_HarnessAfterToolCallHook.md) object
Required: No

 ** beforeInvocation **   <a name="bedrockagentcorecontrol-Type-HarnessHook-beforeInvocation"></a>
A hook that runs before an invocation begins.
Type: [HarnessBeforeInvocationHook](API_HarnessBeforeInvocationHook.md) object
Required: No

 ** beforeToolCall **   <a name="bedrockagentcorecontrol-Type-HarnessHook-beforeToolCall"></a>
A hook that runs before the agent calls a tool.
Type: [HarnessBeforeToolCallHook](API_HarnessBeforeToolCallHook.md) object
Required: No

## See Also
<a name="API_HarnessHook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessHook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessHook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessHook)
