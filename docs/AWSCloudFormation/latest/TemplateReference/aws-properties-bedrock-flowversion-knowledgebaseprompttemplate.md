---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-knowledgebaseprompttemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion KnowledgeBasePromptTemplate
<a name="aws-properties-bedrock-flowversion-knowledgebaseprompttemplate"></a>

Defines a custom prompt template for orchestrating the retrieval and generation process.

## Syntax
<a name="aws-properties-bedrock-flowversion-knowledgebaseprompttemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-knowledgebaseprompttemplate-syntax.json"></a>

```
{
  "[TextPromptTemplate](#cfn-bedrock-flowversion-knowledgebaseprompttemplate-textprompttemplate)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-knowledgebaseprompttemplate-syntax.yaml"></a>

```
  [TextPromptTemplate](#cfn-bedrock-flowversion-knowledgebaseprompttemplate-textprompttemplate): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-knowledgebaseprompttemplate-properties"></a>

`TextPromptTemplate`  <a name="cfn-bedrock-flowversion-knowledgebaseprompttemplate-textprompttemplate"></a>
The text of the prompt template.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
