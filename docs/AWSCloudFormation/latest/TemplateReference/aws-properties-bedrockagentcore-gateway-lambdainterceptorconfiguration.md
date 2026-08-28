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
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:lambda:([a-z]{2}(-gov)?-[a-z]+-\d{1}):(\d{12}):function:([a-zA-Z0-9-_.]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
