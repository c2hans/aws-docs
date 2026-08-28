---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateSecurityProfile.html
---

# UpdateSecurityProfile
<a name="API_UpdateSecurityProfile"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Updates a Device Defender security profile.

Requires permission to access the [UpdateSecurityProfile](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateSecurityProfile_RequestSyntax"></a>

```
PATCH /security-profiles/{{securityProfileName}}?expectedVersion={{expectedVersion}} HTTP/1.1
Content-type: application/json

{
   "additionalMetricsToRetain": [ "{{string}}" ],
   "additionalMetricsToRetainV2": [
      {
         "exportMetric": {{boolean}},
         "metric": "{{string}}",
         "metricDimension": {
            "dimensionName": "{{string}}",
            "operator": "{{string}}"
         }
      }
   ],
   "alertTargets": {
      "{{string}}" : {
         "alertTargetArn": "{{string}}",
         "roleArn": "{{string}}"
      }
   },
   "behaviors": [
      {
         "criteria": {
            "comparisonOperator": "{{string}}",
            "consecutiveDatapointsToAlarm": {{number}},
            "consecutiveDatapointsToClear": {{number}},
            "durationSeconds": {{number}},
            "mlDetectionConfig": {
               "confidenceLevel": "{{string}}"
            },
            "statisticalThreshold": {
               "statistic": "{{string}}"
            },
            "value": {
               "cidrs": [ "{{string}}" ],
               "count": {{number}},
               "number": {{number}},
               "numbers": [ {{number}} ],
               "ports": [ {{number}} ],
               "strings": [ "{{string}}" ]
            }
         },
         "exportMetric": {{boolean}},
         "metric": "{{string}}",
         "metricDimension": {
            "dimensionName": "{{string}}",
            "operator": "{{string}}"
         },
         "name": "{{string}}",
         "suppressAlerts": {{boolean}}
      }
   ],
   "deleteAdditionalMetricsToRetain": {{boolean}},
   "deleteAlertTargets": {{boolean}},
   "deleteBehaviors": {{boolean}},
   "deleteMetricsExportConfig": {{boolean}},
   "metricsExportConfig": {
      "mqttTopic": "{{string}}",
      "roleArn": "{{string}}"
   },
   "securityProfileDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSecurityProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [expectedVersion](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-uri-expectedVersion"></a>
The expected version of the security profile. A new version is generated whenever the security profile is updated. If you specify a value that is different from the actual version, a `VersionConflictException` is thrown.

 ** [securityProfileName](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-uri-securityProfileName"></a>
The name of the security profile you want to update.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_UpdateSecurityProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalMetricsToRetain](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-additionalMetricsToRetain"></a>
 *This parameter has been deprecated.*
 *Please use [UpdateSecurityProfile:additionalMetricsToRetainV2](#iot-UpdateSecurityProfile-request-additionalMetricsToRetainV2) instead.*
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's `behaviors`, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.
Type: Array of strings
Required: No

 ** [additionalMetricsToRetainV2](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-additionalMetricsToRetainV2"></a>
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.
Type: Array of [MetricToRetain](API_MetricToRetain.md) objects
Required: No

 ** [alertTargets](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-alertTargets"></a>
Where the alerts are sent. (Alerts are always sent to the console.)
Type: String to [AlertTarget](API_AlertTarget.md) object map
Valid Keys: `SNS`
Required: No

 ** [behaviors](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-behaviors"></a>
Specifies the behaviors that, when violated by a device (thing), cause an alert.
Type: Array of [Behavior](API_Behavior.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** [deleteAdditionalMetricsToRetain](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-deleteAdditionalMetricsToRetain"></a>
If true, delete all `additionalMetricsToRetain` defined for this security profile. If any `additionalMetricsToRetain` are defined in the current invocation, an exception occurs.
Type: Boolean
Required: No

 ** [deleteAlertTargets](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-deleteAlertTargets"></a>
If true, delete all `alertTargets` defined for this security profile. If any `alertTargets` are defined in the current invocation, an exception occurs.
Type: Boolean
Required: No

 ** [deleteBehaviors](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-deleteBehaviors"></a>
If true, delete all `behaviors` defined for this security profile. If any `behaviors` are defined in the current invocation, an exception occurs.
Type: Boolean
Required: No

 ** [deleteMetricsExportConfig](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-deleteMetricsExportConfig"></a>
Set the value as true to delete metrics export related configurations.
Type: Boolean
Required: No

 ** [metricsExportConfig](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-metricsExportConfig"></a>
Specifies the MQTT topic and role ARN required for metric export.
Type: [MetricsExportConfig](API_MetricsExportConfig.md) object
Required: No

 ** [securityProfileDescription](#API_UpdateSecurityProfile_RequestSyntax) **   <a name="iot-UpdateSecurityProfile-request-securityProfileDescription"></a>
A description of the security profile.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\p{Graph}\x20]*`
Required: No

## Response Syntax
<a name="API_UpdateSecurityProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "additionalMetricsToRetain": [ "string" ],
   "additionalMetricsToRetainV2": [
      {
         "exportMetric": boolean,
         "metric": "string",
         "metricDimension": {
            "dimensionName": "string",
            "operator": "string"
         }
      }
   ],
   "alertTargets": {
      "string" : {
         "alertTargetArn": "string",
         "roleArn": "string"
      }
   },
   "behaviors": [
      {
         "criteria": {
            "comparisonOperator": "string",
            "consecutiveDatapointsToAlarm": number,
            "consecutiveDatapointsToClear": number,
            "durationSeconds": number,
            "mlDetectionConfig": {
               "confidenceLevel": "string"
            },
            "statisticalThreshold": {
               "statistic": "string"
            },
            "value": {
               "cidrs": [ "string" ],
               "count": number,
               "number": number,
               "numbers": [ number ],
               "ports": [ number ],
               "strings": [ "string" ]
            }
         },
         "exportMetric": boolean,
         "metric": "string",
         "metricDimension": {
            "dimensionName": "string",
            "operator": "string"
         },
         "name": "string",
         "suppressAlerts": boolean
      }
   ],
   "creationDate": number,
   "lastModifiedDate": number,
   "metricsExportConfig": {
      "mqttTopic": "string",
      "roleArn": "string"
   },
   "securityProfileArn": "string",
   "securityProfileDescription": "string",
   "securityProfileName": "string",
   "version": number
}
```

## Response Elements
<a name="API_UpdateSecurityProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [additionalMetricsToRetain](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-additionalMetricsToRetain"></a>
 *This parameter has been deprecated.*
 *Please use [UpdateSecurityProfile:additionalMetricsToRetainV2](#iot-UpdateSecurityProfile-response-additionalMetricsToRetainV2) instead.*
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the security profile's `behaviors`, but it is also retained for any metric specified here.
Type: Array of strings

 ** [additionalMetricsToRetainV2](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-additionalMetricsToRetainV2"></a>
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.
Type: Array of [MetricToRetain](API_MetricToRetain.md) objects

 ** [alertTargets](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-alertTargets"></a>
Where the alerts are sent. (Alerts are always sent to the console.)
Type: String to [AlertTarget](API_AlertTarget.md) object map
Valid Keys: `SNS`

 ** [behaviors](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-behaviors"></a>
Specifies the behaviors that, when violated by a device (thing), cause an alert.
Type: Array of [Behavior](API_Behavior.md) objects
Array Members: Maximum number of 100 items.

 ** [creationDate](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-creationDate"></a>
The time the security profile was created.
Type: Timestamp

 ** [lastModifiedDate](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-lastModifiedDate"></a>
The time the security profile was last modified.
Type: Timestamp

 ** [metricsExportConfig](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-metricsExportConfig"></a>
Specifies the MQTT topic and role ARN required for metric export.
Type: [MetricsExportConfig](API_MetricsExportConfig.md) object

 ** [securityProfileArn](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-securityProfileArn"></a>
The ARN of the security profile that was updated.
Type: String

 ** [securityProfileDescription](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-securityProfileDescription"></a>
The description of the security profile.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\p{Graph}\x20]*`

 ** [securityProfileName](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-securityProfileName"></a>
The name of the security profile that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [version](#API_UpdateSecurityProfile_ResponseSyntax) **   <a name="iot-UpdateSecurityProfile-response-version"></a>
The updated version of the security profile.
Type: Long

## Errors
<a name="API_UpdateSecurityProfile_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** VersionConflictException **
An exception thrown when the version of an entity specified with the `expectedVersion` parameter does not match the latest version in the system.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_UpdateSecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateSecurityProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateSecurityProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateSecurityProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateSecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateSecurityProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateSecurityProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateSecurityProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateSecurityProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateSecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateSecurityProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
