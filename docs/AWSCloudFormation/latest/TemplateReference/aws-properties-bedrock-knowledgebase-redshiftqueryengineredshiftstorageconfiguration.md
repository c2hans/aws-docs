---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftQueryEngineRedshiftStorageConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration"></a>

Contains configurations for storage in Amazon Redshift.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration-syntax.json"></a>

```
{
  "[DatabaseName](#cfn-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration-databasename)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration-syntax.yaml"></a>

```
  [DatabaseName](#cfn-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration-databasename): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration-properties"></a>

`DatabaseName`  <a name="cfn-bedrock-knowledgebase-redshiftqueryengineredshiftstorageconfiguration-databasename"></a>
The name of the Amazon Redshift database.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
