---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule Tag
<a name="aws-properties-events-rule-tag"></a>

A key-value pair associated with an ECS Target of an EventBridge rule. The tag will be propagated to ECS by EventBridge when starting an ECS task based on a matched event.

**Important**
Currently, tags are only available when using ECS with EventBridge.

## Syntax
<a name="aws-properties-events-rule-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-tag-syntax.json"></a>

```
{
  "[Key](#cfn-events-rule-tag-key)" : {{String}},
  "[Value](#cfn-events-rule-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-rule-tag-syntax.yaml"></a>

```
  [Key](#cfn-events-rule-tag-key): {{String}}
  [Value](#cfn-events-rule-tag-value): {{String}}
```

## Properties
<a name="aws-properties-events-rule-tag-properties"></a>

`Key`  <a name="cfn-events-rule-tag-key"></a>
A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-events-rule-tag-value"></a>
The value for the specified tag key.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
