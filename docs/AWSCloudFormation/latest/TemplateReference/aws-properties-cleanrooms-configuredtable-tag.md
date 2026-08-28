---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable Tag
<a name="aws-properties-cleanrooms-configuredtable-tag"></a>

An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cleanrooms-configuredtable-tag-key)" : {{String}},
  "[Value](#cfn-cleanrooms-configuredtable-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-tag-syntax.yaml"></a>

```
  [Key](#cfn-cleanrooms-configuredtable-tag-key): {{String}}
  [Value](#cfn-cleanrooms-configuredtable-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-tag-properties"></a>

`Key`  <a name="cfn-cleanrooms-configuredtable-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cleanrooms-configuredtable-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
