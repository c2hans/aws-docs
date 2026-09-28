---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessHookTarget.html
---

# HarnessHookTarget
<a name="API_HarnessHookTarget"></a>

The target that receives lifecycle hook events. Specify one target type.

## Contents
<a name="API_HarnessHookTarget_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** eventBridge **   <a name="bedrockagentcorecontrol-Type-HarnessHookTarget-eventBridge"></a>
An Amazon EventBridge hook target that sends the hook event without waiting for a response.
Type: [HarnessHookEventBridgeTarget](API_HarnessHookEventBridgeTarget.md) object
Required: No

 ** lambda **   <a name="bedrockagentcorecontrol-Type-HarnessHookTarget-lambda"></a>
A Lambda hook target that invokes an AWS Lambda function synchronously and waits for its response.
Type: [HarnessHookLambdaTarget](API_HarnessHookLambdaTarget.md) object
Required: No

 ** sns **   <a name="bedrockagentcorecontrol-Type-HarnessHookTarget-sns"></a>
An Amazon SNS hook target that publishes the hook event without waiting for a response.
Type: [HarnessHookSnsTarget](API_HarnessHookSnsTarget.md) object
Required: No

## See Also
<a name="API_HarnessHookTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessHookTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessHookTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessHookTarget)
