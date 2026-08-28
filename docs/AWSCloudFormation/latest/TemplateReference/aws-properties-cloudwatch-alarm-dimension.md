---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarm-dimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alarm Dimension
<a name="aws-properties-cloudwatch-alarm-dimension"></a>

Dimension is an embedded property of the `AWS::CloudWatch::Alarm` type. Dimensions are name/value pairs that can be associated with a CloudWatch metric. You can specify a maximum of 30 dimensions for a given metric.

## Syntax
<a name="aws-properties-cloudwatch-alarm-dimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarm-dimension-syntax.json"></a>

```
{
  "[Name](#cfn-cloudwatch-alarm-dimension-name)" : {{String}},
  "[Value](#cfn-cloudwatch-alarm-dimension-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarm-dimension-syntax.yaml"></a>

```
  [Name](#cfn-cloudwatch-alarm-dimension-name): {{String}}
  [Value](#cfn-cloudwatch-alarm-dimension-value): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-alarm-dimension-properties"></a>

`Name`  <a name="cfn-cloudwatch-alarm-dimension-name"></a>
The name of the dimension, from 1–255 characters in length. This dimension name must have been included when the metric was published.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudwatch-alarm-dimension-value"></a>
The value for the dimension, from 1–255 characters in length.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-cloudwatch-alarm-dimension--examples"></a>

### Two alarms with dimension values supplied by the Ref function
<a name="aws-properties-cloudwatch-alarm-dimension--examples--Two_alarms_with_dimension_values_supplied_by_the_Ref_function"></a>

The [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html) and [GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html) intrinsic functions are often used to supply values for CloudWatch metric dimensions. Here is an example using the Ref function.

#### JSON
<a name="aws-properties-cloudwatch-alarm-dimension--examples--Two_alarms_with_dimension_values_supplied_by_the_Ref_function--json"></a>

```
{
    "CPUAlarmHigh": {
        "Type": "AWS::CloudWatch::Alarm",
        "Properties": {
            "AlarmDescription": "Scale-up if CPU is greater than 90% for 10 minutes",
            "MetricName": "CPUUtilization",
            "Namespace": "AWS/EC2",
            "Statistic": "Average",
            "Period": "300",
            "EvaluationPeriods": "2",
            "Threshold": "90",
            "AlarmActions": [
                {
                    "Ref": "WebServerScaleUpPolicy"
                }
            ],
            "Dimensions": [
                {
                    "Name": "AutoScalingGroupName",
                    "Value": {
                        "Ref": "WebServerGroup"
                    }
                }
            ],
            "ComparisonOperator": "GreaterThanThreshold"
        }
    },
    "CPUAlarmLow": {
        "Type": "AWS::CloudWatch::Alarm",
        "Properties": {
            "AlarmDescription": "Scale-down if CPU is less than 70% for 10 minutes",
            "MetricName": "CPUUtilization",
            "Namespace": "AWS/EC2",
            "Statistic": "Average",
            "Period": "300",
            "EvaluationPeriods": "2",
            "Threshold": "70",
            "AlarmActions": [
                {
                    "Ref": "WebServerScaleDownPolicy"
                }
            ],
            "Dimensions": [
                {
                    "Name": "AutoScalingGroupName",
                    "Value": {
                        "Ref": "WebServerGroup"
                    }
                }
            ],
            "ComparisonOperator": "LessThanThreshold"
        }
    }
}
```

#### YAML
<a name="aws-properties-cloudwatch-alarm-dimension--examples--Two_alarms_with_dimension_values_supplied_by_the_Ref_function--yaml"></a>

```
CPUAlarmHigh:
  Type: 'AWS::CloudWatch::Alarm'
  Properties:
    AlarmDescription: Scale-up if CPU is greater than 90% for 10 minutes
    MetricName: CPUUtilization
    Namespace: AWS/EC2
    Statistic: Average
    Period: '300'
    EvaluationPeriods: '2'
    Threshold: '90'
    AlarmActions:
      - !Ref WebServerScaleUpPolicy
    Dimensions:
      - Name: AutoScalingGroupName
        Value: !Ref WebServerGroup
    ComparisonOperator: GreaterThanThreshold
CPUAlarmLow:
  Type: 'AWS::CloudWatch::Alarm'
  Properties:
    AlarmDescription: Scale-down if CPU is less than 70% for 10 minutes
    MetricName: CPUUtilization
    Namespace: AWS/EC2
    Statistic: Average
    Period: '300'
    EvaluationPeriods: '2'
    Threshold: '70'
    AlarmActions:
      - !Ref WebServerScaleDownPolicy
    Dimensions:
      - Name: AutoScalingGroupName
        Value: !Ref WebServerGroup
    ComparisonOperator: LessThanThreshold
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
