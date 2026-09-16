---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_UpdateOtaTask.html
---

# UpdateOtaTask
<a name="API_UpdateOtaTask"></a>

Update an over-the-air (OTA) task.

## Request Syntax
<a name="API_UpdateOtaTask_RequestSyntax"></a>

```
PUT /ota-tasks/{{Identifier}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "TaskConfigurationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateOtaTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_UpdateOtaTask_RequestSyntax) **   <a name="managedintegrations-UpdateOtaTask-request-uri-Identifier"></a>
The over-the-air (OTA) task id.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateOtaTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateOtaTask_RequestSyntax) **   <a name="managedintegrations-UpdateOtaTask-request-Description"></a>
The description of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** [TaskConfigurationId](#API_UpdateOtaTask_RequestSyntax) **   <a name="managedintegrations-UpdateOtaTask-request-TaskConfigurationId"></a>
The identifier for the over-the-air (OTA) task configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: No

## Response Syntax
<a name="API_UpdateOtaTask_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateOtaTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateOtaTask_Errors"></a>

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
<a name="API_UpdateOtaTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/UpdateOtaTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/UpdateOtaTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/UpdateOtaTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/UpdateOtaTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/UpdateOtaTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/UpdateOtaTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/UpdateOtaTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/UpdateOtaTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/UpdateOtaTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/UpdateOtaTask)
