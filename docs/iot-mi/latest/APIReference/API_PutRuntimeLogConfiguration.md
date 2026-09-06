---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_PutRuntimeLogConfiguration.html
---

# PutRuntimeLogConfiguration
<a name="API_PutRuntimeLogConfiguration"></a>

Set the runtime log configuration for a specific managed thing.

## Request Syntax
<a name="API_PutRuntimeLogConfiguration_RequestSyntax"></a>

```
PUT /runtime-log-configurations/{{ManagedThingId}} HTTP/1.1
Content-type: application/json

{
   "RuntimeLogConfigurations": {
      "DeleteLocalStoreAfterUpload": {{boolean}},
      "LocalStoreFileRotationMaxBytes": {{number}},
      "LocalStoreFileRotationMaxFiles": {{number}},
      "LocalStoreLocation": "{{string}}",
      "LogFlushLevel": "{{string}}",
      "LogLevel": "{{string}}",
      "UploadLog": {{boolean}},
      "UploadPeriodMinutes": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_PutRuntimeLogConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ManagedThingId](#API_PutRuntimeLogConfiguration_RequestSyntax) **   <a name="managedintegrations-PutRuntimeLogConfiguration-request-uri-ManagedThingId"></a>
The id for a managed thing.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: Yes

## Request Body
<a name="API_PutRuntimeLogConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RuntimeLogConfigurations](#API_PutRuntimeLogConfiguration_RequestSyntax) **   <a name="managedintegrations-PutRuntimeLogConfiguration-request-RuntimeLogConfigurations"></a>
The runtime log configuration for a managed thing.
Type: [RuntimeLogConfigurations](API_RuntimeLogConfigurations.md) object
Required: Yes

## Response Syntax
<a name="API_PutRuntimeLogConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutRuntimeLogConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutRuntimeLogConfiguration_Errors"></a>

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
<a name="API_PutRuntimeLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/PutRuntimeLogConfiguration)
