---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeSecurityProfile.html
---

# DescribeSecurityProfile
<a name="API_DescribeSecurityProfile"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Gets information about a Device Defender security profile.

Requires permission to access the [DescribeSecurityProfile](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeSecurityProfile_RequestSyntax"></a>

```
GET /security-profiles/{{securityProfileName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeSecurityProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [securityProfileName](#API_DescribeSecurityProfile_RequestSyntax) **   <a name="iot-DescribeSecurityProfile-request-uri-securityProfileName"></a>
The name of the security profile whose information you want to get.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DescribeSecurityProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeSecurityProfile_ResponseSyntax"></a>

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
<a name="API_DescribeSecurityProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [additionalMetricsToRetain](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-additionalMetricsToRetain"></a>
 *This parameter has been deprecated.*
 *Please use [DescribeSecurityProfile:additionalMetricsToRetainV2](#iot-DescribeSecurityProfile-response-additionalMetricsToRetainV2) instead.*
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's `behaviors`, but it is also retained for any metric specified here.
Type: Array of strings

 ** [additionalMetricsToRetainV2](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-additionalMetricsToRetainV2"></a>
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here.
Type: Array of [MetricToRetain](API_MetricToRetain.md) objects

 ** [alertTargets](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-alertTargets"></a>
Where the alerts are sent. (Alerts are always sent to the console.)
Type: String to [AlertTarget](API_AlertTarget.md) object map
Valid Keys: `SNS`

 ** [behaviors](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-behaviors"></a>
Specifies the behaviors that, when violated by a device (thing), cause an alert.
Type: Array of [Behavior](API_Behavior.md) objects
Array Members: Maximum number of 100 items.

 ** [creationDate](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-creationDate"></a>
The time the security profile was created.
Type: Timestamp

 ** [lastModifiedDate](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-lastModifiedDate"></a>
The time the security profile was last modified.
Type: Timestamp

 ** [metricsExportConfig](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-metricsExportConfig"></a>
Specifies the MQTT topic and role ARN required for metric export.
Type: [MetricsExportConfig](API_MetricsExportConfig.md) object

 ** [securityProfileArn](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-securityProfileArn"></a>
The ARN of the security profile.
Type: String

 ** [securityProfileDescription](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-securityProfileDescription"></a>
A description of the security profile (associated with the security profile when it was created or updated).
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\p{Graph}\x20]*`

 ** [securityProfileName](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-securityProfileName"></a>
The name of the security profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [version](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="iot-DescribeSecurityProfile-response-version"></a>
The version of the security profile. A new version is generated whenever the security profile is updated.
Type: Long

## Errors
<a name="API_DescribeSecurityProfile_Errors"></a>

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

## See Also
<a name="API_DescribeSecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeSecurityProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeSecurityProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeSecurityProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeSecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeSecurityProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeSecurityProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeSecurityProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeSecurityProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeSecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeSecurityProfile)
