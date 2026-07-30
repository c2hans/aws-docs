---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-lambdainterceptorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway LambdaInterceptorConfiguration
<a name="aws-properties-bedrockagentcore-gateway-lambdainterceptorconfiguration"></a>

The lambda configuration for the interceptor

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-lambdainterceptorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-lambdainterceptorconfiguration-syntax.json"></a>

```
{
  "[Arn](#cfn-bedrockagentcore-gateway-lambdainterceptorconfiguration-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-lambdainterceptorconfiguration-syntax.yaml"></a>

```
  [Arn](#cfn-bedrockagentcore-gateway-lambdainterceptorconfiguration-arn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-lambdainterceptorconfiguration-properties"></a>

`Arn`  <a name="cfn-bedrockagentcore-gateway-lambdainterceptorconfiguration-arn"></a>
The arn of the lambda function to be invoked for the interceptor.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-]{1,20}:lambda:([a-z]{2}(-gov)?-[a-z]+-\d{1}):(\d{12}):function:([a-zA-Z0-9-_.]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
