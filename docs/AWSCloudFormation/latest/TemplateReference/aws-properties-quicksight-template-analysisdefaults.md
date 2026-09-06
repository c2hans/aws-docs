---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-analysisdefaults.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template AnalysisDefaults
<a name="aws-properties-quicksight-template-analysisdefaults"></a>

The configuration for default analysis settings.

## Syntax
<a name="aws-properties-quicksight-template-analysisdefaults-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-analysisdefaults-syntax.json"></a>

```
{
  "[DefaultNewSheetConfiguration](#cfn-quicksight-template-analysisdefaults-defaultnewsheetconfiguration)" : {{DefaultNewSheetConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-analysisdefaults-syntax.yaml"></a>

```
  [DefaultNewSheetConfiguration](#cfn-quicksight-template-analysisdefaults-defaultnewsheetconfiguration): {{
    DefaultNewSheetConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-analysisdefaults-properties"></a>

`DefaultNewSheetConfiguration`  <a name="cfn-quicksight-template-analysisdefaults-defaultnewsheetconfiguration"></a>
The configuration for default new sheet settings.
*Required*: Yes
*Type*: [DefaultNewSheetConfiguration](aws-properties-quicksight-template-defaultnewsheetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
