---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-promptflownoderesourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion PromptFlowNodeResourceConfiguration
<a name="aws-properties-bedrock-flowversion-promptflownoderesourceconfiguration"></a>

Contains configurations for a prompt from Prompt management to use in a node.

## Syntax
<a name="aws-properties-bedrock-flowversion-promptflownoderesourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-promptflownoderesourceconfiguration-syntax.json"></a>

```
{
  "[PromptArn](#cfn-bedrock-flowversion-promptflownoderesourceconfiguration-promptarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-promptflownoderesourceconfiguration-syntax.yaml"></a>

```
  [PromptArn](#cfn-bedrock-flowversion-promptflownoderesourceconfiguration-promptarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-promptflownoderesourceconfiguration-properties"></a>

`PromptArn`  <a name="cfn-bedrock-flowversion-promptflownoderesourceconfiguration-promptarn"></a>
The Amazon Resource Name (ARN) of the prompt from Prompt management.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
