---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-fontsize.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FontSize
<a name="aws-properties-quicksight-dashboard-fontsize"></a>

The option that determines the text display size.

## Syntax
<a name="aws-properties-quicksight-dashboard-fontsize-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-fontsize-syntax.json"></a>

```
{
  "[Absolute](#cfn-quicksight-dashboard-fontsize-absolute)" : {{String}},
  "[Relative](#cfn-quicksight-dashboard-fontsize-relative)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-fontsize-syntax.yaml"></a>

```
  [Absolute](#cfn-quicksight-dashboard-fontsize-absolute): {{String}}
  [Relative](#cfn-quicksight-dashboard-fontsize-relative): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-fontsize-properties"></a>

`Absolute`  <a name="cfn-quicksight-dashboard-fontsize-absolute"></a>
The font size that you want to use in px.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Relative`  <a name="cfn-quicksight-dashboard-fontsize-relative"></a>
The lexical name for the text size, proportional to its surrounding context.
*Required*: No
*Type*: String
*Allowed values*: `EXTRA_SMALL | SMALL | MEDIUM | LARGE | EXTRA_LARGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
