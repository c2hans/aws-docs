---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-streamingdistribution-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::StreamingDistribution Tag
<a name="aws-properties-cloudfront-streamingdistribution-tag"></a>

A complex type that contains `Tag` key and `Tag` value.

## Syntax
<a name="aws-properties-cloudfront-streamingdistribution-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-streamingdistribution-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cloudfront-streamingdistribution-tag-key)" : {{String}},
  "[Value](#cfn-cloudfront-streamingdistribution-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-streamingdistribution-tag-syntax.yaml"></a>

```
  [Key](#cfn-cloudfront-streamingdistribution-tag-key): {{String}}
  [Value](#cfn-cloudfront-streamingdistribution-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-streamingdistribution-tag-properties"></a>

`Key`  <a name="cfn-cloudfront-streamingdistribution-tag-key"></a>
A string that contains `Tag` key.
The string length should be between 1 and 128 characters. Valid characters include `a-z`, `A-Z`, `0-9`, space, and the special characters `_ - . : / = + @`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudfront-streamingdistribution-tag-value"></a>
A string that contains an optional `Tag` value.
The string length should be between 0 and 256 characters. Valid characters include `a-z`, `A-Z`, `0-9`, space, and the special characters `_ - . : / = + @`.
*Required*: Yes
*Type*: String
*Pattern*: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
