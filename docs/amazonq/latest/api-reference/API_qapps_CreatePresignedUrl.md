---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CreatePresignedUrl.html
---

# CreatePresignedUrl
<a name="API_qapps_CreatePresignedUrl"></a>

Creates a presigned URL for an S3 POST operation to upload a file. You can use this URL to set a default file for a `FileUploadCard` in a Q App definition or to provide a file for a single Q App run. The `scope` parameter determines how the file will be used, either at the app definition level or the app session level.

**Note**
The IAM permissions are derived from the `qapps:ImportDocument` action. For more information on the IAM policy for Amazon Q Apps, see [IAM permissions for using Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/deploy-q-apps-iam-permissions.html).

## Request Syntax
<a name="API_qapps_CreatePresignedUrl_RequestSyntax"></a>

```
POST /apps.createPresignedUrl HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "appId": "{{string}}",
   "cardId": "{{string}}",
   "fileContentsSha256": "{{string}}",
   "fileName": "{{string}}",
   "scope": "{{string}}",
   "sessionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_qapps_CreatePresignedUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_CreatePresignedUrl_RequestSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_CreatePresignedUrl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appId](#API_qapps_CreatePresignedUrl_RequestSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-request-appId"></a>
The unique identifier of the Q App the file is associated with.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [cardId](#API_qapps_CreatePresignedUrl_RequestSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-request-cardId"></a>
The unique identifier of the card the file is associated with.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [fileContentsSha256](#API_qapps_CreatePresignedUrl_RequestSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-request-fileContentsSha256"></a>
The Base64-encoded SHA-256 digest of the contents of the file to be uploaded.
Type: String
Pattern: `[A-Za-z0-9+/]{43}=$|^[A-Za-z0-9+/]{42}==$|^[A-Za-z0-9+/]{44}`
Required: Yes

 ** [fileName](#API_qapps_CreatePresignedUrl_RequestSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-request-fileName"></a>
The name of the file to be uploaded.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: Yes

 ** [scope](#API_qapps_CreatePresignedUrl_RequestSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-request-scope"></a>
Whether the file is associated with a Q App definition or a specific Q App session.
Type: String
Valid Values: `APPLICATION | SESSION`
Required: Yes

 ** [sessionId](#API_qapps_CreatePresignedUrl_RequestSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-request-sessionId"></a>
The unique identifier of the Q App session the file is associated with, if applicable.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: No

## Response Syntax
<a name="API_qapps_CreatePresignedUrl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fileId": "string",
   "presignedUrl": "string",
   "presignedUrlExpiration": "string",
   "presignedUrlFields": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_qapps_CreatePresignedUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fileId](#API_qapps_CreatePresignedUrl_ResponseSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-response-fileId"></a>
The unique identifier assigned to the file to be uploaded.
Type: String

 ** [presignedUrl](#API_qapps_CreatePresignedUrl_ResponseSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-response-presignedUrl"></a>
The URL for a presigned S3 POST operation used to upload a file.
Type: String

 ** [presignedUrlExpiration](#API_qapps_CreatePresignedUrl_ResponseSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-response-presignedUrlExpiration"></a>
The date and time that the presigned URL will expire in ISO 8601 format.
Type: Timestamp

 ** [presignedUrlFields](#API_qapps_CreatePresignedUrl_ResponseSyntax) **   <a name="qbusiness-qapps_CreatePresignedUrl-response-presignedUrlFields"></a>
The form fields to include in the presigned S3 POST operation used to upload a file.
Type: String to string map

## Errors
<a name="API_qapps_CreatePresignedUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
HTTP Status Code: 500

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
<a name="API_qapps_CreatePresignedUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/CreatePresignedUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/CreatePresignedUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/CreatePresignedUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/CreatePresignedUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/CreatePresignedUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/CreatePresignedUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/CreatePresignedUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/CreatePresignedUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/CreatePresignedUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/CreatePresignedUrl)
