---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ImportDocument.html
---

# ImportDocument
<a name="API_qapps_ImportDocument"></a>

Uploads a file that can then be used either as a default in a `FileUploadCard` from Q App definition or as a file that is used inside a single Q App run. The purpose of the document is determined by a scope parameter that indicates whether it is at the app definition level or at the app session level.

## Request Syntax
<a name="API_qapps_ImportDocument_RequestSyntax"></a>

```
POST /apps.importDocument HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "appId": "{{string}}",
   "cardId": "{{string}}",
   "fileContentsBase64": "{{string}}",
   "fileName": "{{string}}",
   "scope": "{{string}}",
   "sessionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_qapps_ImportDocument_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_ImportDocument_RequestSyntax) **   <a name="qbusiness-qapps_ImportDocument-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_ImportDocument_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appId](#API_qapps_ImportDocument_RequestSyntax) **   <a name="qbusiness-qapps_ImportDocument-request-appId"></a>
The unique identifier of the Q App the file is associated with.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [cardId](#API_qapps_ImportDocument_RequestSyntax) **   <a name="qbusiness-qapps_ImportDocument-request-cardId"></a>
The unique identifier of the card the file is associated with.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [fileContentsBase64](#API_qapps_ImportDocument_RequestSyntax) **   <a name="qbusiness-qapps_ImportDocument-request-fileContentsBase64"></a>
The base64-encoded contents of the file to upload.
Type: String
Required: Yes

 ** [fileName](#API_qapps_ImportDocument_RequestSyntax) **   <a name="qbusiness-qapps_ImportDocument-request-fileName"></a>
The name of the file being uploaded.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: Yes

 ** [scope](#API_qapps_ImportDocument_RequestSyntax) **   <a name="qbusiness-qapps_ImportDocument-request-scope"></a>
Whether the file is associated with a Q App definition or a specific Q App session.
Type: String
Valid Values: `APPLICATION | SESSION`
Required: Yes

 ** [sessionId](#API_qapps_ImportDocument_RequestSyntax) **   <a name="qbusiness-qapps_ImportDocument-request-sessionId"></a>
The unique identifier of the Q App session the file is associated with, if applicable.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: No

## Response Syntax
<a name="API_qapps_ImportDocument_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fileId": "string"
}
```

## Response Elements
<a name="API_qapps_ImportDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fileId](#API_qapps_ImportDocument_ResponseSyntax) **   <a name="qbusiness-qapps_ImportDocument-response-fileId"></a>
The unique identifier assigned to the uploaded file.
Type: String

## Errors
<a name="API_qapps_ImportDocument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

 ** ContentTooLargeException **
The requested operation could not be completed because the content exceeds the maximum allowed size.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 413

 ** InternalServerException **
An internal service error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The requested operation could not be completed because it would exceed the service's quota or limit.
 ** quotaCode **
The code of the quota that was exceeded
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
 ** serviceCode **
The code for the service where the quota was exceeded
HTTP Status Code: 402

 ** ThrottlingException **
The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.
 ** quotaCode **
The code of the quota that was exceeded
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
 ** serviceCode **
The code for the service where the quota was exceeded
HTTP Status Code: 429

 ** UnauthorizedException **
The client is not authenticated or authorized to perform the requested operation.
HTTP Status Code: 401

 ** ValidationException **
The input failed to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_qapps_ImportDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/ImportDocument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/ImportDocument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/ImportDocument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/ImportDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/ImportDocument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/ImportDocument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/ImportDocument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/ImportDocument)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/ImportDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/ImportDocument)
