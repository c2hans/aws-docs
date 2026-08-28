---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-collectiveconstant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic CollectiveConstant
<a name="aws-properties-quicksight-topic-collectiveconstant"></a>

A structure that represents a collective constant.

## Syntax
<a name="aws-properties-quicksight-topic-collectiveconstant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-collectiveconstant-syntax.json"></a>

```
{
  "[ValueList](#cfn-quicksight-topic-collectiveconstant-valuelist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-collectiveconstant-syntax.yaml"></a>

```
  [ValueList](#cfn-quicksight-topic-collectiveconstant-valuelist): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-topic-collectiveconstant-properties"></a>

`ValueList`  <a name="cfn-quicksight-topic-collectiveconstant-valuelist"></a>
A list of values for the collective constant.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
