---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-placeindex-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::PlaceIndex Tag
<a name="aws-properties-location-placeindex-tag"></a>

<a name="aws-properties-location-placeindex-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Location::PlaceIndex](aws-resource-location-placeindex.md).

## Syntax
<a name="aws-properties-location-placeindex-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-placeindex-tag-syntax.json"></a>

```
{
  "[Key](#cfn-location-placeindex-tag-key)" : {{String}},
  "[Value](#cfn-location-placeindex-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-location-placeindex-tag-syntax.yaml"></a>

```
  [Key](#cfn-location-placeindex-tag-key): {{String}}
  [Value](#cfn-location-placeindex-tag-value): {{String}}
```

## Properties
<a name="aws-properties-location-placeindex-tag-properties"></a>

`Key`  <a name="cfn-location-placeindex-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-location-placeindex-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9 _=@:.+-/]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
