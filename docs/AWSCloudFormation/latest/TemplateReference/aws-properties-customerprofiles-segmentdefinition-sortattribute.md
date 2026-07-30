---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-sortattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition SortAttribute
<a name="aws-properties-customerprofiles-segmentdefinition-sortattribute"></a>

<a name="aws-properties-customerprofiles-segmentdefinition-sortattribute-description"></a>The `SortAttribute` property type specifies Property description not available. for an [AWS::CustomerProfiles::SegmentDefinition](aws-resource-customerprofiles-segmentdefinition.md).

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-sortattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-sortattribute-syntax.json"></a>

```
{
  "[DataType](#cfn-customerprofiles-segmentdefinition-sortattribute-datatype)" : {{String}},
  "[Name](#cfn-customerprofiles-segmentdefinition-sortattribute-name)" : {{String}},
  "[Order](#cfn-customerprofiles-segmentdefinition-sortattribute-order)" : {{String}},
  "[Type](#cfn-customerprofiles-segmentdefinition-sortattribute-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-sortattribute-syntax.yaml"></a>

```
  [DataType](#cfn-customerprofiles-segmentdefinition-sortattribute-datatype): {{String}}
  [Name](#cfn-customerprofiles-segmentdefinition-sortattribute-name): {{String}}
  [Order](#cfn-customerprofiles-segmentdefinition-sortattribute-order): {{String}}
  [Type](#cfn-customerprofiles-segmentdefinition-sortattribute-type): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-sortattribute-properties"></a>

`DataType`  <a name="cfn-customerprofiles-segmentdefinition-sortattribute-datatype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `STRING | NUMBER | DATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-customerprofiles-segmentdefinition-sortattribute-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Order`  <a name="cfn-customerprofiles-segmentdefinition-sortattribute-order"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ASC | DESC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-customerprofiles-segmentdefinition-sortattribute-type"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PROFILE | CALCULATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
