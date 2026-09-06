---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-dateaxisoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DateAxisOptions
<a name="aws-properties-quicksight-analysis-dateaxisoptions"></a>

The options that determine how a date axis is displayed.

## Syntax
<a name="aws-properties-quicksight-analysis-dateaxisoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-dateaxisoptions-syntax.json"></a>

```
{
  "[MissingDateVisibility](#cfn-quicksight-analysis-dateaxisoptions-missingdatevisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-dateaxisoptions-syntax.yaml"></a>

```
  [MissingDateVisibility](#cfn-quicksight-analysis-dateaxisoptions-missingdatevisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-dateaxisoptions-properties"></a>

`MissingDateVisibility`  <a name="cfn-quicksight-analysis-dateaxisoptions-missingdatevisibility"></a>
Determines whether or not missing dates are displayed.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
