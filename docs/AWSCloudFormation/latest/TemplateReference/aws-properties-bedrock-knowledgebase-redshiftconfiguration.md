---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftconfiguration"></a>

Contains configurations for an Amazon Redshift database. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftconfiguration-syntax.json"></a>

```
{
  "[QueryEngineConfiguration](#cfn-bedrock-knowledgebase-redshiftconfiguration-queryengineconfiguration)" : {{RedshiftQueryEngineConfiguration}},
  "[QueryGenerationConfiguration](#cfn-bedrock-knowledgebase-redshiftconfiguration-querygenerationconfiguration)" : {{QueryGenerationConfiguration}},
  "[StorageConfigurations](#cfn-bedrock-knowledgebase-redshiftconfiguration-storageconfigurations)" : {{[ RedshiftQueryEngineStorageConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftconfiguration-syntax.yaml"></a>

```
  [QueryEngineConfiguration](#cfn-bedrock-knowledgebase-redshiftconfiguration-queryengineconfiguration): {{
    RedshiftQueryEngineConfiguration}}
  [QueryGenerationConfiguration](#cfn-bedrock-knowledgebase-redshiftconfiguration-querygenerationconfiguration): {{
    QueryGenerationConfiguration}}
  [StorageConfigurations](#cfn-bedrock-knowledgebase-redshiftconfiguration-storageconfigurations): {{
    - RedshiftQueryEngineStorageConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftconfiguration-properties"></a>

`QueryEngineConfiguration`  <a name="cfn-bedrock-knowledgebase-redshiftconfiguration-queryengineconfiguration"></a>
Specifies configurations for an Amazon Redshift query engine.
*Required*: Yes
*Type*: [RedshiftQueryEngineConfiguration](aws-properties-bedrock-knowledgebase-redshiftqueryengineconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryGenerationConfiguration`  <a name="cfn-bedrock-knowledgebase-redshiftconfiguration-querygenerationconfiguration"></a>
Specifies configurations for generating queries.
*Required*: No
*Type*: [QueryGenerationConfiguration](aws-properties-bedrock-knowledgebase-querygenerationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageConfigurations`  <a name="cfn-bedrock-knowledgebase-redshiftconfiguration-storageconfigurations"></a>
Specifies configurations for Amazon Redshift database storage.
*Required*: Yes
*Type*: Array of [RedshiftQueryEngineStorageConfiguration](aws-properties-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
