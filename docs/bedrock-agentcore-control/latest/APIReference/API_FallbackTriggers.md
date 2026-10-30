---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_FallbackTriggers.html
---

# FallbackTriggers
<a name="API_FallbackTriggers"></a>

The conditions that trigger a fallback to the next target. A fallback occurs if the response matches any of the specified status codes or errors.

## Contents
<a name="API_FallbackTriggers_Contents"></a>

 ** errors **   <a name="bedrockagentcorecontrol-Type-FallbackTriggers-errors"></a>
The errors that trigger a fallback. You can specify the following:
+  `CONNECTION_ERROR` – The gateway couldn't connect to the target because the connection was refused, reset, or timed out. The request didn't reach the target.
+  `FIRST_BYTE_TIMEOUT` – The target accepted the connection but didn't return the first byte of the response within `firstByteTimeoutMilliseconds`. The gateway abandons the request before any of the response reaches you.
+  `UNROUTABLE` – The gateway couldn't route the request to the target, for example because the target doesn't exist or doesn't support the request path. These errors don't count toward the circuit breaker.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `CONNECTION_ERROR | FIRST_BYTE_TIMEOUT | UNROUTABLE`
Required: No

 ** statusCodes **   <a name="bedrockagentcorecontrol-Type-FallbackTriggers-statusCodes"></a>
The HTTP status codes returned by the target that trigger a fallback. You can specify the following:
+ An exact status code – A three-digit code, such as `429`.
+ A class of status codes – The first digit followed by `XX`, such as `5XX`, which matches every code from 500 to 599.
Only 4XX and 5XX codes are supported. Throttling by the gateway itself doesn't trigger a fallback.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `[4-5]([0-9]{2}|XX)`
Required: No

## See Also
<a name="API_FallbackTriggers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/FallbackTriggers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/FallbackTriggers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/FallbackTriggers)
