---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-xray-samplingrule-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::XRay::SamplingRule Tag
<a name="aws-properties-xray-samplingrule-tag"></a>

A map that contains tag keys and tag values to attach to an AWS X-Ray group or sampling rule. For more information about ways to use tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.

The following restrictions apply to tags:
+ Maximum number of user-applied tags per resource: 50
+ Tag keys and values are case sensitive.
+ Don't use `aws:` as a prefix for keys; it's reserved for AWS use. You cannot edit or delete system tags.

## Syntax
<a name="aws-properties-xray-samplingrule-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-xray-samplingrule-tag-syntax.json"></a>

```
{
  "[Key](#cfn-xray-samplingrule-tag-key)" : {{String}},
  "[Value](#cfn-xray-samplingrule-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-xray-samplingrule-tag-syntax.yaml"></a>

```
  [Key](#cfn-xray-samplingrule-tag-key): {{String}}
  [Value](#cfn-xray-samplingrule-tag-value): {{String}}
```

## Properties
<a name="aws-properties-xray-samplingrule-tag-properties"></a>

`Key`  <a name="cfn-xray-samplingrule-tag-key"></a>
A tag key, such as `Stage` or `Name`. A tag key cannot be empty. The key can be a maximum of 128 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-xray-samplingrule-tag-value"></a>
An optional tag value, such as `Production` or `test-only`. The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
