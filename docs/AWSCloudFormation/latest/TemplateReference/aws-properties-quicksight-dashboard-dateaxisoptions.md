---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-dateaxisoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DateAxisOptions
<a name="aws-properties-quicksight-dashboard-dateaxisoptions"></a>

The options that determine how a date axis is displayed.

## Syntax
<a name="aws-properties-quicksight-dashboard-dateaxisoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-dateaxisoptions-syntax.json"></a>

```
{
  "[MissingDateVisibility](#cfn-quicksight-dashboard-dateaxisoptions-missingdatevisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dateaxisoptions-syntax.yaml"></a>

```
  [MissingDateVisibility](#cfn-quicksight-dashboard-dateaxisoptions-missingdatevisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-dateaxisoptions-properties"></a>

`MissingDateVisibility`  <a name="cfn-quicksight-dashboard-dateaxisoptions-missingdatevisibility"></a>
Determines whether or not missing dates are displayed.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
