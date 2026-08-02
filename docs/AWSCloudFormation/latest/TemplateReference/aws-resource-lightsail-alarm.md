---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lightsail-alarm.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Alarm
<a name="aws-resource-lightsail-alarm"></a>

The `AWS::Lightsail::Alarm` resource specifies an alarm that can be used to monitor a single metric for one of your Lightsail resources.

## Syntax
<a name="aws-resource-lightsail-alarm-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lightsail-alarm-syntax.json"></a>

```
{
  "Type" : "AWS::Lightsail::Alarm",
  "Properties" : {
      "[AlarmName](#cfn-lightsail-alarm-alarmname)" : {{String}},
      "[ComparisonOperator](#cfn-lightsail-alarm-comparisonoperator)" : {{String}},
      "[ContactProtocols](#cfn-lightsail-alarm-contactprotocols)" : {{[ String, ... ]}},
      "[DatapointsToAlarm](#cfn-lightsail-alarm-datapointstoalarm)" : {{Integer}},
      "[EvaluationPeriods](#cfn-lightsail-alarm-evaluationperiods)" : {{Integer}},
      "[MetricName](#cfn-lightsail-alarm-metricname)" : {{String}},
      "[MonitoredResourceName](#cfn-lightsail-alarm-monitoredresourcename)" : {{String}},
      "[NotificationEnabled](#cfn-lightsail-alarm-notificationenabled)" : {{Boolean}},
      "[NotificationTriggers](#cfn-lightsail-alarm-notificationtriggers)" : {{[ String, ... ]}},
      "[Threshold](#cfn-lightsail-alarm-threshold)" : {{Number}},
      "[TreatMissingData](#cfn-lightsail-alarm-treatmissingdata)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lightsail-alarm-syntax.yaml"></a>

```
Type: AWS::Lightsail::Alarm
Properties:
  [AlarmName](#cfn-lightsail-alarm-alarmname): {{String}}
  [ComparisonOperator](#cfn-lightsail-alarm-comparisonoperator): {{String}}
  [ContactProtocols](#cfn-lightsail-alarm-contactprotocols): {{
    - String}}
  [DatapointsToAlarm](#cfn-lightsail-alarm-datapointstoalarm): {{Integer}}
  [EvaluationPeriods](#cfn-lightsail-alarm-evaluationperiods): {{Integer}}
  [MetricName](#cfn-lightsail-alarm-metricname): {{String}}
  [MonitoredResourceName](#cfn-lightsail-alarm-monitoredresourcename): {{String}}
  [NotificationEnabled](#cfn-lightsail-alarm-notificationenabled): {{Boolean}}
  [NotificationTriggers](#cfn-lightsail-alarm-notificationtriggers): {{
    - String}}
  [Threshold](#cfn-lightsail-alarm-threshold): {{Number}}
  [TreatMissingData](#cfn-lightsail-alarm-treatmissingdata): {{String}}
```

## Properties
<a name="aws-resource-lightsail-alarm-properties"></a>

`AlarmName`  <a name="cfn-lightsail-alarm-alarmname"></a>
The name of the alarm.
*Required*: Yes
*Type*: String
*Pattern*: `\w[\w\-]*\w`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComparisonOperator`  <a name="cfn-lightsail-alarm-comparisonoperator"></a>
The arithmetic operation to use when comparing the specified statistic and threshold.
*Required*: Yes
*Type*: String
*Allowed values*: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContactProtocols`  <a name="cfn-lightsail-alarm-contactprotocols"></a>
The contact protocols for the alarm, such as `Email`, `SMS` (text messaging), or both.
*Allowed Values*: `Email` \| `SMS`
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatapointsToAlarm`  <a name="cfn-lightsail-alarm-datapointstoalarm"></a>
The number of data points within the evaluation periods that must be breaching to cause the alarm to go to the `ALARM` state.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluationPeriods`  <a name="cfn-lightsail-alarm-evaluationperiods"></a>
The number of periods over which data is compared to the specified threshold.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-lightsail-alarm-metricname"></a>
The name of the metric associated with the alarm.
*Required*: Yes
*Type*: String
*Allowed values*: `CPUUtilization | NetworkIn | NetworkOut | StatusCheckFailed | StatusCheckFailed_Instance | StatusCheckFailed_System | ClientTLSNegotiationErrorCount | HealthyHostCount | UnhealthyHostCount | HTTPCode_LB_4XX_Count | HTTPCode_LB_5XX_Count | HTTPCode_Instance_2XX_Count | HTTPCode_Instance_3XX_Count | HTTPCode_Instance_4XX_Count | HTTPCode_Instance_5XX_Count | InstanceResponseTime | RejectedConnectionCount | RequestCount | DatabaseConnections | DiskQueueDepth | FreeStorageSpace | NetworkReceiveThroughput | NetworkTransmitThroughput | BurstCapacityTime | BurstCapacityPercentage`
*Update requires*: Updates are not supported.

`MonitoredResourceName`  <a name="cfn-lightsail-alarm-monitoredresourcename"></a>
The name of the Lightsail resource that the alarm monitors.
*Required*: Yes
*Type*: String
*Update requires*: Updates are not supported.

`NotificationEnabled`  <a name="cfn-lightsail-alarm-notificationenabled"></a>
A Boolean value indicating whether the alarm is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationTriggers`  <a name="cfn-lightsail-alarm-notificationtriggers"></a>
The alarm states that trigger a notification.
To specify the `OK` and `INSUFFICIENT_DATA` values, you must also specify `ContactProtocols` values. Otherwise, the `OK` and `INSUFFICIENT_DATA` values will not take effect and the stack will drift.
*Allowed Values*: `OK` \| `ALARM` \| `INSUFFICIENT_DATA`
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Threshold`  <a name="cfn-lightsail-alarm-threshold"></a>
The value against which the specified statistic is compared.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TreatMissingData`  <a name="cfn-lightsail-alarm-treatmissingdata"></a>
Specifies how the alarm handles missing data points.
An alarm can treat missing data in the following ways:
+ `breaching` - Assumes the missing data is not within the threshold. Missing data counts towards the number of times that the metric is not within the threshold.
+ `notBreaching` - Assumes the missing data is within the threshold. Missing data does not count towards the number of times that the metric is not within the threshold.
+ `ignore` - Ignores the missing data. Maintains the current alarm state.
+ `missing` - Missing data is treated as missing.
*Required*: No
*Type*: String
*Allowed values*: `breaching | notBreaching | ignore | missing`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lightsail-alarm-return-values"></a>

### Ref
<a name="aws-resource-lightsail-alarm-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a unique identifier for this resource.

### Fn::GetAtt
<a name="aws-resource-lightsail-alarm-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lightsail-alarm-return-values-fn--getatt-fn--getatt"></a>

`AlarmArn`  <a name="AlarmArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the alarm.

`State`  <a name="State-fn::getatt"></a>
The current state of the alarm.
An alarm has the following possible states:
+ `ALARM` - The metric is outside of the defined threshold.
+ `INSUFFICIENT_DATA` - The alarm has recently started, the metric is not available, or not enough data is available for the metric to determine the alarm state.
+ `OK` - The metric is within the defined threshold.

## Remarks
<a name="aws-resource-lightsail-alarm--remarks"></a>

 *Notification triggers*

To specify the `OK` and `INSUFFICIENT_DATA` values of the `NotificationTriggers` parameter, you must also specify `ContactProtocols` values. Otherwise, the `OK` and `INSUFFICIENT_DATA` values of the `NotificationTriggers` parameter will not take effect and the stack will drift.
