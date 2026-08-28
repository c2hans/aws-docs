---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-secondaryvalueoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SecondaryValueOptions
<a name="aws-properties-quicksight-dashboard-secondaryvalueoptions"></a>

The options that determine the presentation of the secondary value of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-secondaryvalueoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-secondaryvalueoptions-syntax.json"></a>

```
{
  "[Visibility](#cfn-quicksight-dashboard-secondaryvalueoptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-secondaryvalueoptions-syntax.yaml"></a>

```
  [Visibility](#cfn-quicksight-dashboard-secondaryvalueoptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-secondaryvalueoptions-properties"></a>

`Visibility`  <a name="cfn-quicksight-dashboard-secondaryvalueoptions-visibility"></a>
Determines the visibility of the secondary value.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
