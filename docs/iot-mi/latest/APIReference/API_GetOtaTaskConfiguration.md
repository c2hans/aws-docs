---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetOtaTaskConfiguration.html
---

# GetOtaTaskConfiguration
<a name="API_GetOtaTaskConfiguration"></a>

Get a configuraiton for the over-the-air (OTA) task.

## Request Syntax
<a name="API_GetOtaTaskConfiguration_RequestSyntax"></a>

```
GET /ota-task-configurations/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOtaTaskConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetOtaTaskConfiguration_RequestSyntax) **   <a name="managedintegrations-GetOtaTaskConfiguration-request-uri-Identifier"></a>
The over-the-air (OTA) task configuration id.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: Yes

## Request Body
<a name="API_GetOtaTaskConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOtaTaskConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "Description": "string",
   "Name": "string",
   "PushConfig": {
      "AbortConfig": {
         "AbortConfigCriteriaList": [
            {
               "Action": "string",
               "FailureType": "string",
               "MinNumberOfExecutedThings": number,
               "ThresholdPercentage": number
            }
         ]
      },
      "RolloutConfig": {
         "ExponentialRolloutRate": {
            "BaseRatePerMinute": number,
            "IncrementFactor": number,
            "RateIncreaseCriteria": {
               "numberOfNotifiedThings": number,
               "numberOfSucceededThings": number
            }
         },
         "MaximumPerMinute": number
      },
      "TimeoutConfig": {
         "InProgressTimeoutInMinutes": number
      }
   },
   "TaskConfigurationId": "string"
}
```

## Response Elements
<a name="API_GetOtaTaskConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_GetOtaTaskConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetOtaTaskConfiguration-response-CreatedAt"></a>
The timestamp value of when the over-the-air (OTA) task configuration was created at.
Type: Timestamp

 ** [Description](#API_GetOtaTaskConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetOtaTaskConfiguration-response-Description"></a>
A description of the over-the-air (OTA) task configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`

 ** [Name](#API_GetOtaTaskConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetOtaTaskConfiguration-response-Name"></a>
The name of the over-the-air (OTA) task configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [PushConfig](#API_GetOtaTaskConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetOtaTaskConfiguration-response-PushConfig"></a>
Describes the type of configuration used for the over-the-air (OTA) task.
Type: [PushConfig](API_PushConfig.md) object

 ** [TaskConfigurationId](#API_GetOtaTaskConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetOtaTaskConfiguration-response-TaskConfigurationId"></a>
The over-the-air (OTA) task configuration id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`

## Errors
<a name="API_GetOtaTaskConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_GetOtaTaskConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetOtaTaskConfiguration)
