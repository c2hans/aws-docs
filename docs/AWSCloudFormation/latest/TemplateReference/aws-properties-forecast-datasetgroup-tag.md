---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-forecast-datasetgroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Forecast::DatasetGroup Tag
<a name="aws-properties-forecast-datasetgroup-tag"></a>

The optional metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.

The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50.
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8.
+ Maximum value length - 256 Unicode characters in UTF-8.
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has `aws` as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of `aws` do not count against your tags per resource limit.

## Syntax
<a name="aws-properties-forecast-datasetgroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-forecast-datasetgroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-forecast-datasetgroup-tag-key)" : {{String}},
  "[Value](#cfn-forecast-datasetgroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-forecast-datasetgroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-forecast-datasetgroup-tag-key): {{String}}
  [Value](#cfn-forecast-datasetgroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-forecast-datasetgroup-tag-properties"></a>

`Key`  <a name="cfn-forecast-datasetgroup-tag-key"></a>
One part of a key-value pair that makes up a tag. A `key` is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-forecast-datasetgroup-tag-value"></a>
The optional part of a key-value pair that makes up a tag. A `value` acts as a descriptor within a tag category (key).
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
