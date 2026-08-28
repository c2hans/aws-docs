---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-connectionfunction-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ConnectionFunction Tag
<a name="aws-properties-cloudfront-connectionfunction-tag"></a>

A complex type that contains `Tag` key and `Tag` value.

## Syntax
<a name="aws-properties-cloudfront-connectionfunction-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-connectionfunction-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cloudfront-connectionfunction-tag-key)" : {{String}},
  "[Value](#cfn-cloudfront-connectionfunction-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-connectionfunction-tag-syntax.yaml"></a>

```
  [Key](#cfn-cloudfront-connectionfunction-tag-key): {{String}}
  [Value](#cfn-cloudfront-connectionfunction-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-connectionfunction-tag-properties"></a>

`Key`  <a name="cfn-cloudfront-connectionfunction-tag-key"></a>
A string that contains `Tag` key.
The string length should be between 1 and 128 characters. Valid characters include `a-z`, `A-Z`, `0-9`, space, and the special characters `_ - . : / = + @`.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudfront-connectionfunction-tag-value"></a>
A string that contains an optional `Tag` value.
The string length should be between 0 and 256 characters. Valid characters include `a-z`, `A-Z`, `0-9`, space, and the special characters `_ - . : / = + @`.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
