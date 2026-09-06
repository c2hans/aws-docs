---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-kpiconditionalformattingoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis KPIConditionalFormattingOption
<a name="aws-properties-quicksight-analysis-kpiconditionalformattingoption"></a>

The conditional formatting options of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-analysis-kpiconditionalformattingoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-kpiconditionalformattingoption-syntax.json"></a>

```
{
  "[ActualValue](#cfn-quicksight-analysis-kpiconditionalformattingoption-actualvalue)" : {{KPIActualValueConditionalFormatting}},
  "[ComparisonValue](#cfn-quicksight-analysis-kpiconditionalformattingoption-comparisonvalue)" : {{KPIComparisonValueConditionalFormatting}},
  "[PrimaryValue](#cfn-quicksight-analysis-kpiconditionalformattingoption-primaryvalue)" : {{KPIPrimaryValueConditionalFormatting}},
  "[ProgressBar](#cfn-quicksight-analysis-kpiconditionalformattingoption-progressbar)" : {{KPIProgressBarConditionalFormatting}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-kpiconditionalformattingoption-syntax.yaml"></a>

```
  [ActualValue](#cfn-quicksight-analysis-kpiconditionalformattingoption-actualvalue): {{
    KPIActualValueConditionalFormatting}}
  [ComparisonValue](#cfn-quicksight-analysis-kpiconditionalformattingoption-comparisonvalue): {{
    KPIComparisonValueConditionalFormatting}}
  [PrimaryValue](#cfn-quicksight-analysis-kpiconditionalformattingoption-primaryvalue): {{
    KPIPrimaryValueConditionalFormatting}}
  [ProgressBar](#cfn-quicksight-analysis-kpiconditionalformattingoption-progressbar): {{
    KPIProgressBarConditionalFormatting}}
```

## Properties
<a name="aws-properties-quicksight-analysis-kpiconditionalformattingoption-properties"></a>

`ActualValue`  <a name="cfn-quicksight-analysis-kpiconditionalformattingoption-actualvalue"></a>
The conditional formatting for the actual value of a KPI visual.
*Required*: No
*Type*: [KPIActualValueConditionalFormatting](aws-properties-quicksight-analysis-kpiactualvalueconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComparisonValue`  <a name="cfn-quicksight-analysis-kpiconditionalformattingoption-comparisonvalue"></a>
The conditional formatting for the comparison value of a KPI visual.
*Required*: No
*Type*: [KPIComparisonValueConditionalFormatting](aws-properties-quicksight-analysis-kpicomparisonvalueconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryValue`  <a name="cfn-quicksight-analysis-kpiconditionalformattingoption-primaryvalue"></a>
The conditional formatting for the primary value of a KPI visual.
*Required*: No
*Type*: [KPIPrimaryValueConditionalFormatting](aws-properties-quicksight-analysis-kpiprimaryvalueconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgressBar`  <a name="cfn-quicksight-analysis-kpiconditionalformattingoption-progressbar"></a>
The conditional formatting for the progress bar of a KPI visual.
*Required*: No
*Type*: [KPIProgressBarConditionalFormatting](aws-properties-quicksight-analysis-kpiprogressbarconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
