---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendraranking-executionplan-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KendraRanking::ExecutionPlan Tag
<a name="aws-properties-kendraranking-executionplan-tag"></a>

A key-value pair that identifies or categorizes a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the `Rescore` API. You can also use a tag to help control access to a rescore execution plan. A tag key and value can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.

## Syntax
<a name="aws-properties-kendraranking-executionplan-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendraranking-executionplan-tag-syntax.json"></a>

```
{
  "[Key](#cfn-kendraranking-executionplan-tag-key)" : {{String}},
  "[Value](#cfn-kendraranking-executionplan-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendraranking-executionplan-tag-syntax.yaml"></a>

```
  [Key](#cfn-kendraranking-executionplan-tag-key): {{String}}
  [Value](#cfn-kendraranking-executionplan-tag-value): {{String}}
```

## Properties
<a name="aws-properties-kendraranking-executionplan-tag-properties"></a>

`Key`  <a name="cfn-kendraranking-executionplan-tag-key"></a>
The key for the tag. Keys are not case sensitive and must be unique.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-kendraranking-executionplan-tag-value"></a>
The value associated with the tag. The value can be an empty string but it can't be null.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
