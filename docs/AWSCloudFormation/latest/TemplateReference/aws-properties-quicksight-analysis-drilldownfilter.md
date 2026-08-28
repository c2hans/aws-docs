---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-drilldownfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DrillDownFilter
<a name="aws-properties-quicksight-analysis-drilldownfilter"></a>

The drill down filter for the column hierarchies.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-analysis-drilldownfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-drilldownfilter-syntax.json"></a>

```
{
  "[CategoryFilter](#cfn-quicksight-analysis-drilldownfilter-categoryfilter)" : {{CategoryDrillDownFilter}},
  "[NumericEqualityFilter](#cfn-quicksight-analysis-drilldownfilter-numericequalityfilter)" : {{NumericEqualityDrillDownFilter}},
  "[TimeRangeFilter](#cfn-quicksight-analysis-drilldownfilter-timerangefilter)" : {{TimeRangeDrillDownFilter}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-drilldownfilter-syntax.yaml"></a>

```
  [CategoryFilter](#cfn-quicksight-analysis-drilldownfilter-categoryfilter): {{
    CategoryDrillDownFilter}}
  [NumericEqualityFilter](#cfn-quicksight-analysis-drilldownfilter-numericequalityfilter): {{
    NumericEqualityDrillDownFilter}}
  [TimeRangeFilter](#cfn-quicksight-analysis-drilldownfilter-timerangefilter): {{
    TimeRangeDrillDownFilter}}
```

## Properties
<a name="aws-properties-quicksight-analysis-drilldownfilter-properties"></a>

`CategoryFilter`  <a name="cfn-quicksight-analysis-drilldownfilter-categoryfilter"></a>
The category type drill down filter. This filter is used for string type columns.
*Required*: No
*Type*: [CategoryDrillDownFilter](aws-properties-quicksight-analysis-categorydrilldownfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumericEqualityFilter`  <a name="cfn-quicksight-analysis-drilldownfilter-numericequalityfilter"></a>
The numeric equality type drill down filter. This filter is used for number type columns.
*Required*: No
*Type*: [NumericEqualityDrillDownFilter](aws-properties-quicksight-analysis-numericequalitydrilldownfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeRangeFilter`  <a name="cfn-quicksight-analysis-drilldownfilter-timerangefilter"></a>
The time range drill down filter. This filter is used for date time columns.
*Required*: No
*Type*: [TimeRangeDrillDownFilter](aws-properties-quicksight-analysis-timerangedrilldownfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
