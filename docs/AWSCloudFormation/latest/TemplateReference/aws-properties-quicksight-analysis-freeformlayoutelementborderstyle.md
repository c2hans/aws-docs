---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-freeformlayoutelementborderstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FreeFormLayoutElementBorderStyle
<a name="aws-properties-quicksight-analysis-freeformlayoutelementborderstyle"></a>

The background style configuration of a free-form layout element.

## Syntax
<a name="aws-properties-quicksight-analysis-freeformlayoutelementborderstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-freeformlayoutelementborderstyle-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-freeformlayoutelementborderstyle-color)" : {{String}},
  "[Visibility](#cfn-quicksight-analysis-freeformlayoutelementborderstyle-visibility)" : {{String}},
  "[Width](#cfn-quicksight-analysis-freeformlayoutelementborderstyle-width)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-freeformlayoutelementborderstyle-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-freeformlayoutelementborderstyle-color): {{String}}
  [Visibility](#cfn-quicksight-analysis-freeformlayoutelementborderstyle-visibility): {{String}}
  [Width](#cfn-quicksight-analysis-freeformlayoutelementborderstyle-width): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-freeformlayoutelementborderstyle-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-freeformlayoutelementborderstyle-color"></a>
The border color of a free-form layout element.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-freeformlayoutelementborderstyle-visibility"></a>
The border visibility of a free-form layout element.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Width`  <a name="cfn-quicksight-analysis-freeformlayoutelementborderstyle-width"></a>
The border width of a free-form layout element.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
