---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-neptuneanalyticsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase NeptuneAnalyticsConfiguration
<a name="aws-properties-bedrock-knowledgebase-neptuneanalyticsconfiguration"></a>

Contains details about the storage configuration of the knowledge base in Amazon Neptune Analytics. For more information, see [Create a vector index in Amazon Neptune Analytics](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-neptune.html).

## Syntax
<a name="aws-properties-bedrock-knowledgebase-neptuneanalyticsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-neptuneanalyticsconfiguration-syntax.json"></a>

```
{
  "[FieldMapping](#cfn-bedrock-knowledgebase-neptuneanalyticsconfiguration-fieldmapping)" : {{NeptuneAnalyticsFieldMapping}},
  "[GraphArn](#cfn-bedrock-knowledgebase-neptuneanalyticsconfiguration-grapharn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-neptuneanalyticsconfiguration-syntax.yaml"></a>

```
  [FieldMapping](#cfn-bedrock-knowledgebase-neptuneanalyticsconfiguration-fieldmapping): {{
    NeptuneAnalyticsFieldMapping}}
  [GraphArn](#cfn-bedrock-knowledgebase-neptuneanalyticsconfiguration-grapharn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-neptuneanalyticsconfiguration-properties"></a>

`FieldMapping`  <a name="cfn-bedrock-knowledgebase-neptuneanalyticsconfiguration-fieldmapping"></a>
Contains the names of the fields to which to map information about the vector store.
*Required*: Yes
*Type*: [NeptuneAnalyticsFieldMapping](aws-properties-bedrock-knowledgebase-neptuneanalyticsfieldmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GraphArn`  <a name="cfn-bedrock-knowledgebase-neptuneanalyticsconfiguration-grapharn"></a>
The Amazon Resource Name (ARN) of the Neptune Analytics vector store.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):neptune-graph:[a-zA-Z0-9-]*:[0-9]{12}:graph\/g-[a-zA-Z0-9]{10}$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
