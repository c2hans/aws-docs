---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-view-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::View Tag
<a name="aws-properties-connect-view-tag"></a>

A key-value pair to associate with a resource.

## Syntax
<a name="aws-properties-connect-view-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-view-tag-syntax.json"></a>

```
{
  "[Key](#cfn-connect-view-tag-key)" : {{String}},
  "[Value](#cfn-connect-view-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-view-tag-syntax.yaml"></a>

```
  [Key](#cfn-connect-view-tag-key): {{String}}
  [Value](#cfn-connect-view-tag-value): {{String}}
```

## Properties
<a name="aws-properties-connect-view-tag-properties"></a>

`Key`  <a name="cfn-connect-view-tag-key"></a>
The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, \_, ., /, =, \+, and -
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-connect-view-tag-value"></a>
The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, \_, ., /, =, \+, and -
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
