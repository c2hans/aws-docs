---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-paneltitleoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PanelTitleOptions
<a name="aws-properties-quicksight-template-paneltitleoptions"></a>

The options that determine the title styles for each small multiples panel.

## Syntax
<a name="aws-properties-quicksight-template-paneltitleoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-paneltitleoptions-syntax.json"></a>

```
{
  "[FontConfiguration](#cfn-quicksight-template-paneltitleoptions-fontconfiguration)" : {{FontConfiguration}},
  "[HorizontalTextAlignment](#cfn-quicksight-template-paneltitleoptions-horizontaltextalignment)" : {{String}},
  "[Visibility](#cfn-quicksight-template-paneltitleoptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-paneltitleoptions-syntax.yaml"></a>

```
  [FontConfiguration](#cfn-quicksight-template-paneltitleoptions-fontconfiguration): {{
    FontConfiguration}}
  [HorizontalTextAlignment](#cfn-quicksight-template-paneltitleoptions-horizontaltextalignment): {{String}}
  [Visibility](#cfn-quicksight-template-paneltitleoptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-paneltitleoptions-properties"></a>

`FontConfiguration`  <a name="cfn-quicksight-template-paneltitleoptions-fontconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-template-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HorizontalTextAlignment`  <a name="cfn-quicksight-template-paneltitleoptions-horizontaltextalignment"></a>
Sets the horizontal text alignment of the title within each panel.
*Required*: No
*Type*: String
*Allowed values*: `LEFT | CENTER | RIGHT | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-paneltitleoptions-visibility"></a>
Determines whether or not panel titles are displayed.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
