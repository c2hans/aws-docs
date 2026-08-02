---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-analysisdefaults.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis AnalysisDefaults
<a name="aws-properties-quicksight-analysis-analysisdefaults"></a>

The configuration for default analysis settings.

## Syntax
<a name="aws-properties-quicksight-analysis-analysisdefaults-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-analysisdefaults-syntax.json"></a>

```
{
  "[DefaultNewSheetConfiguration](#cfn-quicksight-analysis-analysisdefaults-defaultnewsheetconfiguration)" : {{DefaultNewSheetConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-analysisdefaults-syntax.yaml"></a>

```
  [DefaultNewSheetConfiguration](#cfn-quicksight-analysis-analysisdefaults-defaultnewsheetconfiguration): {{
    DefaultNewSheetConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-analysisdefaults-properties"></a>

`DefaultNewSheetConfiguration`  <a name="cfn-quicksight-analysis-analysisdefaults-defaultnewsheetconfiguration"></a>
The configuration for default new sheet settings.
*Required*: Yes
*Type*: [DefaultNewSheetConfiguration](aws-properties-quicksight-analysis-defaultnewsheetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
