---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-capacityreservation-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::CapacityReservation Tag
<a name="aws-properties-athena-capacityreservation-tag"></a>

A label that you assign to a resource. Athena resources include workgroups, data catalogs, and capacity reservations. Each tag consists of a key and an optional value, both of which you define. For example, you can use tags to categorize Athena resources by purpose, owner, or environment. Use a consistent set of tag keys to make it easier to search and filter the resources in your account. For best practices, see [Tagging Best Practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html). Tag keys can be from 1 to 128 UTF-8 Unicode characters, and tag values can be from 0 to 256 UTF-8 Unicode characters. Tags can use letters and numbers representable in UTF-8, and the following characters: \+ - = . \_ : / @. Tag keys and values are case-sensitive. Tag keys must be unique per resource. If you specify more than one tag, separate them by commas.

## Syntax
<a name="aws-properties-athena-capacityreservation-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-capacityreservation-tag-syntax.json"></a>

```
{
  "[Key](#cfn-athena-capacityreservation-tag-key)" : {{String}},
  "[Value](#cfn-athena-capacityreservation-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-athena-capacityreservation-tag-syntax.yaml"></a>

```
  [Key](#cfn-athena-capacityreservation-tag-key): {{String}}
  [Value](#cfn-athena-capacityreservation-tag-value): {{String}}
```

## Properties
<a name="aws-properties-athena-capacityreservation-tag-properties"></a>

`Key`  <a name="cfn-athena-capacityreservation-tag-key"></a>
A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: \+ - = . \_ : / @. Tag keys are case-sensitive and must be unique per resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-athena-capacityreservation-tag-value"></a>
A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: \+ - = . \_ : / @. Tag values are case-sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
