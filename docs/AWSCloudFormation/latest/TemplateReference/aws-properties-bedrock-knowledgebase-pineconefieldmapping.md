---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-pineconefieldmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase PineconeFieldMapping
<a name="aws-properties-bedrock-knowledgebase-pineconefieldmapping"></a>

Contains the names of the fields to which to map information about the vector store.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-pineconefieldmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-pineconefieldmapping-syntax.json"></a>

```
{
  "[MetadataField](#cfn-bedrock-knowledgebase-pineconefieldmapping-metadatafield)" : {{String}},
  "[TextField](#cfn-bedrock-knowledgebase-pineconefieldmapping-textfield)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-pineconefieldmapping-syntax.yaml"></a>

```
  [MetadataField](#cfn-bedrock-knowledgebase-pineconefieldmapping-metadatafield): {{String}}
  [TextField](#cfn-bedrock-knowledgebase-pineconefieldmapping-textfield): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-pineconefieldmapping-properties"></a>

`MetadataField`  <a name="cfn-bedrock-knowledgebase-pineconefieldmapping-metadatafield"></a>
The name of the field in which Amazon Bedrock stores metadata about the vector store.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TextField`  <a name="cfn-bedrock-knowledgebase-pineconefieldmapping-textfield"></a>
The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
