---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ram-permission-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RAM::Permission Tag
<a name="aws-properties-ram-permission-tag"></a>

A structure containing a tag. A tag is metadata that you can attach to your resources to help organize and categorize them. You can also use them to help you secure your resources. For more information, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html).

For more information about tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference Guide*.

## Syntax
<a name="aws-properties-ram-permission-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ram-permission-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ram-permission-tag-key)" : {{String}},
  "[Value](#cfn-ram-permission-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ram-permission-tag-syntax.yaml"></a>

```
  [Key](#cfn-ram-permission-tag-key): {{String}}
  [Value](#cfn-ram-permission-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ram-permission-tag-properties"></a>

`Key`  <a name="cfn-ram-permission-tag-key"></a>
The key, or name, attached to the tag. Every tag must have a key. Key names are case sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ram-permission-tag-value"></a>
The string value attached to the tag. The value can be an empty string. Key values are case sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
