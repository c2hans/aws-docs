---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-negativevalueconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard NegativeValueConfiguration
<a name="aws-properties-quicksight-dashboard-negativevalueconfiguration"></a>

The options that determine the negative value configuration.

## Syntax
<a name="aws-properties-quicksight-dashboard-negativevalueconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-negativevalueconfiguration-syntax.json"></a>

```
{
  "[DisplayMode](#cfn-quicksight-dashboard-negativevalueconfiguration-displaymode)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-negativevalueconfiguration-syntax.yaml"></a>

```
  [DisplayMode](#cfn-quicksight-dashboard-negativevalueconfiguration-displaymode): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-negativevalueconfiguration-properties"></a>

`DisplayMode`  <a name="cfn-quicksight-dashboard-negativevalueconfiguration-displaymode"></a>
Determines the display mode of the negative value configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `POSITIVE | NEGATIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
