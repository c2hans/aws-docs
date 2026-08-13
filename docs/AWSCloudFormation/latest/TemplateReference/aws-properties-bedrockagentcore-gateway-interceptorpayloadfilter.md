---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-interceptorpayloadfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway InterceptorPayloadFilter
<a name="aws-properties-bedrockagentcore-gateway-interceptorpayloadfilter"></a>

<a name="aws-properties-bedrockagentcore-gateway-interceptorpayloadfilter-description"></a>The `InterceptorPayloadFilter` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Gateway](aws-resource-bedrockagentcore-gateway.md).

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-interceptorpayloadfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-interceptorpayloadfilter-syntax.json"></a>

```
{
  "[Exclude](#cfn-bedrockagentcore-gateway-interceptorpayloadfilter-exclude)" : {{[ InterceptorPayloadExclusionSelector, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-interceptorpayloadfilter-syntax.yaml"></a>

```
  [Exclude](#cfn-bedrockagentcore-gateway-interceptorpayloadfilter-exclude): {{
    - InterceptorPayloadExclusionSelector}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-interceptorpayloadfilter-properties"></a>

`Exclude`  <a name="cfn-bedrockagentcore-gateway-interceptorpayloadfilter-exclude"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [InterceptorPayloadExclusionSelector](aws-properties-bedrockagentcore-gateway-interceptorpayloadexclusionselector.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
