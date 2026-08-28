---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-timeequalityfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TimeEqualityFilter
<a name="aws-properties-quicksight-analysis-timeequalityfilter"></a>

A `TimeEqualityFilter` filters values that are equal to a given value.

## Syntax
<a name="aws-properties-quicksight-analysis-timeequalityfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-timeequalityfilter-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-analysis-timeequalityfilter-column)" : {{ColumnIdentifier}},
  "[DefaultFilterControlConfiguration](#cfn-quicksight-analysis-timeequalityfilter-defaultfiltercontrolconfiguration)" : {{DefaultFilterControlConfiguration}},
  "[FilterId](#cfn-quicksight-analysis-timeequalityfilter-filterid)" : {{String}},
  "[ParameterName](#cfn-quicksight-analysis-timeequalityfilter-parametername)" : {{String}},
  "[RollingDate](#cfn-quicksight-analysis-timeequalityfilter-rollingdate)" : {{RollingDateConfiguration}},
  "[TimeGranularity](#cfn-quicksight-analysis-timeequalityfilter-timegranularity)" : {{String}},
  "[Value](#cfn-quicksight-analysis-timeequalityfilter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-timeequalityfilter-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-analysis-timeequalityfilter-column): {{
    ColumnIdentifier}}
  [DefaultFilterControlConfiguration](#cfn-quicksight-analysis-timeequalityfilter-defaultfiltercontrolconfiguration): {{
    DefaultFilterControlConfiguration}}
  [FilterId](#cfn-quicksight-analysis-timeequalityfilter-filterid): {{String}}
  [ParameterName](#cfn-quicksight-analysis-timeequalityfilter-parametername): {{String}}
  [RollingDate](#cfn-quicksight-analysis-timeequalityfilter-rollingdate): {{
    RollingDateConfiguration}}
  [TimeGranularity](#cfn-quicksight-analysis-timeequalityfilter-timegranularity): {{String}}
  [Value](#cfn-quicksight-analysis-timeequalityfilter-value): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-timeequalityfilter-properties"></a>

`Column`  <a name="cfn-quicksight-analysis-timeequalityfilter-column"></a>
The column that the filter is applied to.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultFilterControlConfiguration`  <a name="cfn-quicksight-analysis-timeequalityfilter-defaultfiltercontrolconfiguration"></a>
The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.
*Required*: No
*Type*: [DefaultFilterControlConfiguration](aws-properties-quicksight-analysis-defaultfiltercontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterId`  <a name="cfn-quicksight-analysis-timeequalityfilter-filterid"></a>
An identifier that uniquely identifies a filter within a dashboard, analysis, or template.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterName`  <a name="cfn-quicksight-analysis-timeequalityfilter-parametername"></a>
The parameter whose value should be used for the filter value.
This field is mutually exclusive to `Value` and `RollingDate`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RollingDate`  <a name="cfn-quicksight-analysis-timeequalityfilter-rollingdate"></a>
The rolling date input for the `TimeEquality` filter.
This field is mutually exclusive to `Value` and `ParameterName`.
*Required*: No
*Type*: [RollingDateConfiguration](aws-properties-quicksight-analysis-rollingdateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeGranularity`  <a name="cfn-quicksight-analysis-timeequalityfilter-timegranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
*Required*: No
*Type*: String
*Allowed values*: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-analysis-timeequalityfilter-value"></a>
The value of a `TimeEquality` filter.
This field is mutually exclusive to `RollingDate` and `ParameterName`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
