---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-rerankingmetadataselectivemodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow RerankingMetadataSelectiveModeConfiguration
<a name="aws-properties-bedrock-flow-rerankingmetadataselectivemodeconfiguration"></a>

Configuration for selectively including or excluding metadata fields during the reranking process. This allows you to control which metadata attributes are considered when reordering search results.

## Syntax
<a name="aws-properties-bedrock-flow-rerankingmetadataselectivemodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-rerankingmetadataselectivemodeconfiguration-syntax.json"></a>

```
{
  "[FieldsToExclude](#cfn-bedrock-flow-rerankingmetadataselectivemodeconfiguration-fieldstoexclude)" : {{[ FieldForReranking, ... ]}},
  "[FieldsToInclude](#cfn-bedrock-flow-rerankingmetadataselectivemodeconfiguration-fieldstoinclude)" : {{[ FieldForReranking, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-rerankingmetadataselectivemodeconfiguration-syntax.yaml"></a>

```
  [FieldsToExclude](#cfn-bedrock-flow-rerankingmetadataselectivemodeconfiguration-fieldstoexclude): {{
    - FieldForReranking}}
  [FieldsToInclude](#cfn-bedrock-flow-rerankingmetadataselectivemodeconfiguration-fieldstoinclude): {{
    - FieldForReranking}}
```

## Properties
<a name="aws-properties-bedrock-flow-rerankingmetadataselectivemodeconfiguration-properties"></a>

`FieldsToExclude`  <a name="cfn-bedrock-flow-rerankingmetadataselectivemodeconfiguration-fieldstoexclude"></a>
A list of metadata field names to explicitly exclude from the reranking process. All metadata fields except these will be considered when reordering search results. This parameter cannot be used together with fieldsToInclude.
*Required*: No
*Type*: Array of [FieldForReranking](aws-properties-bedrock-flow-fieldforreranking.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldsToInclude`  <a name="cfn-bedrock-flow-rerankingmetadataselectivemodeconfiguration-fieldstoinclude"></a>
A list of metadata field names to explicitly include in the reranking process. Only these fields will be considered when reordering search results. This parameter cannot be used together with fieldsToExclude.
*Required*: No
*Type*: Array of [FieldForReranking](aws-properties-bedrock-flow-fieldforreranking.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
