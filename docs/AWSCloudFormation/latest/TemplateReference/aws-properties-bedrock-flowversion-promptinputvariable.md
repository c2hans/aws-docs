---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-promptinputvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion PromptInputVariable
<a name="aws-properties-bedrock-flowversion-promptinputvariable"></a>

Contains information about a variable in the prompt.

## Syntax
<a name="aws-properties-bedrock-flowversion-promptinputvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-promptinputvariable-syntax.json"></a>

```
{
  "[Name](#cfn-bedrock-flowversion-promptinputvariable-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-promptinputvariable-syntax.yaml"></a>

```
  [Name](#cfn-bedrock-flowversion-promptinputvariable-name): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-promptinputvariable-properties"></a>

`Name`  <a name="cfn-bedrock-flowversion-promptinputvariable-name"></a>
The name of the variable.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
