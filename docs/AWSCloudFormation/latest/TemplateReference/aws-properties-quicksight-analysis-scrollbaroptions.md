---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-scrollbaroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ScrollBarOptions
<a name="aws-properties-quicksight-analysis-scrollbaroptions"></a>

The visual display options for a data zoom scroll bar.

## Syntax
<a name="aws-properties-quicksight-analysis-scrollbaroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-scrollbaroptions-syntax.json"></a>

```
{
  "[Visibility](#cfn-quicksight-analysis-scrollbaroptions-visibility)" : {{String}},
  "[VisibleRange](#cfn-quicksight-analysis-scrollbaroptions-visiblerange)" : {{VisibleRangeOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-scrollbaroptions-syntax.yaml"></a>

```
  [Visibility](#cfn-quicksight-analysis-scrollbaroptions-visibility): {{String}}
  [VisibleRange](#cfn-quicksight-analysis-scrollbaroptions-visiblerange): {{
    VisibleRangeOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-scrollbaroptions-properties"></a>

`Visibility`  <a name="cfn-quicksight-analysis-scrollbaroptions-visibility"></a>
The visibility of the data zoom scroll bar.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisibleRange`  <a name="cfn-quicksight-analysis-scrollbaroptions-visiblerange"></a>
The visibility range for the data zoom scroll bar.
*Required*: No
*Type*: [VisibleRangeOptions](aws-properties-quicksight-analysis-visiblerangeoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
