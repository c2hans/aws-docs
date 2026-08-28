---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-playbackrestrictionpolicy-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::PlaybackRestrictionPolicy Tag
<a name="aws-properties-ivs-playbackrestrictionpolicy-tag"></a>

A key-value pair that you can use to categorize and manage Amazon IVS PlaybackRestrictionPolicies.

## Syntax
<a name="aws-properties-ivs-playbackrestrictionpolicy-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-playbackrestrictionpolicy-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ivs-playbackrestrictionpolicy-tag-key)" : {{String}},
  "[Value](#cfn-ivs-playbackrestrictionpolicy-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivs-playbackrestrictionpolicy-tag-syntax.yaml"></a>

```
  [Key](#cfn-ivs-playbackrestrictionpolicy-tag-key): {{String}}
  [Value](#cfn-ivs-playbackrestrictionpolicy-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ivs-playbackrestrictionpolicy-tag-properties"></a>

`Key`  <a name="cfn-ivs-playbackrestrictionpolicy-tag-key"></a>
One part of a key-value pair that makes up a tag. A `key` is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ivs-playbackrestrictionpolicy-tag-value"></a>
The optional part of a key-value pair that makes up a tag. A `value` acts as a descriptor within a tag category (key).
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
