---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase HierarchicalChunkingLevelConfiguration
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration"></a>

Token settings for each layer.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration-syntax.json"></a>

```
{
  "[MaxTokens](#cfn-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration-maxtokens)" : {{Number}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration-syntax.yaml"></a>

```
  [MaxTokens](#cfn-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration-maxtokens): {{Number}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration-properties"></a>

`MaxTokens`  <a name="cfn-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration-maxtokens"></a>
The maximum number of tokens that a chunk can contain in this layer.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
