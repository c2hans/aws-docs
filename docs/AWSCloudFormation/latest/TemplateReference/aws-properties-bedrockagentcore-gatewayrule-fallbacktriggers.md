---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-fallbacktriggers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule FallbackTriggers
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktriggers"></a>

The conditions that trigger a fallback to the next target. A fallback occurs if the response matches any of the specified status codes or errors.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktriggers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktriggers-syntax.json"></a>

```
{
  "[Errors](#cfn-bedrockagentcore-gatewayrule-fallbacktriggers-errors)" : {{[ String, ... ]}},
  "[StatusCodes](#cfn-bedrockagentcore-gatewayrule-fallbacktriggers-statuscodes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktriggers-syntax.yaml"></a>

```
  [Errors](#cfn-bedrockagentcore-gatewayrule-fallbacktriggers-errors): {{
    - String}}
  [StatusCodes](#cfn-bedrockagentcore-gatewayrule-fallbacktriggers-statuscodes): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktriggers-properties"></a>

`Errors`  <a name="cfn-bedrockagentcore-gatewayrule-fallbacktriggers-errors"></a>
The errors that trigger a fallback. You can specify the following:
+ `CONNECTION_ERROR` – The gateway couldn't connect to the target because the connection was refused, reset, or timed out. The request didn't reach the target.
+ `FIRST_BYTE_TIMEOUT` – The target accepted the connection but didn't return the first byte of the response within `firstByteTimeoutMilliseconds`. The gateway abandons the request before any of the response reaches you.
+ `UNROUTABLE` – The gateway couldn't route the request to the target, for example because the target doesn't exist or doesn't support the request path. These errors don't count toward the circuit breaker.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusCodes`  <a name="cfn-bedrockagentcore-gatewayrule-fallbacktriggers-statuscodes"></a>
The HTTP status codes returned by the target that trigger a fallback. You can specify the following:
+ An exact status code – A three-digit code, such as `429`.
+ A class of status codes – The first digit followed by `XX`, such as `5XX`, which matches every code from 500 to 599.
Only 4XX and 5XX codes are supported. Throttling by the gateway itself doesn't trigger a fallback.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
