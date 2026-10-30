---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_Fallback.html
---

# Fallback
<a name="API_Fallback"></a>

The fallback configuration for a route to an inference target. Defines an ordered list of fallback targets to try when a request to the route's target fails, and the conditions that trigger a fallback. A fallback can occur only before the gateway sends the first byte of the response to the caller. After a streaming response starts, the gateway doesn't fall back.

## Contents
<a name="API_Fallback_Contents"></a>

 ** targetFallback **   <a name="bedrockagentcorecontrol-Type-Fallback-targetFallback"></a>
The ordered list of fallback targets. The gateway tries each target in order until a response doesn't match that target's triggers, and returns that response to the caller. If every target fails, the gateway returns the last response. You can specify up to two fallback targets. Each combination of target and model, including the route's target, can appear only once.
Type: Array of [FallbackTarget](API_FallbackTarget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** circuitBreaker **   <a name="bedrockagentcorecontrol-Type-Fallback-circuitBreaker"></a>
Specifies whether the gateway temporarily stops sending your requests to a failing target. The circuit breaker tracks each combination of target and model separately. With the circuit breaker enabled, the gateway skips one or more targets and models that fail repeatedly, and your requests go to the next target in the chain. The gateway always tries the last remaining target in the chain. The gateway enables the circuit breaker by default.
Type: [CircuitBreakerConfiguration](API_CircuitBreakerConfiguration.md) object
Required: No

 ** firstByteTimeoutMilliseconds **   <a name="bedrockagentcorecontrol-Type-Fallback-firstByteTimeoutMilliseconds"></a>
The maximum time, in milliseconds, from sending the request to the route's target until the first byte of the response body arrives. If the time expires, the gateway abandons the request and treats it as a `FIRST_BYTE_TIMEOUT` error. If you don't specify a value, no timeout is enforced.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 900000.
Required: No

 ** triggerOn **   <a name="bedrockagentcorecontrol-Type-Fallback-triggerOn"></a>
The status codes and errors from the route's target that cause the gateway to send the request to the first fallback target. If you omit `triggerOn`, the gateway falls back on `5XX` status codes and on the `CONNECTION_ERROR`, `FIRST_BYTE_TIMEOUT`, and `UNROUTABLE` errors. If you specify `triggerOn`, only the status codes and errors that you list trigger a fallback.
Type: [FallbackTriggers](API_FallbackTriggers.md) object
Required: No

## See Also
<a name="API_Fallback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Fallback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Fallback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Fallback)
