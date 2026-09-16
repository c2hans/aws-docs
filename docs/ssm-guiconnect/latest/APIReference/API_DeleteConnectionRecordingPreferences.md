---
source_url: https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_DeleteConnectionRecordingPreferences.html
---

# DeleteConnectionRecordingPreferences
<a name="API_DeleteConnectionRecordingPreferences"></a>

Deletes the preferences for recording RDP connections.

## Request Syntax
<a name="API_DeleteConnectionRecordingPreferences_RequestSyntax"></a>

```
POST /DeleteConnectionRecordingPreferences HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteConnectionRecordingPreferences_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteConnectionRecordingPreferences_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_DeleteConnectionRecordingPreferences_RequestSyntax) **   <a name="ssmguiconnect-DeleteConnectionRecordingPreferences-request-ClientToken"></a>
User-provided idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_DeleteConnectionRecordingPreferences_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ClientToken": "string"
}
```

## Response Elements
<a name="API_DeleteConnectionRecordingPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientToken](#API_DeleteConnectionRecordingPreferences_ResponseSyntax) **   <a name="ssmguiconnect-DeleteConnectionRecordingPreferences-response-ClientToken"></a>
Service-provided idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_DeleteConnectionRecordingPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
An error occurred due to a conflict.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Your request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteConnectionRecordingPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-guiconnect-2021-05-01/DeleteConnectionRecordingPreferences)
