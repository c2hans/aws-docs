---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-endpoint-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::Endpoint Tag
<a name="aws-properties-dms-endpoint-tag"></a>

A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:
+  `AddTagsToResource`
+  `ListTagsForResource`
+  `RemoveTagsFromResource`

## Syntax
<a name="aws-properties-dms-endpoint-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-endpoint-tag-syntax.json"></a>

```
{
  "[Key](#cfn-dms-endpoint-tag-key)" : {{String}},
  "[Value](#cfn-dms-endpoint-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-endpoint-tag-syntax.yaml"></a>

```
  [Key](#cfn-dms-endpoint-tag-key): {{String}}
  [Value](#cfn-dms-endpoint-tag-value): {{String}}
```

## Properties
<a name="aws-properties-dms-endpoint-tag-properties"></a>

`Key`  <a name="cfn-dms-endpoint-tag-key"></a>
A key is the required name of the tag. The string value can be 1-128 Unicode characters in length and can't be prefixed with "aws:" or "dms:". The string can only contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '\+', '-' (Java regular expressions: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-dms-endpoint-tag-value"></a>
A value is the optional value of the tag. The string value can be 1-256 Unicode characters in length and can't be prefixed with "aws:" or "dms:". The string can only contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '\+', '-' (Java regular expressions: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
