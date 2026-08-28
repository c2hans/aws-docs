---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-topbottomfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TopBottomFilter
<a name="aws-properties-quicksight-template-topbottomfilter"></a>

A `TopBottomFilter` filters values that are at the top or the bottom.

## Syntax
<a name="aws-properties-quicksight-template-topbottomfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-topbottomfilter-syntax.json"></a>

```
{
  "[AggregationSortConfigurations](#cfn-quicksight-template-topbottomfilter-aggregationsortconfigurations)" : {{[ AggregationSortConfiguration, ... ]}},
  "[Column](#cfn-quicksight-template-topbottomfilter-column)" : {{ColumnIdentifier}},
  "[DefaultFilterControlConfiguration](#cfn-quicksight-template-topbottomfilter-defaultfiltercontrolconfiguration)" : {{DefaultFilterControlConfiguration}},
  "[FilterId](#cfn-quicksight-template-topbottomfilter-filterid)" : {{String}},
  "[Limit](#cfn-quicksight-template-topbottomfilter-limit)" : {{Number}},
  "[ParameterName](#cfn-quicksight-template-topbottomfilter-parametername)" : {{String}},
  "[TimeGranularity](#cfn-quicksight-template-topbottomfilter-timegranularity)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-topbottomfilter-syntax.yaml"></a>

```
  [AggregationSortConfigurations](#cfn-quicksight-template-topbottomfilter-aggregationsortconfigurations): {{
    - AggregationSortConfiguration}}
  [Column](#cfn-quicksight-template-topbottomfilter-column): {{
    ColumnIdentifier}}
  [DefaultFilterControlConfiguration](#cfn-quicksight-template-topbottomfilter-defaultfiltercontrolconfiguration): {{
    DefaultFilterControlConfiguration}}
  [FilterId](#cfn-quicksight-template-topbottomfilter-filterid): {{String}}
  [Limit](#cfn-quicksight-template-topbottomfilter-limit): {{Number}}
  [ParameterName](#cfn-quicksight-template-topbottomfilter-parametername): {{String}}
  [TimeGranularity](#cfn-quicksight-template-topbottomfilter-timegranularity): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-topbottomfilter-properties"></a>

`AggregationSortConfigurations`  <a name="cfn-quicksight-template-topbottomfilter-aggregationsortconfigurations"></a>
The aggregation and sort configuration of the top bottom filter.
*Required*: Yes
*Type*: Array of [AggregationSortConfiguration](aws-properties-quicksight-template-aggregationsortconfiguration.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Column`  <a name="cfn-quicksight-template-topbottomfilter-column"></a>
The column that the filter is applied to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-template-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultFilterControlConfiguration`  <a name="cfn-quicksight-template-topbottomfilter-defaultfiltercontrolconfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
*Required*: No
*Type*: [DefaultFilterControlConfiguration](aws-properties-quicksight-template-defaultfiltercontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterId`  <a name="cfn-quicksight-template-topbottomfilter-filterid"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Limit`  <a name="cfn-quicksight-template-topbottomfilter-limit"></a>
The number of items to include in the top bottom filter results.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterName`  <a name="cfn-quicksight-template-topbottomfilter-parametername"></a>
The parameter whose value should be used for the filter value.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeGranularity`  <a name="cfn-quicksight-template-topbottomfilter-timegranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
*Required*: No
*Type*: String
*Allowed values*: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
