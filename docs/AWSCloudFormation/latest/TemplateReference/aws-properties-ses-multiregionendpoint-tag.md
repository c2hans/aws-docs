---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-multiregionendpoint-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MultiRegionEndpoint Tag
<a name="aws-properties-ses-multiregionendpoint-tag"></a>

An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.

Each tag consists of a required *tag key* and an associated *tag value*, both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: \_ . : / = \+ -. The following additional restrictions apply to tags:
+ Tag keys and values are case sensitive.
+ For each associated resource, each tag key must be unique and it can have only one value.
+ The `aws:` prefix is reserved for use by AWS; you can’t use it in any tag keys or values that you define. In addition, you can't edit or remove tag keys or values that use this prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
+ You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.

## Syntax
<a name="aws-properties-ses-multiregionendpoint-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-multiregionendpoint-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ses-multiregionendpoint-tag-key)" : {{String}},
  "[Value](#cfn-ses-multiregionendpoint-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-multiregionendpoint-tag-syntax.yaml"></a>

```
  [Key](#cfn-ses-multiregionendpoint-tag-key): {{String}}
  [Value](#cfn-ses-multiregionendpoint-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ses-multiregionendpoint-tag-properties"></a>

`Key`  <a name="cfn-ses-multiregionendpoint-tag-key"></a>
One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ses-multiregionendpoint-tag-value"></a>
The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don't want a resource to have a specific tag value, don't specify a value for this parameter. If you don't specify a value, Amazon SES sets the value to an empty string.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
