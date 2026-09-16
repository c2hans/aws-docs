---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-fielddefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType FieldDefinition
<a name="aws-properties-glue-connectiontype-fielddefinition"></a>

<a name="aws-properties-glue-connectiontype-fielddefinition-description"></a>The `FieldDefinition` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-fielddefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-fielddefinition-syntax.json"></a>

```
{
  "[FieldDataType](#cfn-glue-connectiontype-fielddefinition-fielddatatype)" : {{String}},
  "[FilterOverrides](#cfn-glue-connectiontype-fielddefinition-filteroverrides)" : {{FilterOverrides}},
  "[IsNullable](#cfn-glue-connectiontype-fielddefinition-isnullable)" : {{Boolean}},
  "[IsOrderable](#cfn-glue-connectiontype-fielddefinition-isorderable)" : {{Boolean}},
  "[IsPartitionable](#cfn-glue-connectiontype-fielddefinition-ispartitionable)" : {{Boolean}},
  "[IsQueryable](#cfn-glue-connectiontype-fielddefinition-isqueryable)" : {{Boolean}},
  "[Name](#cfn-glue-connectiontype-fielddefinition-name)" : {{String}},
  "[ResponseDateFormat](#cfn-glue-connectiontype-fielddefinition-responsedateformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-fielddefinition-syntax.yaml"></a>

```
  [FieldDataType](#cfn-glue-connectiontype-fielddefinition-fielddatatype): {{String}}
  [FilterOverrides](#cfn-glue-connectiontype-fielddefinition-filteroverrides): {{
    FilterOverrides}}
  [IsNullable](#cfn-glue-connectiontype-fielddefinition-isnullable): {{Boolean}}
  [IsOrderable](#cfn-glue-connectiontype-fielddefinition-isorderable): {{Boolean}}
  [IsPartitionable](#cfn-glue-connectiontype-fielddefinition-ispartitionable): {{Boolean}}
  [IsQueryable](#cfn-glue-connectiontype-fielddefinition-isqueryable): {{Boolean}}
  [Name](#cfn-glue-connectiontype-fielddefinition-name): {{String}}
  [ResponseDateFormat](#cfn-glue-connectiontype-fielddefinition-responsedateformat): {{String}}
```

## Properties
<a name="aws-properties-glue-connectiontype-fielddefinition-properties"></a>

`FieldDataType`  <a name="cfn-glue-connectiontype-fielddefinition-fielddatatype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `INT | SMALLINT | BIGINT | FLOAT | LONG | DATE | BOOLEAN | MAP | ARRAY | STRING | TIMESTAMP | DECIMAL | BYTE | SHORT | DOUBLE | STRUCT | BINARY | UNION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterOverrides`  <a name="cfn-glue-connectiontype-fielddefinition-filteroverrides"></a>
Property description not available.
*Required*: No
*Type*: [FilterOverrides](aws-properties-glue-connectiontype-filteroverrides.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsNullable`  <a name="cfn-glue-connectiontype-fielddefinition-isnullable"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsOrderable`  <a name="cfn-glue-connectiontype-fielddefinition-isorderable"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsPartitionable`  <a name="cfn-glue-connectiontype-fielddefinition-ispartitionable"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsQueryable`  <a name="cfn-glue-connectiontype-fielddefinition-isqueryable"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-glue-connectiontype-fielddefinition-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResponseDateFormat`  <a name="cfn-glue-connectiontype-fielddefinition-responsedateformat"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
