---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Alarm.html
---

# Alarm
<a name="API_Alarm"></a>

Describes an alarm.

An alarm is a way to monitor your Lightsail resource metrics. For more information, see [Alarms in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms).

## Contents
<a name="API_Alarm_Contents"></a>

 ** arn **   <a name="Lightsail-Type-Alarm-arn"></a>
The Amazon Resource Name (ARN) of the alarm.
Type: String
Pattern: `.*\S.*`
Required: No

 ** comparisonOperator **   <a name="Lightsail-Type-Alarm-comparisonOperator"></a>
The arithmetic operation used when comparing the specified statistic and threshold.
Type: String
Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold`
Required: No

 ** contactProtocols **   <a name="Lightsail-Type-Alarm-contactProtocols"></a>
The contact protocols for the alarm, such as `Email`, `SMS` (text messaging), or both.
Type: Array of strings
Valid Values: `Email | SMS`
Required: No

 ** createdAt **   <a name="Lightsail-Type-Alarm-createdAt"></a>
The timestamp when the alarm was created.
Type: Timestamp
Required: No

 ** datapointsToAlarm **   <a name="Lightsail-Type-Alarm-datapointsToAlarm"></a>
The number of data points that must not within the specified threshold to trigger the alarm.
Type: Integer
Required: No

 ** evaluationPeriods **   <a name="Lightsail-Type-Alarm-evaluationPeriods"></a>
The number of periods over which data is compared to the specified threshold.
Type: Integer
Required: No

 ** location **   <a name="Lightsail-Type-Alarm-location"></a>
An object that lists information about the location of the alarm.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** metricName **   <a name="Lightsail-Type-Alarm-metricName"></a>
The name of the metric associated with the alarm.
Type: String
Valid Values: `CPUUtilization | NetworkIn | NetworkOut | StatusCheckFailed | StatusCheckFailed_Instance | StatusCheckFailed_System | ClientTLSNegotiationErrorCount | HealthyHostCount | UnhealthyHostCount | HTTPCode_LB_4XX_Count | HTTPCode_LB_5XX_Count | HTTPCode_Instance_2XX_Count | HTTPCode_Instance_3XX_Count | HTTPCode_Instance_4XX_Count | HTTPCode_Instance_5XX_Count | InstanceResponseTime | RejectedConnectionCount | RequestCount | DatabaseConnections | DiskQueueDepth | FreeStorageSpace | NetworkReceiveThroughput | NetworkTransmitThroughput | FreeableMemory | SwapUsage | BurstCapacityTime | BurstCapacityPercentage`
Required: No

 ** monitoredResourceInfo **   <a name="Lightsail-Type-Alarm-monitoredResourceInfo"></a>
An object that lists information about the resource monitored by the alarm.
Type: [MonitoredResourceInfo](API_MonitoredResourceInfo.md) object
Required: No

 ** name **   <a name="Lightsail-Type-Alarm-name"></a>
The name of the alarm.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** notificationEnabled **   <a name="Lightsail-Type-Alarm-notificationEnabled"></a>
Indicates whether the alarm is enabled.
Type: Boolean
Required: No

 ** notificationTriggers **   <a name="Lightsail-Type-Alarm-notificationTriggers"></a>
The alarm states that trigger a notification.
Type: Array of strings
Valid Values: `OK | ALARM | INSUFFICIENT_DATA`
Required: No

 ** period **   <a name="Lightsail-Type-Alarm-period"></a>
The period, in seconds, over which the statistic is applied.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: No

 ** resourceType **   <a name="Lightsail-Type-Alarm-resourceType"></a>
The Lightsail resource type of the alarm.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** state **   <a name="Lightsail-Type-Alarm-state"></a>
The current state of the alarm.
An alarm has the following possible states:
+  `ALARM` - The metric is outside of the defined threshold.
+  `INSUFFICIENT_DATA` - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.
+  `OK` - The metric is within the defined threshold.
Type: String
Valid Values: `OK | ALARM | INSUFFICIENT_DATA`
Required: No

 ** statistic **   <a name="Lightsail-Type-Alarm-statistic"></a>
The statistic for the metric associated with the alarm.
The following statistics are available:
+  `Minimum` - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.
+  `Maximum` - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.
+  `Sum` - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.
+  `Average` - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.
+  `SampleCount` - The count, or number, of data points used for the statistical calculation.
Type: String
Valid Values: `Minimum | Maximum | Sum | Average | SampleCount`
Required: No

 ** supportCode **   <a name="Lightsail-Type-Alarm-supportCode"></a>
The support code. Include this code in your email to support when you have questions about your Lightsail alarm. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-Alarm-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** threshold **   <a name="Lightsail-Type-Alarm-threshold"></a>
The value against which the specified statistic is compared.
Type: Double
Required: No

 ** treatMissingData **   <a name="Lightsail-Type-Alarm-treatMissingData"></a>
Specifies how the alarm handles missing data points.
An alarm can treat missing data in the following ways:
+  `breaching` - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.
+  `notBreaching` - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.
+  `ignore` - Ignore the missing data. Maintains the current alarm state.
+  `missing` - Missing data is treated as missing.
Type: String
Valid Values: `breaching | notBreaching | ignore | missing`
Required: No

 ** unit **   <a name="Lightsail-Type-Alarm-unit"></a>
The unit of the metric associated with the alarm.
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
Required: No

## See Also
<a name="API_Alarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Alarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Alarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Alarm)
