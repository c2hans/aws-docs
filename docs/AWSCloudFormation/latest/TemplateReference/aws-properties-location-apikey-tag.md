---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-apikey-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::APIKey Tag
<a name="aws-properties-location-apikey-tag"></a>

Applies one or more tags to the API key. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.

## Syntax
<a name="aws-properties-location-apikey-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-apikey-tag-syntax.json"></a>

```
{
  "[Key](#cfn-location-apikey-tag-key)" : {{String}},
  "[Value](#cfn-location-apikey-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-location-apikey-tag-syntax.yaml"></a>

```
  [Key](#cfn-location-apikey-tag-key): {{String}}
  [Value](#cfn-location-apikey-tag-value): {{String}}
```

## Properties
<a name="aws-properties-location-apikey-tag-properties"></a>

`Key`  <a name="cfn-location-apikey-tag-key"></a>
The key value/string of an API key. This value is used when making API calls to authorize the call. For example, see [GetMapGlyphs](https://docs.aws.amazon.com/location/latest/APIReference/API_GetMapGlyphs.html).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-location-apikey-tag-value"></a>
The value of the tag that is associated with the specified API key.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9 _=@:.+-/]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
