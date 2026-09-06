---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-entity-datatype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Entity DataType
<a name="aws-properties-iottwinmaker-entity-datatype"></a>

The entity data type.

## Syntax
<a name="aws-properties-iottwinmaker-entity-datatype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-entity-datatype-syntax.json"></a>

```
{
  "[AllowedValues](#cfn-iottwinmaker-entity-datatype-allowedvalues)" : {{[ DataValue, ... ]}},
  "[NestedType](#cfn-iottwinmaker-entity-datatype-nestedtype)" : {{DataType}},
  "[Relationship](#cfn-iottwinmaker-entity-datatype-relationship)" : {{Relationship}},
  "[Type](#cfn-iottwinmaker-entity-datatype-type)" : {{String}},
  "[UnitOfMeasure](#cfn-iottwinmaker-entity-datatype-unitofmeasure)" : {{String}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-entity-datatype-syntax.yaml"></a>

```
  [AllowedValues](#cfn-iottwinmaker-entity-datatype-allowedvalues): {{
    - DataValue}}
  [NestedType](#cfn-iottwinmaker-entity-datatype-nestedtype): {{
    DataType}}
  [Relationship](#cfn-iottwinmaker-entity-datatype-relationship): {{
    Relationship}}
  [Type](#cfn-iottwinmaker-entity-datatype-type): {{String}}
  [UnitOfMeasure](#cfn-iottwinmaker-entity-datatype-unitofmeasure): {{String}}
```

## Properties
<a name="aws-properties-iottwinmaker-entity-datatype-properties"></a>

`AllowedValues`  <a name="cfn-iottwinmaker-entity-datatype-allowedvalues"></a>
The allowed values.
*Required*: No
*Type*: Array of [DataValue](aws-properties-iottwinmaker-entity-datavalue.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NestedType`  <a name="cfn-iottwinmaker-entity-datatype-nestedtype"></a>
The nested type.
*Required*: No
*Type*: [DataType](#aws-properties-iottwinmaker-entity-datatype)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Relationship`  <a name="cfn-iottwinmaker-entity-datatype-relationship"></a>
The relationship.
*Required*: No
*Type*: [Relationship](aws-properties-iottwinmaker-entity-relationship.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iottwinmaker-entity-datatype-type"></a>
The entity type.
*Required*: No
*Type*: String
*Allowed values*: `RELATIONSHIP | STRING | LONG | BOOLEAN | INTEGER | DOUBLE | LIST | MAP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnitOfMeasure`  <a name="cfn-iottwinmaker-entity-datatype-unitofmeasure"></a>
The unit of measure.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
