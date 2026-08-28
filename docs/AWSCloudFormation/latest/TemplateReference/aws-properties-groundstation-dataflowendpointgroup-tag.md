---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroup Tag
<a name="aws-properties-groundstation-dataflowendpointgroup-tag"></a>

The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`. digits, whitespace, `_`, `.`, `:`, `/`, `=`, `+`, `@`, `-`, and `"`.

For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html)

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-groundstation-dataflowendpointgroup-tag-key)" : {{String}},
  "[Value](#cfn-groundstation-dataflowendpointgroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-groundstation-dataflowendpointgroup-tag-key): {{String}}
  [Value](#cfn-groundstation-dataflowendpointgroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroup-tag-properties"></a>

`Key`  <a name="cfn-groundstation-dataflowendpointgroup-tag-key"></a>
Name of the object key.
*Required*: Yes
*Type*: String
*Pattern*: `^[ a-zA-Z0-9\+\-=._:/@]{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-groundstation-dataflowendpointgroup-tag-value"></a>
Value of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[ a-zA-Z0-9\+\-=._:/@]{1,256}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
