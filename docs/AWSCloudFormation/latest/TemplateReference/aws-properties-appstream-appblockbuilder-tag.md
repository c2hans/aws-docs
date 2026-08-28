---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-appblockbuilder-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::AppBlockBuilder Tag
<a name="aws-properties-appstream-appblockbuilder-tag"></a>

The tag of the app block builder.

## Syntax
<a name="aws-properties-appstream-appblockbuilder-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-appblockbuilder-tag-syntax.json"></a>

```
{
  "[Key](#cfn-appstream-appblockbuilder-tag-key)" : {{String}},
  "[Value](#cfn-appstream-appblockbuilder-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-appblockbuilder-tag-syntax.yaml"></a>

```
  [Key](#cfn-appstream-appblockbuilder-tag-key): {{String}}
  [Value](#cfn-appstream-appblockbuilder-tag-value): {{String}}
```

## Properties
<a name="aws-properties-appstream-appblockbuilder-tag-properties"></a>

`Key`  <a name="cfn-appstream-appblockbuilder-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appstream-appblockbuilder-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
