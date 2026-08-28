---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-activity-tagsentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::Activity TagsEntry
<a name="aws-properties-stepfunctions-activity-tagsentry"></a>

The `TagsEntry` property specifies *tags* to identify an activity.

## Syntax
<a name="aws-properties-stepfunctions-activity-tagsentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-activity-tagsentry-syntax.json"></a>

```
{
  "[Key](#cfn-stepfunctions-activity-tagsentry-key)" : {{String}},
  "[Value](#cfn-stepfunctions-activity-tagsentry-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-stepfunctions-activity-tagsentry-syntax.yaml"></a>

```
  [Key](#cfn-stepfunctions-activity-tagsentry-key): {{String}}
  [Value](#cfn-stepfunctions-activity-tagsentry-value): {{String}}
```

## Properties
<a name="aws-properties-stepfunctions-activity-tagsentry-properties"></a>

`Key`  <a name="cfn-stepfunctions-activity-tagsentry-key"></a>
The `key` for a key-value pair in a tag entry.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-stepfunctions-activity-tagsentry-value"></a>
The `value` for a key-value pair in a tag entry.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
