---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-insightrule-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::InsightRule Tag
<a name="aws-properties-cloudwatch-insightrule-tag"></a>

A key-value pair associated with a CloudWatch resource.

## Syntax
<a name="aws-properties-cloudwatch-insightrule-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-insightrule-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cloudwatch-insightrule-tag-key)" : {{String}},
  "[Value](#cfn-cloudwatch-insightrule-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-insightrule-tag-syntax.yaml"></a>

```
  [Key](#cfn-cloudwatch-insightrule-tag-key): {{String}}
  [Value](#cfn-cloudwatch-insightrule-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-insightrule-tag-properties"></a>

`Key`  <a name="cfn-cloudwatch-insightrule-tag-key"></a>
A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudwatch-insightrule-tag-value"></a>
The value for the specified tag key.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
