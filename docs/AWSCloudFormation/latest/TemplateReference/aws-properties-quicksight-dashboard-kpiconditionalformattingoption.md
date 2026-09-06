---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-kpiconditionalformattingoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard KPIConditionalFormattingOption
<a name="aws-properties-quicksight-dashboard-kpiconditionalformattingoption"></a>

The conditional formatting options of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-kpiconditionalformattingoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-kpiconditionalformattingoption-syntax.json"></a>

```
{
  "[ActualValue](#cfn-quicksight-dashboard-kpiconditionalformattingoption-actualvalue)" : {{KPIActualValueConditionalFormatting}},
  "[ComparisonValue](#cfn-quicksight-dashboard-kpiconditionalformattingoption-comparisonvalue)" : {{KPIComparisonValueConditionalFormatting}},
  "[PrimaryValue](#cfn-quicksight-dashboard-kpiconditionalformattingoption-primaryvalue)" : {{KPIPrimaryValueConditionalFormatting}},
  "[ProgressBar](#cfn-quicksight-dashboard-kpiconditionalformattingoption-progressbar)" : {{KPIProgressBarConditionalFormatting}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-kpiconditionalformattingoption-syntax.yaml"></a>

```
  [ActualValue](#cfn-quicksight-dashboard-kpiconditionalformattingoption-actualvalue): {{
    KPIActualValueConditionalFormatting}}
  [ComparisonValue](#cfn-quicksight-dashboard-kpiconditionalformattingoption-comparisonvalue): {{
    KPIComparisonValueConditionalFormatting}}
  [PrimaryValue](#cfn-quicksight-dashboard-kpiconditionalformattingoption-primaryvalue): {{
    KPIPrimaryValueConditionalFormatting}}
  [ProgressBar](#cfn-quicksight-dashboard-kpiconditionalformattingoption-progressbar): {{
    KPIProgressBarConditionalFormatting}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-kpiconditionalformattingoption-properties"></a>

`ActualValue`  <a name="cfn-quicksight-dashboard-kpiconditionalformattingoption-actualvalue"></a>
The conditional formatting for the actual value of a KPI visual.
*Required*: No
*Type*: [KPIActualValueConditionalFormatting](aws-properties-quicksight-dashboard-kpiactualvalueconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComparisonValue`  <a name="cfn-quicksight-dashboard-kpiconditionalformattingoption-comparisonvalue"></a>
The conditional formatting for the comparison value of a KPI visual.
*Required*: No
*Type*: [KPIComparisonValueConditionalFormatting](aws-properties-quicksight-dashboard-kpicomparisonvalueconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryValue`  <a name="cfn-quicksight-dashboard-kpiconditionalformattingoption-primaryvalue"></a>
The conditional formatting for the primary value of a KPI visual.
*Required*: No
*Type*: [KPIPrimaryValueConditionalFormatting](aws-properties-quicksight-dashboard-kpiprimaryvalueconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgressBar`  <a name="cfn-quicksight-dashboard-kpiconditionalformattingoption-progressbar"></a>
The conditional formatting for the progress bar of a KPI visual.
*Required*: No
*Type*: [KPIProgressBarConditionalFormatting](aws-properties-quicksight-dashboard-kpiprogressbarconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
