---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase HierarchicalChunkingConfiguration
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration"></a>

Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration-syntax.json"></a>

```
{
  "[LevelConfigurations](#cfn-wisdom-knowledgebase-hierarchicalchunkingconfiguration-levelconfigurations)" : {{[ HierarchicalChunkingLevelConfiguration, ... ]}},
  "[OverlapTokens](#cfn-wisdom-knowledgebase-hierarchicalchunkingconfiguration-overlaptokens)" : {{Number}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration-syntax.yaml"></a>

```
  [LevelConfigurations](#cfn-wisdom-knowledgebase-hierarchicalchunkingconfiguration-levelconfigurations): {{
    - HierarchicalChunkingLevelConfiguration}}
  [OverlapTokens](#cfn-wisdom-knowledgebase-hierarchicalchunkingconfiguration-overlaptokens): {{Number}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration-properties"></a>

`LevelConfigurations`  <a name="cfn-wisdom-knowledgebase-hierarchicalchunkingconfiguration-levelconfigurations"></a>
Token settings for each layer.
*Required*: Yes
*Type*: Array of [HierarchicalChunkingLevelConfiguration](aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverlapTokens`  <a name="cfn-wisdom-knowledgebase-hierarchicalchunkingconfiguration-overlaptokens"></a>
The number of tokens to repeat across chunks in the same layer.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
