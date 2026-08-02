---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-codesigningconfig-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CodeSigningConfig Tag
<a name="aws-properties-lambda-codesigningconfig-tag"></a>

A [tag](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) to apply to the code signing configuration.

## Syntax
<a name="aws-properties-lambda-codesigningconfig-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-codesigningconfig-tag-syntax.json"></a>

```
{
  "[Key](#cfn-lambda-codesigningconfig-tag-key)" : {{String}},
  "[Value](#cfn-lambda-codesigningconfig-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-codesigningconfig-tag-syntax.yaml"></a>

```
  [Key](#cfn-lambda-codesigningconfig-tag-key): {{String}}
  [Value](#cfn-lambda-codesigningconfig-tag-value): {{String}}
```

## Properties
<a name="aws-properties-lambda-codesigningconfig-tag-properties"></a>

`Key`  <a name="cfn-lambda-codesigningconfig-tag-key"></a>
The key for this tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-lambda-codesigningconfig-tag-value"></a>
The value for this tag.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
