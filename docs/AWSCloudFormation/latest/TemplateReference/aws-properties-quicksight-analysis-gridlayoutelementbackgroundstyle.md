---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-gridlayoutelementbackgroundstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GridLayoutElementBackgroundStyle
<a name="aws-properties-quicksight-analysis-gridlayoutelementbackgroundstyle"></a>

The background style configuration of a grid layout element.

## Syntax
<a name="aws-properties-quicksight-analysis-gridlayoutelementbackgroundstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-gridlayoutelementbackgroundstyle-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-gridlayoutelementbackgroundstyle-color)" : {{String}},
  "[Visibility](#cfn-quicksight-analysis-gridlayoutelementbackgroundstyle-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-gridlayoutelementbackgroundstyle-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-gridlayoutelementbackgroundstyle-color): {{String}}
  [Visibility](#cfn-quicksight-analysis-gridlayoutelementbackgroundstyle-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-gridlayoutelementbackgroundstyle-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-gridlayoutelementbackgroundstyle-color"></a>
The background color of a grid layout element.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-gridlayoutelementbackgroundstyle-visibility"></a>
The background visibility of a grid layout element.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
