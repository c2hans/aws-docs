---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessHookEventBridgeTarget.html
---

# HarnessHookEventBridgeTarget
<a name="API_HarnessHookEventBridgeTarget"></a>

The configuration for an Amazon EventBridge hook target.

## Contents
<a name="API_HarnessHookEventBridgeTarget_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-HarnessHookEventBridgeTarget-arn"></a>
The ARN of the Amazon EventBridge event bus to send hook events to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+`
Required: Yes

## See Also
<a name="API_HarnessHookEventBridgeTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessHookEventBridgeTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessHookEventBridgeTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessHookEventBridgeTarget)
