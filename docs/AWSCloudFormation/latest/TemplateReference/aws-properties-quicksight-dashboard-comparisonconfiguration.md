---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-comparisonconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ComparisonConfiguration
<a name="aws-properties-quicksight-dashboard-comparisonconfiguration"></a>

The comparison display configuration of a KPI or gauge chart.

## Syntax
<a name="aws-properties-quicksight-dashboard-comparisonconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-comparisonconfiguration-syntax.json"></a>

```
{
  "[ComparisonFormat](#cfn-quicksight-dashboard-comparisonconfiguration-comparisonformat)" : {{ComparisonFormatConfiguration}},
  "[ComparisonMethod](#cfn-quicksight-dashboard-comparisonconfiguration-comparisonmethod)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-comparisonconfiguration-syntax.yaml"></a>

```
  [ComparisonFormat](#cfn-quicksight-dashboard-comparisonconfiguration-comparisonformat): {{
    ComparisonFormatConfiguration}}
  [ComparisonMethod](#cfn-quicksight-dashboard-comparisonconfiguration-comparisonmethod): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-comparisonconfiguration-properties"></a>

`ComparisonFormat`  <a name="cfn-quicksight-dashboard-comparisonconfiguration-comparisonformat"></a>
The format of the comparison.
*Required*: No
*Type*: [ComparisonFormatConfiguration](aws-properties-quicksight-dashboard-comparisonformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComparisonMethod`  <a name="cfn-quicksight-dashboard-comparisonconfiguration-comparisonmethod"></a>
The method of the comparison. Choose from the following options:
+  `DIFFERENCE`
+  `PERCENT_DIFFERENCE`
+  `PERCENT`
*Required*: No
*Type*: String
*Allowed values*: `DIFFERENCE | PERCENT_DIFFERENCE | PERCENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
