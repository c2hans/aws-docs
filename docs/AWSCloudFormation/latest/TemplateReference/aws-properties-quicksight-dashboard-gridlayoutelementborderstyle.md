---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-gridlayoutelementborderstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GridLayoutElementBorderStyle
<a name="aws-properties-quicksight-dashboard-gridlayoutelementborderstyle"></a>

The border style configuration of a grid layout element.

## Syntax
<a name="aws-properties-quicksight-dashboard-gridlayoutelementborderstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-gridlayoutelementborderstyle-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-dashboard-gridlayoutelementborderstyle-color)" : {{String}},
  "[Visibility](#cfn-quicksight-dashboard-gridlayoutelementborderstyle-visibility)" : {{String}},
  "[Width](#cfn-quicksight-dashboard-gridlayoutelementborderstyle-width)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-gridlayoutelementborderstyle-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-dashboard-gridlayoutelementborderstyle-color): {{String}}
  [Visibility](#cfn-quicksight-dashboard-gridlayoutelementborderstyle-visibility): {{String}}
  [Width](#cfn-quicksight-dashboard-gridlayoutelementborderstyle-width): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-gridlayoutelementborderstyle-properties"></a>

`Color`  <a name="cfn-quicksight-dashboard-gridlayoutelementborderstyle-color"></a>
The border color of a grid layout element.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-dashboard-gridlayoutelementborderstyle-visibility"></a>
The border visibility of a grid layout element.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Width`  <a name="cfn-quicksight-dashboard-gridlayoutelementborderstyle-width"></a>
The border width of a grid layout element.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
