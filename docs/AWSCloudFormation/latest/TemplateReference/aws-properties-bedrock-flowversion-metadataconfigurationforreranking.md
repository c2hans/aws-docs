---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-metadataconfigurationforreranking.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion MetadataConfigurationForReranking
<a name="aws-properties-bedrock-flowversion-metadataconfigurationforreranking"></a>

Configuration for how metadata should be used during the reranking process in Knowledge Base vector searches. This determines which metadata fields are included or excluded when reordering search results.

## Syntax
<a name="aws-properties-bedrock-flowversion-metadataconfigurationforreranking-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-metadataconfigurationforreranking-syntax.json"></a>

```
{
  "[SelectionMode](#cfn-bedrock-flowversion-metadataconfigurationforreranking-selectionmode)" : {{String}},
  "[SelectiveModeConfiguration](#cfn-bedrock-flowversion-metadataconfigurationforreranking-selectivemodeconfiguration)" : {{RerankingMetadataSelectiveModeConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-metadataconfigurationforreranking-syntax.yaml"></a>

```
  [SelectionMode](#cfn-bedrock-flowversion-metadataconfigurationforreranking-selectionmode): {{String}}
  [SelectiveModeConfiguration](#cfn-bedrock-flowversion-metadataconfigurationforreranking-selectivemodeconfiguration): {{
    RerankingMetadataSelectiveModeConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-metadataconfigurationforreranking-properties"></a>

`SelectionMode`  <a name="cfn-bedrock-flowversion-metadataconfigurationforreranking-selectionmode"></a>
The mode for selecting which metadata fields to include in the reranking process. Valid values are ALL (use all available metadata fields) or SELECTIVE (use only specified fields).
*Required*: Yes
*Type*: String
*Allowed values*: `SELECTIVE | ALL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectiveModeConfiguration`  <a name="cfn-bedrock-flowversion-metadataconfigurationforreranking-selectivemodeconfiguration"></a>
Configuration for selective mode, which allows you to explicitly include or exclude specific metadata fields during reranking. This is only used when selectionMode is set to SELECTIVE.
*Required*: No
*Type*: [RerankingMetadataSelectiveModeConfiguration](aws-properties-bedrock-flowversion-rerankingmetadataselectivemodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
