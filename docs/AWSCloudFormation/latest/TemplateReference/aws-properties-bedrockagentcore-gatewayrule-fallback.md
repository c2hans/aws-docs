---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-fallback.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule Fallback
<a name="aws-properties-bedrockagentcore-gatewayrule-fallback"></a>

The fallback configuration for a route to an inference target. Defines an ordered list of fallback targets to try when a request to the route's target fails, and the conditions that trigger a fallback. A fallback can occur only before the gateway sends the first byte of the response to the caller. After a streaming response starts, the gateway doesn't fall back.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-fallback-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-fallback-syntax.json"></a>

```
{
  "[CircuitBreaker](#cfn-bedrockagentcore-gatewayrule-fallback-circuitbreaker)" : {{CircuitBreakerConfiguration}},
  "[FirstByteTimeoutMilliseconds](#cfn-bedrockagentcore-gatewayrule-fallback-firstbytetimeoutmilliseconds)" : {{Integer}},
  "[TargetFallback](#cfn-bedrockagentcore-gatewayrule-fallback-targetfallback)" : {{[ FallbackTarget, ... ]}},
  "[TriggerOn](#cfn-bedrockagentcore-gatewayrule-fallback-triggeron)" : {{FallbackTriggers}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-fallback-syntax.yaml"></a>

```
  [CircuitBreaker](#cfn-bedrockagentcore-gatewayrule-fallback-circuitbreaker): {{
    CircuitBreakerConfiguration}}
  [FirstByteTimeoutMilliseconds](#cfn-bedrockagentcore-gatewayrule-fallback-firstbytetimeoutmilliseconds): {{Integer}}
  [TargetFallback](#cfn-bedrockagentcore-gatewayrule-fallback-targetfallback): {{
    - FallbackTarget}}
  [TriggerOn](#cfn-bedrockagentcore-gatewayrule-fallback-triggeron): {{
    FallbackTriggers}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-fallback-properties"></a>

`CircuitBreaker`  <a name="cfn-bedrockagentcore-gatewayrule-fallback-circuitbreaker"></a>
Specifies whether the gateway temporarily stops sending your requests to a failing target. The circuit breaker tracks each combination of target and model separately. With the circuit breaker enabled, the gateway skips one or more targets and models that fail repeatedly, and your requests go to the next target in the chain. The gateway always tries the last remaining target in the chain. The gateway enables the circuit breaker by default.
*Required*: No
*Type*: [CircuitBreakerConfiguration](aws-properties-bedrockagentcore-gatewayrule-circuitbreakerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirstByteTimeoutMilliseconds`  <a name="cfn-bedrockagentcore-gatewayrule-fallback-firstbytetimeoutmilliseconds"></a>
The maximum time, in milliseconds, from sending the request to the route's target until the first byte of the response body arrives. If the time expires, the gateway abandons the request and treats it as a `FIRST_BYTE_TIMEOUT` error. If you don't specify a value, no timeout is enforced.
*Required*: No
*Type*: Integer
*Minimum*: `50`
*Maximum*: `900000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetFallback`  <a name="cfn-bedrockagentcore-gatewayrule-fallback-targetfallback"></a>
The ordered list of fallback targets. The gateway tries each target in order until a response doesn't match that target's triggers, and returns that response to the caller. If every target fails, the gateway returns the last response. You can specify up to two fallback targets. Each combination of target and model, including the route's target, can appear only once.
*Required*: Yes
*Type*: Array of [FallbackTarget](aws-properties-bedrockagentcore-gatewayrule-fallbacktarget.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TriggerOn`  <a name="cfn-bedrockagentcore-gatewayrule-fallback-triggeron"></a>
The status codes and errors from the route's target that cause the gateway to send the request to the first fallback target. If you omit `triggerOn`, the gateway falls back on `5XX` status codes and on the `CONNECTION_ERROR`, `FIRST_BYTE_TIMEOUT`, and `UNROUTABLE` errors. If you specify `triggerOn`, only the status codes and errors that you list trigger a fallback.
*Required*: No
*Type*: [FallbackTriggers](aws-properties-bedrockagentcore-gatewayrule-fallbacktriggers.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
