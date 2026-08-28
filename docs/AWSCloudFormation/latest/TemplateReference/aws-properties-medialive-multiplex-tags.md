---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-multiplex-tags.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplex Tags
<a name="aws-properties-medialive-multiplex-tags"></a>

<a name="aws-properties-medialive-multiplex-tags-description"></a>The `Tags` property type specifies Property description not available. for an [AWS::MediaLive::Multiplex](aws-resource-medialive-multiplex.md).

## Syntax
<a name="aws-properties-medialive-multiplex-tags-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-multiplex-tags-syntax.json"></a>

```
{
  "[Key](#cfn-medialive-multiplex-tags-key)" : {{String}},
  "[Value](#cfn-medialive-multiplex-tags-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-multiplex-tags-syntax.yaml"></a>

```
  [Key](#cfn-medialive-multiplex-tags-key): {{String}}
  [Value](#cfn-medialive-multiplex-tags-value): {{String}}
```

## Properties
<a name="aws-properties-medialive-multiplex-tags-properties"></a>

`Key`  <a name="cfn-medialive-multiplex-tags-key"></a>
The key name of the tag.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-medialive-multiplex-tags-value"></a>
The value for the tag.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
