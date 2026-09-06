---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-kpiconditionalformattingoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template KPIConditionalFormattingOption
<a name="aws-properties-quicksight-template-kpiconditionalformattingoption"></a>

The conditional formatting options of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-template-kpiconditionalformattingoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-kpiconditionalformattingoption-syntax.json"></a>

```
{
  "[ActualValue](#cfn-quicksight-template-kpiconditionalformattingoption-actualvalue)" : {{KPIActualValueConditionalFormatting}},
  "[ComparisonValue](#cfn-quicksight-template-kpiconditionalformattingoption-comparisonvalue)" : {{KPIComparisonValueConditionalFormatting}},
  "[PrimaryValue](#cfn-quicksight-template-kpiconditionalformattingoption-primaryvalue)" : {{KPIPrimaryValueConditionalFormatting}},
  "[ProgressBar](#cfn-quicksight-template-kpiconditionalformattingoption-progressbar)" : {{KPIProgressBarConditionalFormatting}}
}
```

### YAML
<a name="aws-properties-quicksight-template-kpiconditionalformattingoption-syntax.yaml"></a>

```
  [ActualValue](#cfn-quicksight-template-kpiconditionalformattingoption-actualvalue): {{
    KPIActualValueConditionalFormatting}}
  [ComparisonValue](#cfn-quicksight-template-kpiconditionalformattingoption-comparisonvalue): {{
    KPIComparisonValueConditionalFormatting}}
  [PrimaryValue](#cfn-quicksight-template-kpiconditionalformattingoption-primaryvalue): {{
    KPIPrimaryValueConditionalFormatting}}
  [ProgressBar](#cfn-quicksight-template-kpiconditionalformattingoption-progressbar): {{
    KPIProgressBarConditionalFormatting}}
```

## Properties
<a name="aws-properties-quicksight-template-kpiconditionalformattingoption-properties"></a>

`ActualValue`  <a name="cfn-quicksight-template-kpiconditionalformattingoption-actualvalue"></a>
The conditional formatting for the actual value of a KPI visual.
*Required*: No
*Type*: [KPIActualValueConditionalFormatting](aws-properties-quicksight-template-kpiactualvalueconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComparisonValue`  <a name="cfn-quicksight-template-kpiconditionalformattingoption-comparisonvalue"></a>
The conditional formatting for the comparison value of a KPI visual.
*Required*: No
*Type*: [KPIComparisonValueConditionalFormatting](aws-properties-quicksight-template-kpicomparisonvalueconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryValue`  <a name="cfn-quicksight-template-kpiconditionalformattingoption-primaryvalue"></a>
The conditional formatting for the primary value of a KPI visual.
*Required*: No
*Type*: [KPIPrimaryValueConditionalFormatting](aws-properties-quicksight-template-kpiprimaryvalueconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgressBar`  <a name="cfn-quicksight-template-kpiconditionalformattingoption-progressbar"></a>
The conditional formatting for the progress bar of a KPI visual.
*Required*: No
*Type*: [KPIProgressBarConditionalFormatting](aws-properties-quicksight-template-kpiprogressbarconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
