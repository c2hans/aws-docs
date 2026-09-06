---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftQueryEngineAwsDataCatalogStorageConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration"></a>

Contains configurations for storage in AWS Glue Data Catalog.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-syntax.json"></a>

```
{
  "[TableNames](#cfn-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-tablenames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-syntax.yaml"></a>

```
  [TableNames](#cfn-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-tablenames): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-properties"></a>

`TableNames`  <a name="cfn-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-tablenames"></a>
A list of names of the tables to use.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
