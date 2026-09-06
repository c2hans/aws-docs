---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateOtaTaskConfiguration.html
---

# CreateOtaTaskConfiguration
<a name="API_CreateOtaTaskConfiguration"></a>

Create a configuraiton for the over-the-air (OTA) task.

## Request Syntax
<a name="API_CreateOtaTaskConfiguration_RequestSyntax"></a>

```
POST /ota-task-configurations HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "PushConfig": {
      "AbortConfig": {
         "AbortConfigCriteriaList": [
            {
               "Action": "{{string}}",
               "FailureType": "{{string}}",
               "MinNumberOfExecutedThings": {{number}},
               "ThresholdPercentage": {{number}}
            }
         ]
      },
      "RolloutConfig": {
         "ExponentialRolloutRate": {
            "BaseRatePerMinute": {{number}},
            "IncrementFactor": {{number}},
            "RateIncreaseCriteria": {
               "numberOfNotifiedThings": {{number}},
               "numberOfSucceededThings": {{number}}
            }
         },
         "MaximumPerMinute": {{number}}
      },
      "TimeoutConfig": {
         "InProgressTimeoutInMinutes": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateOtaTaskConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateOtaTaskConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateOtaTaskConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateOtaTaskConfiguration-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [Description](#API_CreateOtaTaskConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateOtaTaskConfiguration-request-Description"></a>
A description of the over-the-air (OTA) task configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** [Name](#API_CreateOtaTaskConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateOtaTaskConfiguration-request-Name"></a>
The name of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** [PushConfig](#API_CreateOtaTaskConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateOtaTaskConfiguration-request-PushConfig"></a>
Describes the type of configuration used for the over-the-air (OTA) task.
Type: [PushConfig](API_PushConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateOtaTaskConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "TaskConfigurationId": "string"
}
```

## Response Elements
<a name="API_CreateOtaTaskConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [TaskConfigurationId](#API_CreateOtaTaskConfiguration_ResponseSyntax) **   <a name="managedintegrations-CreateOtaTaskConfiguration-response-TaskConfigurationId"></a>
The identifier of the over-the-air (OTA) task configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`

## Errors
<a name="API_CreateOtaTaskConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict with the request.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_CreateOtaTaskConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateOtaTaskConfiguration)
