---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-interceptorinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway InterceptorInputConfiguration
<a name="aws-properties-bedrockagentcore-gateway-interceptorinputconfiguration"></a>

The input configuration of the interceptor.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-interceptorinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-interceptorinputconfiguration-syntax.json"></a>

```
{
  "[PassRequestHeaders](#cfn-bedrockagentcore-gateway-interceptorinputconfiguration-passrequestheaders)" : {{Boolean}},
  "[PayloadFilter](#cfn-bedrockagentcore-gateway-interceptorinputconfiguration-payloadfilter)" : {{InterceptorPayloadFilter}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-interceptorinputconfiguration-syntax.yaml"></a>

```
  [PassRequestHeaders](#cfn-bedrockagentcore-gateway-interceptorinputconfiguration-passrequestheaders): {{Boolean}}
  [PayloadFilter](#cfn-bedrockagentcore-gateway-interceptorinputconfiguration-payloadfilter): {{
    InterceptorPayloadFilter}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-interceptorinputconfiguration-properties"></a>

`PassRequestHeaders`  <a name="cfn-bedrockagentcore-gateway-interceptorinputconfiguration-passrequestheaders"></a>
Indicates whether to pass request headers as input into the interceptor. When set to true, request headers will be passed.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PayloadFilter`  <a name="cfn-bedrockagentcore-gateway-interceptorinputconfiguration-payloadfilter"></a>
Property description not available.
*Required*: No
*Type*: [InterceptorPayloadFilter](aws-properties-bedrockagentcore-gateway-interceptorpayloadfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
