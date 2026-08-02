---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-geofencecollection-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::GeofenceCollection Tag
<a name="aws-properties-location-geofencecollection-tag"></a>

Applies one or more tags to the geofence collection. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.

## Syntax
<a name="aws-properties-location-geofencecollection-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-geofencecollection-tag-syntax.json"></a>

```
{
  "[Key](#cfn-location-geofencecollection-tag-key)" : {{String}},
  "[Value](#cfn-location-geofencecollection-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-location-geofencecollection-tag-syntax.yaml"></a>

```
  [Key](#cfn-location-geofencecollection-tag-key): {{String}}
  [Value](#cfn-location-geofencecollection-tag-value): {{String}}
```

## Properties
<a name="aws-properties-location-geofencecollection-tag-properties"></a>

`Key`  <a name="cfn-location-geofencecollection-tag-key"></a>
The key of the tag that is associated with the specified geofence collection.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-location-geofencecollection-tag-value"></a>
The value of the tag that is associated with the specified geofence collection.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9 _=@:.+-/]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
