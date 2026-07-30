---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-interceptorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway InterceptorConfiguration
<a name="aws-properties-bedrockagentcore-gateway-interceptorconfiguration"></a>

The interceptor configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-interceptorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-interceptorconfiguration-syntax.json"></a>

```
{
  "[Lambda](#cfn-bedrockagentcore-gateway-interceptorconfiguration-lambda)" : {{LambdaInterceptorConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-interceptorconfiguration-syntax.yaml"></a>

```
  [Lambda](#cfn-bedrockagentcore-gateway-interceptorconfiguration-lambda): {{
    LambdaInterceptorConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-interceptorconfiguration-properties"></a>

`Lambda`  <a name="cfn-bedrockagentcore-gateway-interceptorconfiguration-lambda"></a>
The details of the lambda function used for the interceptor.
*Required*: Yes
*Type*: [LambdaInterceptorConfiguration](aws-properties-bedrockagentcore-gateway-lambdainterceptorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
