---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_PutAlarm.html
---

# PutAlarm
<a name="API_PutAlarm"></a>

Creates or updates an alarm, and associates it with the specified metric.

An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see [Alarms in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms).

When this action creates an alarm, the alarm state is immediately set to `INSUFFICIENT_DATA`. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.

When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm. The alarm is then evaluated with the updated configuration.

The `put alarm` operation supports tag-based access control via request tags. For more information, see the [Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags).

## Request Syntax
<a name="API_PutAlarm_RequestSyntax"></a>

```
{
   "alarmName": "{{string}}",
   "comparisonOperator": "{{string}}",
   "contactProtocols": [ "{{string}}" ],
   "datapointsToAlarm": {{number}},
   "evaluationPeriods": {{number}},
   "metricName": "{{string}}",
   "monitoredResourceName": "{{string}}",
   "notificationEnabled": {{boolean}},
   "notificationTriggers": [ "{{string}}" ],
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "threshold": {{number}},
   "treatMissingData": "{{string}}"
}
```

## Request Parameters
<a name="API_PutAlarm_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [alarmName](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-alarmName"></a>
The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [comparisonOperator](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-comparisonOperator"></a>
The arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value is used as the first operand.
Type: String
Valid Values: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold`
Required: Yes

 ** [contactProtocols](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-contactProtocols"></a>
The contact protocols to use for the alarm, such as `Email`, `SMS` (text messaging), or both.
A notification is sent via the specified contact protocol if notifications are enabled for the alarm, and when the alarm is triggered.
A notification is not sent if a contact protocol is not specified, if the specified contact protocol is not configured in the AWS Region, or if notifications are not enabled for the alarm using the `notificationEnabled` paramater.
Use the `CreateContactMethod` action to configure a contact protocol in an AWS Region.
Type: Array of strings
Valid Values: `Email | SMS`
Required: No

 ** [datapointsToAlarm](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-datapointsToAlarm"></a>
The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an "M out of N" alarm, this value (`datapointsToAlarm`) is the M.
Type: Integer
Required: No

 ** [evaluationPeriods](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-evaluationPeriods"></a>
The number of most recent periods over which data is compared to the specified threshold. If you are setting an "M out of N" alarm, this value (`evaluationPeriods`) is the N.
If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies the rolling period of time in which data points are evaluated.
Each evaluation period is five minutes long. For example, specify an evaluation period of 24 to evaluate a metric over a rolling period of two hours.
You can specify a minimum valuation period of 1 (5 minutes), and a maximum evaluation period of 288 (24 hours).
Type: Integer
Required: Yes

 ** [metricName](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-metricName"></a>
The name of the metric to associate with the alarm.
You can configure up to two alarms per metric.
The following metrics are available for each resource type:
+  **Instances**: `BurstCapacityPercentage`, `BurstCapacityTime`, `CPUUtilization`, `NetworkIn`, `NetworkOut`, `StatusCheckFailed`, `StatusCheckFailed_Instance`, and `StatusCheckFailed_System`.
+  **Load balancers**: `ClientTLSNegotiationErrorCount`, `HealthyHostCount`, `UnhealthyHostCount`, `HTTPCode_LB_4XX_Count`, `HTTPCode_LB_5XX_Count`, `HTTPCode_Instance_2XX_Count`, `HTTPCode_Instance_3XX_Count`, `HTTPCode_Instance_4XX_Count`, `HTTPCode_Instance_5XX_Count`, `InstanceResponseTime`, `RejectedConnectionCount`, and `RequestCount`.
+  **Relational databases**: `CPUUtilization`, `DatabaseConnections`, `DiskQueueDepth`, `FreeStorageSpace`, `NetworkReceiveThroughput`, and `NetworkTransmitThroughput`.
For more information about these metrics, see [Metrics available in Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-resource-health-metrics#available-metrics).
Type: String
Valid Values: `CPUUtilization | NetworkIn | NetworkOut | StatusCheckFailed | StatusCheckFailed_Instance | StatusCheckFailed_System | ClientTLSNegotiationErrorCount | HealthyHostCount | UnhealthyHostCount | HTTPCode_LB_4XX_Count | HTTPCode_LB_5XX_Count | HTTPCode_Instance_2XX_Count | HTTPCode_Instance_3XX_Count | HTTPCode_Instance_4XX_Count | HTTPCode_Instance_5XX_Count | InstanceResponseTime | RejectedConnectionCount | RequestCount | DatabaseConnections | DiskQueueDepth | FreeStorageSpace | NetworkReceiveThroughput | NetworkTransmitThroughput | BurstCapacityTime | BurstCapacityPercentage`
Required: Yes

 ** [monitoredResourceName](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-monitoredResourceName"></a>
The name of the Lightsail resource that will be monitored.
Instances, load balancers, and relational databases are the only Lightsail resources that can currently be monitored by alarms.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [notificationEnabled](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-notificationEnabled"></a>
Indicates whether the alarm is enabled.
Notifications are enabled by default if you don't specify this parameter.
Type: Boolean
Required: No

 ** [notificationTriggers](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-notificationTriggers"></a>
The alarm states that trigger a notification.
An alarm has the following possible states:
+  `ALARM` - The metric is outside of the defined threshold.
+  `INSUFFICIENT_DATA` - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.
+  `OK` - The metric is within the defined threshold.
When you specify a notification trigger, the `ALARM` state must be specified. The `INSUFFICIENT_DATA` and `OK` states can be specified in addition to the `ALARM` state.
+ If you specify `OK` as an alarm trigger, a notification is sent when the alarm switches from an `ALARM` or `INSUFFICIENT_DATA` alarm state to an `OK` state. This can be thought of as an *all clear* alarm notification.
+ If you specify `INSUFFICIENT_DATA` as the alarm trigger, a notification is sent when the alarm switches from an `OK` or `ALARM` alarm state to an `INSUFFICIENT_DATA` state.
The notification trigger defaults to `ALARM` if you don't specify this parameter.
Type: Array of strings
Valid Values: `OK | ALARM | INSUFFICIENT_DATA`
Required: No

 ** [tags](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-tags"></a>
The tag keys and optional values to add to the alarm during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [threshold](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-threshold"></a>
The value against which the specified statistic is compared.
Type: Double
Required: Yes

 ** [treatMissingData](#API_PutAlarm_RequestSyntax) **   <a name="Lightsail-PutAlarm-request-treatMissingData"></a>
Sets how this alarm will handle missing data points.
An alarm can treat missing data in the following ways:
+  `breaching` - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.
+  `notBreaching` - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.
+  `ignore` - Ignore the missing data. Maintains the current alarm state.
+  `missing` - Missing data is treated as missing.
If `treatMissingData` is not specified, the default behavior of `missing` is used.
Type: String
Valid Values: `breaching | notBreaching | ignore | missing`
Required: No

## Response Syntax
<a name="API_PutAlarm_ResponseSyntax"></a>

```
{
   "operations": [
      {
         "createdAt": number,
         "errorCode": "string",
         "errorDetails": "string",
         "id": "string",
         "isTerminal": boolean,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "operationDetails": "string",
         "operationType": "string",
         "resourceName": "string",
         "resourceType": "string",
         "status": "string",
         "statusChangedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_PutAlarm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operations](#API_PutAlarm_ResponseSyntax) **   <a name="Lightsail-PutAlarm-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_PutAlarm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_PutAlarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/PutAlarm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/PutAlarm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/PutAlarm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/PutAlarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/PutAlarm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/PutAlarm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/PutAlarm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/PutAlarm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/PutAlarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/PutAlarm)
