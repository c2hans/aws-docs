---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialnulldatasettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialNullDataSettings
<a name="aws-properties-quicksight-analysis-geospatialnulldatasettings"></a>

The properties for the visualization of null data.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialnulldatasettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialnulldatasettings-syntax.json"></a>

```
{
  "[SymbolStyle](#cfn-quicksight-analysis-geospatialnulldatasettings-symbolstyle)" : {{GeospatialNullSymbolStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialnulldatasettings-syntax.yaml"></a>

```
  [SymbolStyle](#cfn-quicksight-analysis-geospatialnulldatasettings-symbolstyle): {{
    GeospatialNullSymbolStyle}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialnulldatasettings-properties"></a>

`SymbolStyle`  <a name="cfn-quicksight-analysis-geospatialnulldatasettings-symbolstyle"></a>
The symbol style for null data.
*Required*: Yes
*Type*: [GeospatialNullSymbolStyle](aws-properties-quicksight-analysis-geospatialnullsymbolstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
