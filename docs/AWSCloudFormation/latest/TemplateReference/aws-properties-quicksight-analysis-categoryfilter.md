---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-categoryfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis CategoryFilter
<a name="aws-properties-quicksight-analysis-categoryfilter"></a>

A `CategoryFilter` filters text values.

For more information, see [Adding text filters](https://docs.aws.amazon.com/quicksight/latest/user/add-a-text-filter-data-prep.html) in the *Amazon Quick Suite User Guide*.

## Syntax
<a name="aws-properties-quicksight-analysis-categoryfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-categoryfilter-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-analysis-categoryfilter-column)" : {{ColumnIdentifier}},
  "[Configuration](#cfn-quicksight-analysis-categoryfilter-configuration)" : {{CategoryFilterConfiguration}},
  "[DefaultFilterControlConfiguration](#cfn-quicksight-analysis-categoryfilter-defaultfiltercontrolconfiguration)" : {{DefaultFilterControlConfiguration}},
  "[FilterId](#cfn-quicksight-analysis-categoryfilter-filterid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-categoryfilter-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-analysis-categoryfilter-column): {{
    ColumnIdentifier}}
  [Configuration](#cfn-quicksight-analysis-categoryfilter-configuration): {{
    CategoryFilterConfiguration}}
  [DefaultFilterControlConfiguration](#cfn-quicksight-analysis-categoryfilter-defaultfiltercontrolconfiguration): {{
    DefaultFilterControlConfiguration}}
  [FilterId](#cfn-quicksight-analysis-categoryfilter-filterid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-categoryfilter-properties"></a>

`Column`  <a name="cfn-quicksight-analysis-categoryfilter-column"></a>
The column that the filter is applied to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configuration`  <a name="cfn-quicksight-analysis-categoryfilter-configuration"></a>
The configuration for a `CategoryFilter`.
*Required*: Yes
*Type*: [CategoryFilterConfiguration](aws-properties-quicksight-analysis-categoryfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultFilterControlConfiguration`  <a name="cfn-quicksight-analysis-categoryfilter-defaultfiltercontrolconfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
*Required*: No
*Type*: [DefaultFilterControlConfiguration](aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterId`  <a name="cfn-quicksight-analysis-categoryfilter-filterid"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
