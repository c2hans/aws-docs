---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-supportauthz-supportpermit-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SupportAuthZ::SupportPermit Tag
<a name="aws-properties-supportauthz-supportpermit-tag"></a>

A key-value pair to associate with a resource.

## Syntax
<a name="aws-properties-supportauthz-supportpermit-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-supportauthz-supportpermit-tag-syntax.json"></a>

```
{
  "[Key](#cfn-supportauthz-supportpermit-tag-key)" : {{String}},
  "[Value](#cfn-supportauthz-supportpermit-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-supportauthz-supportpermit-tag-syntax.yaml"></a>

```
  [Key](#cfn-supportauthz-supportpermit-tag-key): {{String}}
  [Value](#cfn-supportauthz-supportpermit-tag-value): {{String}}
```

## Properties
<a name="aws-properties-supportauthz-supportpermit-tag-properties"></a>

`Key`  <a name="cfn-supportauthz-supportpermit-tag-key"></a>
The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-supportauthz-supportpermit-tag-value"></a>
The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
