---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-assistantassociation-associationdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AssistantAssociation AssociationData
<a name="aws-properties-wisdom-assistantassociation-associationdata"></a>

A union type that currently has a single argument, which is the knowledge base ID.

## Syntax
<a name="aws-properties-wisdom-assistantassociation-associationdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-assistantassociation-associationdata-syntax.json"></a>

```
{
  "[ExternalBedrockKnowledgeBaseConfig](#cfn-wisdom-assistantassociation-associationdata-externalbedrockknowledgebaseconfig)" : {{ExternalBedrockKnowledgeBaseConfig}},
  "[KnowledgeBaseId](#cfn-wisdom-assistantassociation-associationdata-knowledgebaseid)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-assistantassociation-associationdata-syntax.yaml"></a>

```
  [ExternalBedrockKnowledgeBaseConfig](#cfn-wisdom-assistantassociation-associationdata-externalbedrockknowledgebaseconfig): {{
    ExternalBedrockKnowledgeBaseConfig}}
  [KnowledgeBaseId](#cfn-wisdom-assistantassociation-associationdata-knowledgebaseid): {{String}}
```

## Properties
<a name="aws-properties-wisdom-assistantassociation-associationdata-properties"></a>

`ExternalBedrockKnowledgeBaseConfig`  <a name="cfn-wisdom-assistantassociation-associationdata-externalbedrockknowledgebaseconfig"></a>
Property description not available.
*Required*: No
*Type*: [ExternalBedrockKnowledgeBaseConfig](aws-properties-wisdom-assistantassociation-externalbedrockknowledgebaseconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KnowledgeBaseId`  <a name="cfn-wisdom-assistantassociation-associationdata-knowledgebaseid"></a>
The identifier of the knowledge base.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
