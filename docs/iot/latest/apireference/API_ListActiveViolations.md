---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListActiveViolations.html
---

# ListActiveViolations
<a name="API_ListActiveViolations"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Lists the active violations for a given Device Defender security profile.

Requires permission to access the [ListActiveViolations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListActiveViolations_RequestSyntax"></a>

```
GET /active-violations?behaviorCriteriaType={{behaviorCriteriaType}}&listSuppressedAlerts={{listSuppressedAlerts}}&maxResults={{maxResults}}&nextToken={{nextToken}}&securityProfileName={{securityProfileName}}&thingName={{thingName}}&verificationState={{verificationState}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListActiveViolations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [behaviorCriteriaType](#API_ListActiveViolations_RequestSyntax) **   <a name="iot-ListActiveViolations-request-uri-behaviorCriteriaType"></a>
 The criteria for a behavior.
Valid Values: `STATIC | STATISTICAL | MACHINE_LEARNING`

 ** [listSuppressedAlerts](#API_ListActiveViolations_RequestSyntax) **   <a name="iot-ListActiveViolations-request-uri-listSuppressedAlerts"></a>
 A list of all suppressed alerts.

 ** [maxResults](#API_ListActiveViolations_RequestSyntax) **   <a name="iot-ListActiveViolations-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListActiveViolations_RequestSyntax) **   <a name="iot-ListActiveViolations-request-uri-nextToken"></a>
The token for the next set of results.

 ** [securityProfileName](#API_ListActiveViolations_RequestSyntax) **   <a name="iot-ListActiveViolations-request-uri-securityProfileName"></a>
The name of the Device Defender security profile for which violations are listed.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [thingName](#API_ListActiveViolations_RequestSyntax) **   <a name="iot-ListActiveViolations-request-uri-thingName"></a>
The name of the thing whose active violations are listed.
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [verificationState](#API_ListActiveViolations_RequestSyntax) **   <a name="iot-ListActiveViolations-request-uri-verificationState"></a>
The verification state of the violation (detect alarm).
Valid Values: `FALSE_POSITIVE | BENIGN_POSITIVE | TRUE_POSITIVE | UNKNOWN`

## Request Body
<a name="API_ListActiveViolations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListActiveViolations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "activeViolations": [
      {
         "behavior": {
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
         },
         "lastViolationTime": number,
         "lastViolationValue": {
            "cidrs": [ "string" ],
            "count": number,
            "number": number,
            "numbers": [ number ],
            "ports": [ number ],
            "strings": [ "string" ]
         },
         "securityProfileName": "string",
         "thingName": "string",
         "verificationState": "string",
         "verificationStateDescription": "string",
         "violationEventAdditionalInfo": {
            "confidenceLevel": "string"
         },
         "violationId": "string",
         "violationStartTime": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListActiveViolations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activeViolations](#API_ListActiveViolations_ResponseSyntax) **   <a name="iot-ListActiveViolations-response-activeViolations"></a>
The list of active violations.
Type: Array of [ActiveViolation](API_ActiveViolation.md) objects

 ** [nextToken](#API_ListActiveViolations_ResponseSyntax) **   <a name="iot-ListActiveViolations-response-nextToken"></a>
A token that can be used to retrieve the next set of results, or `null` if there are no additional results.
Type: String

## Errors
<a name="API_ListActiveViolations_Errors"></a>

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
<a name="API_ListActiveViolations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListActiveViolations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListActiveViolations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListActiveViolations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListActiveViolations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListActiveViolations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListActiveViolations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListActiveViolations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListActiveViolations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListActiveViolations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListActiveViolations)
