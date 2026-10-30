---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-fallbacktarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule FallbackTarget
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktarget"></a>

Specifies a target to send the request to when the previous target in the fallback chain fails. Includes the target name, the model to send, and the conditions that trigger a fallback from this target to the next one.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktarget-syntax.json"></a>

```
{
  "[FirstByteTimeoutMilliseconds](#cfn-bedrockagentcore-gatewayrule-fallbacktarget-firstbytetimeoutmilliseconds)" : {{Integer}},
  "[Model](#cfn-bedrockagentcore-gatewayrule-fallbacktarget-model)" : {{String}},
  "[TargetName](#cfn-bedrockagentcore-gatewayrule-fallbacktarget-targetname)" : {{String}},
  "[TriggerOn](#cfn-bedrockagentcore-gatewayrule-fallbacktarget-triggeron)" : {{FallbackTriggers}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktarget-syntax.yaml"></a>

```
  [FirstByteTimeoutMilliseconds](#cfn-bedrockagentcore-gatewayrule-fallbacktarget-firstbytetimeoutmilliseconds): {{Integer}}
  [Model](#cfn-bedrockagentcore-gatewayrule-fallbacktarget-model): {{String}}
  [TargetName](#cfn-bedrockagentcore-gatewayrule-fallbacktarget-targetname): {{String}}
  [TriggerOn](#cfn-bedrockagentcore-gatewayrule-fallbacktarget-triggeron): {{
    FallbackTriggers}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-fallbacktarget-properties"></a>

`FirstByteTimeoutMilliseconds`  <a name="cfn-bedrockagentcore-gatewayrule-fallbacktarget-firstbytetimeoutmilliseconds"></a>
The maximum time, in milliseconds, from sending the request to this target until the first byte of the response body arrives. This setting isn't inherited from the route. If you don't specify a value, no timeout is enforced.
*Required*: No
*Type*: Integer
*Minimum*: `50`
*Maximum*: `900000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Model`  <a name="cfn-bedrockagentcore-gatewayrule-fallbacktarget-model"></a>
The model ID to send to this fallback target. If you don't specify a model, the gateway sends the model from the original request.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-._/@:]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetName`  <a name="cfn-bedrockagentcore-gatewayrule-fallbacktarget-targetname"></a>
The name of the gateway target to fall back to. The target must be an inference target.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TriggerOn`  <a name="cfn-bedrockagentcore-gatewayrule-fallbacktarget-triggeron"></a>
The status codes and errors from this target that cause the gateway to send the request to the next fallback target. This setting isn't inherited from the route. If you omit it, the gateway uses the default triggers: `5XX` status codes and the `CONNECTION_ERROR`, `FIRST_BYTE_TIMEOUT`, and `UNROUTABLE` errors.
*Required*: No
*Type*: [FallbackTriggers](aws-properties-bedrockagentcore-gatewayrule-fallbacktriggers.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
