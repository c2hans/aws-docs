---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-categoryinnerfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis CategoryInnerFilter
<a name="aws-properties-quicksight-analysis-categoryinnerfilter"></a>

A `CategoryInnerFilter` filters text values for the `NestedFilter`.

## Syntax
<a name="aws-properties-quicksight-analysis-categoryinnerfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-categoryinnerfilter-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-analysis-categoryinnerfilter-column)" : {{ColumnIdentifier}},
  "[Configuration](#cfn-quicksight-analysis-categoryinnerfilter-configuration)" : {{CategoryFilterConfiguration}},
  "[DefaultFilterControlConfiguration](#cfn-quicksight-analysis-categoryinnerfilter-defaultfiltercontrolconfiguration)" : {{DefaultFilterControlConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-categoryinnerfilter-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-analysis-categoryinnerfilter-column): {{
    ColumnIdentifier}}
  [Configuration](#cfn-quicksight-analysis-categoryinnerfilter-configuration): {{
    CategoryFilterConfiguration}}
  [DefaultFilterControlConfiguration](#cfn-quicksight-analysis-categoryinnerfilter-defaultfiltercontrolconfiguration): {{
    DefaultFilterControlConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-categoryinnerfilter-properties"></a>

`Column`  <a name="cfn-quicksight-analysis-categoryinnerfilter-column"></a>
Property description not available.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configuration`  <a name="cfn-quicksight-analysis-categoryinnerfilter-configuration"></a>
Property description not available.
*Required*: Yes
*Type*: [CategoryFilterConfiguration](aws-properties-quicksight-analysis-categoryfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultFilterControlConfiguration`  <a name="cfn-quicksight-analysis-categoryinnerfilter-defaultfiltercontrolconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [DefaultFilterControlConfiguration](aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
