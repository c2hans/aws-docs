---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-gridlayoutelementborderstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GridLayoutElementBorderStyle
<a name="aws-properties-quicksight-template-gridlayoutelementborderstyle"></a>

The border style configuration of a grid layout element.

## Syntax
<a name="aws-properties-quicksight-template-gridlayoutelementborderstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-gridlayoutelementborderstyle-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-template-gridlayoutelementborderstyle-color)" : {{String}},
  "[Visibility](#cfn-quicksight-template-gridlayoutelementborderstyle-visibility)" : {{String}},
  "[Width](#cfn-quicksight-template-gridlayoutelementborderstyle-width)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-gridlayoutelementborderstyle-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-template-gridlayoutelementborderstyle-color): {{String}}
  [Visibility](#cfn-quicksight-template-gridlayoutelementborderstyle-visibility): {{String}}
  [Width](#cfn-quicksight-template-gridlayoutelementborderstyle-width): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-gridlayoutelementborderstyle-properties"></a>

`Color`  <a name="cfn-quicksight-template-gridlayoutelementborderstyle-color"></a>
The border color of a grid layout element.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-gridlayoutelementborderstyle-visibility"></a>
The border visibility of a grid layout element.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Width`  <a name="cfn-quicksight-template-gridlayoutelementborderstyle-width"></a>
The border width of a grid layout element.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
