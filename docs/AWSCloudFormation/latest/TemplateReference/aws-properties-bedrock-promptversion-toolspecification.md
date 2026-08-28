---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-toolspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion ToolSpecification
<a name="aws-properties-bedrock-promptversion-toolspecification"></a>

The specification for the tool. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-promptversion-toolspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-toolspecification-syntax.json"></a>

```
{
  "[Description](#cfn-bedrock-promptversion-toolspecification-description)" : {{String}},
  "[InputSchema](#cfn-bedrock-promptversion-toolspecification-inputschema)" : {{ToolInputSchema}},
  "[Name](#cfn-bedrock-promptversion-toolspecification-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-toolspecification-syntax.yaml"></a>

```
  [Description](#cfn-bedrock-promptversion-toolspecification-description): {{String}}
  [InputSchema](#cfn-bedrock-promptversion-toolspecification-inputschema): {{
    ToolInputSchema}}
  [Name](#cfn-bedrock-promptversion-toolspecification-name): {{String}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-toolspecification-properties"></a>

`Description`  <a name="cfn-bedrock-promptversion-toolspecification-description"></a>
The description for the tool.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSchema`  <a name="cfn-bedrock-promptversion-toolspecification-inputschema"></a>
The input schema for the tool in JSON format.
*Required*: Yes
*Type*: [ToolInputSchema](aws-properties-bedrock-promptversion-toolinputschema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-promptversion-toolspecification-name"></a>
The name for the tool.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
