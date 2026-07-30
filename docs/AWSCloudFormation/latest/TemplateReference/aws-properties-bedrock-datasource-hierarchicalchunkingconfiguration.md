---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-hierarchicalchunkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource HierarchicalChunkingConfiguration
<a name="aws-properties-bedrock-datasource-hierarchicalchunkingconfiguration"></a>

Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.

You configure the number of tokens to overlap, or repeat across adjacent chunks. For example, if you set overlap tokens to 60, the last 60 tokens in the first chunk are also included at the beginning of the second chunk. For each layer, you must also configure the maximum number of tokens in a chunk.

## Syntax
<a name="aws-properties-bedrock-datasource-hierarchicalchunkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-hierarchicalchunkingconfiguration-syntax.json"></a>

```
{
  "[LevelConfigurations](#cfn-bedrock-datasource-hierarchicalchunkingconfiguration-levelconfigurations)" : {{[ HierarchicalChunkingLevelConfiguration, ... ]}},
  "[OverlapTokens](#cfn-bedrock-datasource-hierarchicalchunkingconfiguration-overlaptokens)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-hierarchicalchunkingconfiguration-syntax.yaml"></a>

```
  [LevelConfigurations](#cfn-bedrock-datasource-hierarchicalchunkingconfiguration-levelconfigurations): {{
    - HierarchicalChunkingLevelConfiguration}}
  [OverlapTokens](#cfn-bedrock-datasource-hierarchicalchunkingconfiguration-overlaptokens): {{Integer}}
```

## Properties
<a name="aws-properties-bedrock-datasource-hierarchicalchunkingconfiguration-properties"></a>

`LevelConfigurations`  <a name="cfn-bedrock-datasource-hierarchicalchunkingconfiguration-levelconfigurations"></a>
Token settings for each layer.
*Required*: Yes
*Type*: Array of [HierarchicalChunkingLevelConfiguration](aws-properties-bedrock-datasource-hierarchicalchunkinglevelconfiguration.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OverlapTokens`  <a name="cfn-bedrock-datasource-hierarchicalchunkingconfiguration-overlaptokens"></a>
The number of tokens to repeat across chunks in the same layer.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
