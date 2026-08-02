---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-percentvisiblerange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard PercentVisibleRange
<a name="aws-properties-quicksight-dashboard-percentvisiblerange"></a>

The percent range in the visible range.

## Syntax
<a name="aws-properties-quicksight-dashboard-percentvisiblerange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-percentvisiblerange-syntax.json"></a>

```
{
  "[From](#cfn-quicksight-dashboard-percentvisiblerange-from)" : {{Number}},
  "[To](#cfn-quicksight-dashboard-percentvisiblerange-to)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-percentvisiblerange-syntax.yaml"></a>

```
  [From](#cfn-quicksight-dashboard-percentvisiblerange-from): {{Number}}
  [To](#cfn-quicksight-dashboard-percentvisiblerange-to): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-percentvisiblerange-properties"></a>

`From`  <a name="cfn-quicksight-dashboard-percentvisiblerange-from"></a>
The lower bound of the range.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`To`  <a name="cfn-quicksight-dashboard-percentvisiblerange-to"></a>
The top bound of the range.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
