---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alert-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert Condition
<a name="aws-properties-cloudwatch-alert-condition"></a>

The thresholds that set the alert's state. Specify at least one of WarningThreshold and CriticalThreshold.

## Syntax
<a name="aws-properties-cloudwatch-alert-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alert-condition-syntax.json"></a>

```
{
  "[Comparator](#cfn-cloudwatch-alert-condition-comparator)" : {{String}},
  "[CriticalThreshold](#cfn-cloudwatch-alert-condition-criticalthreshold)" : {{Number}},
  "[ThresholdField](#cfn-cloudwatch-alert-condition-thresholdfield)" : {{String}},
  "[ThresholdMode](#cfn-cloudwatch-alert-condition-thresholdmode)" : {{String}},
  "[WarningThreshold](#cfn-cloudwatch-alert-condition-warningthreshold)" : {{Number}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alert-condition-syntax.yaml"></a>

```
  [Comparator](#cfn-cloudwatch-alert-condition-comparator): {{String}}
  [CriticalThreshold](#cfn-cloudwatch-alert-condition-criticalthreshold): {{Number}}
  [ThresholdField](#cfn-cloudwatch-alert-condition-thresholdfield): {{String}}
  [ThresholdMode](#cfn-cloudwatch-alert-condition-thresholdmode): {{String}}
  [WarningThreshold](#cfn-cloudwatch-alert-condition-warningthreshold): {{Number}}
```

## Properties
<a name="aws-properties-cloudwatch-alert-condition-properties"></a>

`Comparator`  <a name="cfn-cloudwatch-alert-condition-comparator"></a>
The comparison operator. Valid values: GT, GTE, LT, LTE (greater than, greater than or equal to, less than, less than or equal to).
*Required*: No
*Type*: String
*Allowed values*: `GT | LT | GTE | LTE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CriticalThreshold`  <a name="cfn-cloudwatch-alert-condition-criticalthreshold"></a>
The value at which the alert enters the CRITICAL state.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdField`  <a name="cfn-cloudwatch-alert-condition-thresholdfield"></a>
The result field to compare against the threshold. Required when ThresholdMode is FIELD\_VALUE.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdMode`  <a name="cfn-cloudwatch-alert-condition-thresholdmode"></a>
How the threshold is applied. COUNT\_OF\_RESULTS compares the number of rows the query returns. FIELD\_VALUE compares the value of ThresholdField in each result row; each row is tracked separately.
*Required*: No
*Type*: String
*Allowed values*: `COUNT_OF_RESULTS | FIELD_VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WarningThreshold`  <a name="cfn-cloudwatch-alert-condition-warningthreshold"></a>
The value at which the alert enters the WARNING state.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
