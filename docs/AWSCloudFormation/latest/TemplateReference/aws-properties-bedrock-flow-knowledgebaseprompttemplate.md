---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-knowledgebaseprompttemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow KnowledgeBasePromptTemplate
<a name="aws-properties-bedrock-flow-knowledgebaseprompttemplate"></a>

Defines a custom prompt template for orchestrating the retrieval and generation process.

## Syntax
<a name="aws-properties-bedrock-flow-knowledgebaseprompttemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-knowledgebaseprompttemplate-syntax.json"></a>

```
{
  "[TextPromptTemplate](#cfn-bedrock-flow-knowledgebaseprompttemplate-textprompttemplate)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-knowledgebaseprompttemplate-syntax.yaml"></a>

```
  [TextPromptTemplate](#cfn-bedrock-flow-knowledgebaseprompttemplate-textprompttemplate): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-knowledgebaseprompttemplate-properties"></a>

`TextPromptTemplate`  <a name="cfn-bedrock-flow-knowledgebaseprompttemplate-textprompttemplate"></a>
The text of the prompt template.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
