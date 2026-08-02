---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-directoryservice-simplead-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectoryService::SimpleAD Tag
<a name="aws-properties-directoryservice-simplead-tag"></a>

Metadata assigned to a directory consisting of a key-value pair.

## Syntax
<a name="aws-properties-directoryservice-simplead-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-directoryservice-simplead-tag-syntax.json"></a>

```
{
  "[Key](#cfn-directoryservice-simplead-tag-key)" : {{String}},
  "[Value](#cfn-directoryservice-simplead-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-directoryservice-simplead-tag-syntax.yaml"></a>

```
  [Key](#cfn-directoryservice-simplead-tag-key): {{String}}
  [Value](#cfn-directoryservice-simplead-tag-value): {{String}}
```

## Properties
<a name="aws-properties-directoryservice-simplead-tag-properties"></a>

`Key`  <a name="cfn-directoryservice-simplead-tag-key"></a>
Required name of the tag. The string value can be Unicode characters and cannot be prefixed with "aws:". The string can contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '\+', '-', ':', '@'(Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-directoryservice-simplead-tag-value"></a>
The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '\+', '-', ':', '@' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
