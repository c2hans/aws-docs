---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-bordersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis BorderSettings
<a name="aws-properties-quicksight-analysis-bordersettings"></a>

Border settings configuration for visual elements, including visibility, width, and color properties.

## Syntax
<a name="aws-properties-quicksight-analysis-bordersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-bordersettings-syntax.json"></a>

```
{
  "[BorderColor](#cfn-quicksight-analysis-bordersettings-bordercolor)" : {{String}},
  "[BorderVisibility](#cfn-quicksight-analysis-bordersettings-bordervisibility)" : {{String}},
  "[BorderWidth](#cfn-quicksight-analysis-bordersettings-borderwidth)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-bordersettings-syntax.yaml"></a>

```
  [BorderColor](#cfn-quicksight-analysis-bordersettings-bordercolor): {{String}}
  [BorderVisibility](#cfn-quicksight-analysis-bordersettings-bordervisibility): {{String}}
  [BorderWidth](#cfn-quicksight-analysis-bordersettings-borderwidth): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-bordersettings-properties"></a>

`BorderColor`  <a name="cfn-quicksight-analysis-bordersettings-bordercolor"></a>
Color of the border.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BorderVisibility`  <a name="cfn-quicksight-analysis-bordersettings-bordervisibility"></a>
Visibility setting for the border.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BorderWidth`  <a name="cfn-quicksight-analysis-bordersettings-borderwidth"></a>
Width of the border. Valid range is from 1px to 8px.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
