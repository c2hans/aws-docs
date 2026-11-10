---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-visualcustomactiondefaults.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template VisualCustomActionDefaults
<a name="aws-properties-quicksight-template-visualcustomactiondefaults"></a>

A list of custom actions applied to visuals in an analysis or sheet.

## Syntax
<a name="aws-properties-quicksight-template-visualcustomactiondefaults-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-visualcustomactiondefaults-syntax.json"></a>

```
{
  "[HighlightOperation](#cfn-quicksight-template-visualcustomactiondefaults-highlightoperation)" : {{VisualHighlightOperation}}
}
```

### YAML
<a name="aws-properties-quicksight-template-visualcustomactiondefaults-syntax.yaml"></a>

```
  [HighlightOperation](#cfn-quicksight-template-visualcustomactiondefaults-highlightoperation): {{
    VisualHighlightOperation}}
```

## Properties
<a name="aws-properties-quicksight-template-visualcustomactiondefaults-properties"></a>

`HighlightOperation`  <a name="cfn-quicksight-template-visualcustomactiondefaults-highlightoperation"></a>
A list of highlight operations available for visuals in an analysis or sheet.
*Required*: No
*Type*: [VisualHighlightOperation](aws-properties-quicksight-template-visualhighlightoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
