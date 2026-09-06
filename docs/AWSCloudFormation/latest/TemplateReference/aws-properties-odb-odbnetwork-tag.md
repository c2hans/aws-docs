---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-odbnetwork-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork Tag
<a name="aws-properties-odb-odbnetwork-tag"></a>

A key-value pair to associate with a resource.

## Syntax
<a name="aws-properties-odb-odbnetwork-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-odbnetwork-tag-syntax.json"></a>

```
{
  "[Key](#cfn-odb-odbnetwork-tag-key)" : {{String}},
  "[Value](#cfn-odb-odbnetwork-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-odbnetwork-tag-syntax.yaml"></a>

```
  [Key](#cfn-odb-odbnetwork-tag-key): {{String}}
  [Value](#cfn-odb-odbnetwork-tag-value): {{String}}
```

## Properties
<a name="aws-properties-odb-odbnetwork-tag-properties"></a>

`Key`  <a name="cfn-odb-odbnetwork-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`. You can use any of the following characters: the set of Unicode letters, digits, whitespace, `_`, `.`, `:`, `/`, `=`, `+`, `@`, `-`, and `"`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-odb-odbnetwork-tag-value"></a>
The value for the tag. You can specify a value that's 1 to 256 characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
