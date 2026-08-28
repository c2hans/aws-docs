---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-macie-allowlist-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Macie::AllowList Tag
<a name="aws-properties-macie-allowlist-tag"></a>

Specifies a tag (key-value pair) to apply to an allow list. A *tag* is a label that you can define and associate with AWS resources, including certain types of Amazon Macie resources. Each tag consists of a *tag key* and an associated *tag value*. A *tag key* is a general label that acts as a category for a more specific tag value. Each tag key must be unique and it can have only one tag value. A *tag value* acts as a descriptor for a tag key. Tag keys and values are case sensitive. They can contain letters, numbers, spaces, or the following symbols: \_ . : / = \+ - @

For more information, see [Tagging Macie resources](https://docs.aws.amazon.com/macie/latest/user/tagging-resources.html) in the *Amazon Macie User Guide*.

## Syntax
<a name="aws-properties-macie-allowlist-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-macie-allowlist-tag-syntax.json"></a>

```
{
  "[Key](#cfn-macie-allowlist-tag-key)" : {{String}},
  "[Value](#cfn-macie-allowlist-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-macie-allowlist-tag-syntax.yaml"></a>

```
  [Key](#cfn-macie-allowlist-tag-key): {{String}}
  [Value](#cfn-macie-allowlist-tag-value): {{String}}
```

## Properties
<a name="aws-properties-macie-allowlist-tag-properties"></a>

`Key`  <a name="cfn-macie-allowlist-tag-key"></a>
The name of the tag key. A tag key can contain up to 128 UTF-8 characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-macie-allowlist-tag-value"></a>
The tag value to associate with the specified tag key (`Key`). A tag value can contain up to 256 UTF-8 characters. A tag value cannot be null, but it can be an empty string.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
