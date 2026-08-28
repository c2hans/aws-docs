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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
