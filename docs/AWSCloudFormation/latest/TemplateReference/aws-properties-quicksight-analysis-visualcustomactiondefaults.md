---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-visualcustomactiondefaults.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis VisualCustomActionDefaults
<a name="aws-properties-quicksight-analysis-visualcustomactiondefaults"></a>

A list of custom actions applied to visuals in an analysis or sheet.

## Syntax
<a name="aws-properties-quicksight-analysis-visualcustomactiondefaults-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-visualcustomactiondefaults-syntax.json"></a>

```
{
  "[HighlightOperation](#cfn-quicksight-analysis-visualcustomactiondefaults-highlightoperation)" : {{VisualHighlightOperation}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-visualcustomactiondefaults-syntax.yaml"></a>

```
  [HighlightOperation](#cfn-quicksight-analysis-visualcustomactiondefaults-highlightoperation): {{
    VisualHighlightOperation}}
```

## Properties
<a name="aws-properties-quicksight-analysis-visualcustomactiondefaults-properties"></a>

`HighlightOperation`  <a name="cfn-quicksight-analysis-visualcustomactiondefaults-highlightoperation"></a>
A list of highlight operations available for visuals in an analysis or sheet.
*Required*: No
*Type*: [VisualHighlightOperation](aws-properties-quicksight-analysis-visualhighlightoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
