---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateSecurityProfile.html
---

# CreateSecurityProfile
<a name="API_CreateSecurityProfile"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Creates a Device Defender security profile.

Requires permission to access the [CreateSecurityProfile](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateSecurityProfile_RequestSyntax"></a>

```
POST /security-profiles/{{securityProfileName}} HTTP/1.1
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
   "metricsExportConfig": {
      "mqttTopic": "{{string}}",
      "roleArn": "{{string}}"
   },
   "securityProfileDescription": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateSecurityProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [securityProfileName](#API_CreateSecurityProfile_RequestSyntax) **   <a name="iot-CreateSecurityProfile-request-uri-securityProfileName"></a>
The name you are giving to the security profile.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_CreateSecurityProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalMetricsToRetain](#API_CreateSecurityProfile_RequestSyntax) **   <a name="iot-CreateSecurityProfile-request-additionalMetricsToRetain"></a>
 *This parameter has been deprecated.*
 *Please use [CreateSecurityProfile:additionalMetricsToRetainV2](#iot-CreateSecurityProfile-request-additionalMetricsToRetainV2) instead.*
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's `behaviors`, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.
Type: Array of strings
Required: No

 ** [additionalMetricsToRetainV2](#API_CreateSecurityProfile_RequestSyntax) **   <a name="iot-CreateSecurityProfile-request-additionalMetricsToRetainV2"></a>
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's `behaviors`, but it is also retained for any metric specified here. Can be used with custom metrics; cannot be used with dimensions.
Type: Array of [MetricToRetain](API_MetricToRetain.md) objects
Required: No

 ** [alertTargets](#API_CreateSecurityProfile_RequestSyntax) **   <a name="iot-CreateSecurityProfile-request-alertTargets"></a>
Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.
Type: String to [AlertTarget](API_AlertTarget.md) object map
Valid Keys: `SNS`
Required: No

 ** [behaviors](#API_CreateSecurityProfile_RequestSyntax) **   <a name="iot-CreateSecurityProfile-request-behaviors"></a>
Specifies the behaviors that, when violated by a device (thing), cause an alert.
Type: Array of [Behavior](API_Behavior.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** [metricsExportConfig](#API_CreateSecurityProfile_RequestSyntax) **   <a name="iot-CreateSecurityProfile-request-metricsExportConfig"></a>
Specifies the MQTT topic and role ARN required for metric export.
Type: [MetricsExportConfig](API_MetricsExportConfig.md) object
Required: No

 ** [securityProfileDescription](#API_CreateSecurityProfile_RequestSyntax) **   <a name="iot-CreateSecurityProfile-request-securityProfileDescription"></a>
A description of the security profile.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\p{Graph}\x20]*`
Required: No

 ** [tags](#API_CreateSecurityProfile_RequestSyntax) **   <a name="iot-CreateSecurityProfile-request-tags"></a>
Metadata that can be used to manage the security profile.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateSecurityProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "securityProfileArn": "string",
   "securityProfileName": "string"
}
```

## Response Elements
<a name="API_CreateSecurityProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [securityProfileArn](#API_CreateSecurityProfile_ResponseSyntax) **   <a name="iot-CreateSecurityProfile-response-securityProfileArn"></a>
The ARN of the security profile.
Type: String

 ** [securityProfileName](#API_CreateSecurityProfile_ResponseSyntax) **   <a name="iot-CreateSecurityProfile-response-securityProfileName"></a>
The name you gave to the security profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Errors
<a name="API_CreateSecurityProfile_Errors"></a>

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

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateSecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateSecurityProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateSecurityProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateSecurityProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateSecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateSecurityProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateSecurityProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateSecurityProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateSecurityProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateSecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateSecurityProfile)
