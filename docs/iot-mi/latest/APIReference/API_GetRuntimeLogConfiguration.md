---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetRuntimeLogConfiguration.html
---

# GetRuntimeLogConfiguration
<a name="API_GetRuntimeLogConfiguration"></a>

Get the runtime log configuration for a specific managed thing.

## Request Syntax
<a name="API_GetRuntimeLogConfiguration_RequestSyntax"></a>

```
GET /runtime-log-configurations/{{ManagedThingId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRuntimeLogConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ManagedThingId](#API_GetRuntimeLogConfiguration_RequestSyntax) **   <a name="managedintegrations-GetRuntimeLogConfiguration-request-uri-ManagedThingId"></a>
The id for a managed thing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Request Body
<a name="API_GetRuntimeLogConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRuntimeLogConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ManagedThingId": "string",
   "RuntimeLogConfigurations": {
      "DeleteLocalStoreAfterUpload": boolean,
      "LocalStoreFileRotationMaxBytes": number,
      "LocalStoreFileRotationMaxFiles": number,
      "LocalStoreLocation": "string",
      "LogFlushLevel": "string",
      "LogLevel": "string",
      "UploadLog": boolean,
      "UploadPeriodMinutes": number
   }
}
```

## Response Elements
<a name="API_GetRuntimeLogConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagedThingId](#API_GetRuntimeLogConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetRuntimeLogConfiguration-response-ManagedThingId"></a>
The id for a managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`

 ** [RuntimeLogConfigurations](#API_GetRuntimeLogConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetRuntimeLogConfiguration-response-RuntimeLogConfigurations"></a>
The runtime log configuration for a managed thing.
Type: [RuntimeLogConfigurations](API_RuntimeLogConfigurations.md) object

## Errors
<a name="API_GetRuntimeLogConfiguration_Errors"></a>

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
<a name="API_GetRuntimeLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetRuntimeLogConfiguration)
