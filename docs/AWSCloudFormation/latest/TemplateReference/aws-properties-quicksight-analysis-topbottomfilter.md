---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-topbottomfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TopBottomFilter
<a name="aws-properties-quicksight-analysis-topbottomfilter"></a>

A `TopBottomFilter` filters values that are at the top or the bottom.

## Syntax
<a name="aws-properties-quicksight-analysis-topbottomfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-topbottomfilter-syntax.json"></a>

```
{
  "[AggregationSortConfigurations](#cfn-quicksight-analysis-topbottomfilter-aggregationsortconfigurations)" : {{[ AggregationSortConfiguration, ... ]}},
  "[Column](#cfn-quicksight-analysis-topbottomfilter-column)" : {{ColumnIdentifier}},
  "[DefaultFilterControlConfiguration](#cfn-quicksight-analysis-topbottomfilter-defaultfiltercontrolconfiguration)" : {{DefaultFilterControlConfiguration}},
  "[FilterId](#cfn-quicksight-analysis-topbottomfilter-filterid)" : {{String}},
  "[Limit](#cfn-quicksight-analysis-topbottomfilter-limit)" : {{Number}},
  "[ParameterName](#cfn-quicksight-analysis-topbottomfilter-parametername)" : {{String}},
  "[TimeGranularity](#cfn-quicksight-analysis-topbottomfilter-timegranularity)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-topbottomfilter-syntax.yaml"></a>

```
  [AggregationSortConfigurations](#cfn-quicksight-analysis-topbottomfilter-aggregationsortconfigurations): {{
    - AggregationSortConfiguration}}
  [Column](#cfn-quicksight-analysis-topbottomfilter-column): {{
    ColumnIdentifier}}
  [DefaultFilterControlConfiguration](#cfn-quicksight-analysis-topbottomfilter-defaultfiltercontrolconfiguration): {{
    DefaultFilterControlConfiguration}}
  [FilterId](#cfn-quicksight-analysis-topbottomfilter-filterid): {{String}}
  [Limit](#cfn-quicksight-analysis-topbottomfilter-limit): {{Number}}
  [ParameterName](#cfn-quicksight-analysis-topbottomfilter-parametername): {{String}}
  [TimeGranularity](#cfn-quicksight-analysis-topbottomfilter-timegranularity): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-topbottomfilter-properties"></a>

`AggregationSortConfigurations`  <a name="cfn-quicksight-analysis-topbottomfilter-aggregationsortconfigurations"></a>
The aggregation and sort configuration of the top bottom filter.
*Required*: Yes
*Type*: Array of [AggregationSortConfiguration](aws-properties-quicksight-analysis-aggregationsortconfiguration.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Column`  <a name="cfn-quicksight-analysis-topbottomfilter-column"></a>
The column that the filter is applied to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultFilterControlConfiguration`  <a name="cfn-quicksight-analysis-topbottomfilter-defaultfiltercontrolconfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
*Required*: No
*Type*: [DefaultFilterControlConfiguration](aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterId`  <a name="cfn-quicksight-analysis-topbottomfilter-filterid"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Limit`  <a name="cfn-quicksight-analysis-topbottomfilter-limit"></a>
The number of items to include in the top bottom filter results.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterName`  <a name="cfn-quicksight-analysis-topbottomfilter-parametername"></a>
The parameter whose value should be used for the filter value.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeGranularity`  <a name="cfn-quicksight-analysis-topbottomfilter-timegranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
*Required*: No
*Type*: String
*Allowed values*: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
