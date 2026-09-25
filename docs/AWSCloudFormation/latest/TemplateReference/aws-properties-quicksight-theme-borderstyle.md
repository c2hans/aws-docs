---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-borderstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme BorderStyle
<a name="aws-properties-quicksight-theme-borderstyle"></a>

The display options for tile borders for visuals.

## Syntax
<a name="aws-properties-quicksight-theme-borderstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-borderstyle-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-theme-borderstyle-color)" : {{String}},
  "[Show](#cfn-quicksight-theme-borderstyle-show)" : {{Boolean}},
  "[Width](#cfn-quicksight-theme-borderstyle-width)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-borderstyle-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-theme-borderstyle-color): {{String}}
  [Show](#cfn-quicksight-theme-borderstyle-show): {{Boolean}}
  [Width](#cfn-quicksight-theme-borderstyle-width): {{String}}
```

## Properties
<a name="aws-properties-quicksight-theme-borderstyle-properties"></a>

`Color`  <a name="cfn-quicksight-theme-borderstyle-color"></a>
The option to add color for tile borders for visuals.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Show`  <a name="cfn-quicksight-theme-borderstyle-show"></a>
The option to enable display of borders for visuals.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Width`  <a name="cfn-quicksight-theme-borderstyle-width"></a>
The option to set the width of tile borders for visuals.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
