---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_FallbackTarget.html
---

# FallbackTarget
<a name="API_FallbackTarget"></a>

Specifies a target to send the request to when the previous target in the fallback chain fails. Includes the target name, the model to send, and the conditions that trigger a fallback from this target to the next one.

## Contents
<a name="API_FallbackTarget_Contents"></a>

 ** targetName **   <a name="bedrockagentcorecontrol-Type-FallbackTarget-targetName"></a>
The name of the gateway target to fall back to. The target must be an inference target.
Type: String
Pattern: `([0-9a-zA-Z][-]?){1,100}`
Required: Yes

 ** firstByteTimeoutMilliseconds **   <a name="bedrockagentcorecontrol-Type-FallbackTarget-firstByteTimeoutMilliseconds"></a>
The maximum time, in milliseconds, from sending the request to this target until the first byte of the response body arrives. This setting isn't inherited from the route. If you don't specify a value, no timeout is enforced.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 900000.
Required: No

 ** model **   <a name="bedrockagentcorecontrol-Type-FallbackTarget-model"></a>
The model ID to send to this fallback target. If you don't specify a model, the gateway sends the model from the original request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-._/@:]*`
Required: No

 ** triggerOn **   <a name="bedrockagentcorecontrol-Type-FallbackTarget-triggerOn"></a>
The status codes and errors from this target that cause the gateway to send the request to the next fallback target. This setting isn't inherited from the route. If you omit it, the gateway uses the default triggers: `5XX` status codes and the `CONNECTION_ERROR`, `FIRST_BYTE_TIMEOUT`, and `UNROUTABLE` errors.
Type: [FallbackTriggers](API_FallbackTriggers.md) object
Required: No

## See Also
<a name="API_FallbackTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/FallbackTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/FallbackTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/FallbackTarget)
