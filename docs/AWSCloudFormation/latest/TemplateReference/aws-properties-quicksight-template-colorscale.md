---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-colorscale.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ColorScale
<a name="aws-properties-quicksight-template-colorscale"></a>

Determines the color scale that is applied to the visual.

## Syntax
<a name="aws-properties-quicksight-template-colorscale-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-colorscale-syntax.json"></a>

```
{
  "[ColorFillType](#cfn-quicksight-template-colorscale-colorfilltype)" : {{String}},
  "[Colors](#cfn-quicksight-template-colorscale-colors)" : {{[ DataColor, ... ]}},
  "[NullValueColor](#cfn-quicksight-template-colorscale-nullvaluecolor)" : {{DataColor}}
}
```

### YAML
<a name="aws-properties-quicksight-template-colorscale-syntax.yaml"></a>

```
  [ColorFillType](#cfn-quicksight-template-colorscale-colorfilltype): {{String}}
  [Colors](#cfn-quicksight-template-colorscale-colors): {{
    - DataColor}}
  [NullValueColor](#cfn-quicksight-template-colorscale-nullvaluecolor): {{
    DataColor}}
```

## Properties
<a name="aws-properties-quicksight-template-colorscale-properties"></a>

`ColorFillType`  <a name="cfn-quicksight-template-colorscale-colorfilltype"></a>
Determines the color fill type.
*Required*: Yes
*Type*: String
*Allowed values*: `DISCRETE | GRADIENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Colors`  <a name="cfn-quicksight-template-colorscale-colors"></a>
Determines the list of colors that are applied to the visual.
*Required*: Yes
*Type*: Array of [DataColor](aws-properties-quicksight-template-datacolor.md)
*Minimum*: `2`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullValueColor`  <a name="cfn-quicksight-template-colorscale-nullvaluecolor"></a>
Determines the color that is applied to null values.
*Required*: No
*Type*: [DataColor](aws-properties-quicksight-template-datacolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
