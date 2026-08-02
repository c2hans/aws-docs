---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-associationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent AssociationConfiguration
<a name="aws-properties-wisdom-aiagent-associationconfiguration"></a>

The configuration for an Amazon Q in Connect Assistant Association.

## Syntax
<a name="aws-properties-wisdom-aiagent-associationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-associationconfiguration-syntax.json"></a>

```
{
  "[AssociationConfigurationData](#cfn-wisdom-aiagent-associationconfiguration-associationconfigurationdata)" : {{AssociationConfigurationData}},
  "[AssociationId](#cfn-wisdom-aiagent-associationconfiguration-associationid)" : {{String}},
  "[AssociationType](#cfn-wisdom-aiagent-associationconfiguration-associationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-associationconfiguration-syntax.yaml"></a>

```
  [AssociationConfigurationData](#cfn-wisdom-aiagent-associationconfiguration-associationconfigurationdata): {{
    AssociationConfigurationData}}
  [AssociationId](#cfn-wisdom-aiagent-associationconfiguration-associationid): {{String}}
  [AssociationType](#cfn-wisdom-aiagent-associationconfiguration-associationtype): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-associationconfiguration-properties"></a>

`AssociationConfigurationData`  <a name="cfn-wisdom-aiagent-associationconfiguration-associationconfigurationdata"></a>
A typed union of the data of the configuration for an Amazon Q in Connect Assistant Association.
*Required*: No
*Type*: [AssociationConfigurationData](aws-properties-wisdom-aiagent-associationconfigurationdata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociationId`  <a name="cfn-wisdom-aiagent-associationconfiguration-associationid"></a>
The identifier of the association for this Association Configuration.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociationType`  <a name="cfn-wisdom-aiagent-associationconfiguration-associationtype"></a>
The type of the association for this Association Configuration.
*Required*: No
*Type*: String
*Allowed values*: `KNOWLEDGE_BASE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
