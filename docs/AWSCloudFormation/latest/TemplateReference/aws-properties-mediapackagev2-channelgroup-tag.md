---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-channelgroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::ChannelGroup Tag
<a name="aws-properties-mediapackagev2-channelgroup-tag"></a>

A comma-separated list of tag key:value pairs that you define.

## Syntax
<a name="aws-properties-mediapackagev2-channelgroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-channelgroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-mediapackagev2-channelgroup-tag-key)" : {{String}},
  "[Value](#cfn-mediapackagev2-channelgroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-channelgroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-mediapackagev2-channelgroup-tag-key): {{String}}
  [Value](#cfn-mediapackagev2-channelgroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-channelgroup-tag-properties"></a>

`Key`  <a name="cfn-mediapackagev2-channelgroup-tag-key"></a>
The key in the key:value pair for the tag.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-mediapackagev2-channelgroup-tag-value"></a>
The value in the key:value pair for the tag.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
