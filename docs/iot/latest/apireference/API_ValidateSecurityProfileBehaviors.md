---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ValidateSecurityProfileBehaviors.html
---

# ValidateSecurityProfileBehaviors
<a name="API_ValidateSecurityProfileBehaviors"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Validates a Device Defender security profile behaviors specification.

Requires permission to access the [ValidateSecurityProfileBehaviors](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ValidateSecurityProfileBehaviors_RequestSyntax"></a>

```
POST /security-profile-behaviors/validate HTTP/1.1
Content-type: application/json

{
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
   ]
}
```

## URI Request Parameters
<a name="API_ValidateSecurityProfileBehaviors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ValidateSecurityProfileBehaviors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [behaviors](#API_ValidateSecurityProfileBehaviors_RequestSyntax) **   <a name="iot-ValidateSecurityProfileBehaviors-request-behaviors"></a>
Specifies the behaviors that, when violated by a device (thing), cause an alert.
Type: Array of [Behavior](API_Behavior.md) objects
Array Members: Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_ValidateSecurityProfileBehaviors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "valid": boolean,
   "validationErrors": [
      {
         "errorMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ValidateSecurityProfileBehaviors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [valid](#API_ValidateSecurityProfileBehaviors_ResponseSyntax) **   <a name="iot-ValidateSecurityProfileBehaviors-response-valid"></a>
True if the behaviors were valid.
Type: Boolean

 ** [validationErrors](#API_ValidateSecurityProfileBehaviors_ResponseSyntax) **   <a name="iot-ValidateSecurityProfileBehaviors-response-validationErrors"></a>
The list of any errors found in the behaviors.
Type: Array of [ValidationError](API_ValidationError.md) objects

## Errors
<a name="API_ValidateSecurityProfileBehaviors_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ValidateSecurityProfileBehaviors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ValidateSecurityProfileBehaviors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ValidateSecurityProfileBehaviors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ValidateSecurityProfileBehaviors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ValidateSecurityProfileBehaviors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ValidateSecurityProfileBehaviors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ValidateSecurityProfileBehaviors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ValidateSecurityProfileBehaviors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ValidateSecurityProfileBehaviors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ValidateSecurityProfileBehaviors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ValidateSecurityProfileBehaviors)
