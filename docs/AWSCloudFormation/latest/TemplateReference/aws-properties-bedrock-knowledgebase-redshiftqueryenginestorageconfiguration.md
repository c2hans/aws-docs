---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftQueryEngineStorageConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration"></a>

Contains configurations for Amazon Redshift data storage. Specify the data storage service to use in the `type` field and include the corresponding field. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-syntax.json"></a>

```
{
  "[AwsDataCatalogConfiguration](#cfn-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-awsdatacatalogconfiguration)" : {{RedshiftQueryEngineAwsDataCatalogStorageConfiguration}},
  "[RedshiftConfiguration](#cfn-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-redshiftconfiguration)" : {{RedshiftQueryEngineRedshiftStorageConfiguration}},
  "[Type](#cfn-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-syntax.yaml"></a>

```
  [AwsDataCatalogConfiguration](#cfn-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-awsdatacatalogconfiguration): {{
    RedshiftQueryEngineAwsDataCatalogStorageConfiguration}}
  [RedshiftConfiguration](#cfn-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-redshiftconfiguration): {{
    RedshiftQueryEngineRedshiftStorageConfiguration}}
  [Type](#cfn-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-properties"></a>

`AwsDataCatalogConfiguration`  <a name="cfn-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-awsdatacatalogconfiguration"></a>
Specifies configurations for storage in AWS Glue Data Catalog.
*Required*: No
*Type*: [RedshiftQueryEngineAwsDataCatalogStorageConfiguration](aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RedshiftConfiguration`  <a name="cfn-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-redshiftconfiguration"></a>
Specifies configurations for storage in Amazon Redshift.
*Required*: No
*Type*: [RedshiftQueryEngineRedshiftStorageConfiguration](aws-properties-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-bedrock-knowledgebase-redshiftqueryenginestorageconfiguration-type"></a>
The data storage service to use.
*Required*: Yes
*Type*: String
*Allowed values*: `REDSHIFT | AWS_DATA_CATALOG`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
