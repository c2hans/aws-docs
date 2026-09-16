---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQAppSessionMetadata.html
---

# UpdateQAppSessionMetadata
<a name="API_qapps_UpdateQAppSessionMetadata"></a>

Updates the configuration metadata of a session for a given Q App `sessionId`.

## Request Syntax
<a name="API_qapps_UpdateQAppSessionMetadata_RequestSyntax"></a>

```
POST /runtime.updateQAppSessionMetadata HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "sessionId": "{{string}}",
   "sessionName": "{{string}}",
   "sharingConfiguration": {
      "acceptResponses": {{boolean}},
      "enabled": {{boolean}},
      "revealCards": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_qapps_UpdateQAppSessionMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_UpdateQAppSessionMetadata_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQAppSessionMetadata-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_UpdateQAppSessionMetadata_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sessionId](#API_qapps_UpdateQAppSessionMetadata_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQAppSessionMetadata-request-sessionId"></a>
The unique identifier of the Q App session to update configuration for.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [sessionName](#API_qapps_UpdateQAppSessionMetadata_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQAppSessionMetadata-request-sessionName"></a>
The new name for the Q App session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** [sharingConfiguration](#API_qapps_UpdateQAppSessionMetadata_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQAppSessionMetadata-request-sharingConfiguration"></a>
The new sharing configuration for the Q App data collection session.
Type: [SessionSharingConfiguration](API_qapps_SessionSharingConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_qapps_UpdateQAppSessionMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "sessionArn": "string",
   "sessionId": "string",
   "sessionName": "string",
   "sharingConfiguration": {
      "acceptResponses": boolean,
      "enabled": boolean,
      "revealCards": boolean
   }
}
```

## Response Elements
<a name="API_qapps_UpdateQAppSessionMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sessionArn](#API_qapps_UpdateQAppSessionMetadata_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQAppSessionMetadata-response-sessionArn"></a>
The Amazon Resource Name (ARN) of the updated Q App session.
Type: String

 ** [sessionId](#API_qapps_UpdateQAppSessionMetadata_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQAppSessionMetadata-response-sessionId"></a>
The unique identifier of the updated Q App session.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`

 ** [sessionName](#API_qapps_UpdateQAppSessionMetadata_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQAppSessionMetadata-response-sessionName"></a>
The new name of the updated Q App session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [sharingConfiguration](#API_qapps_UpdateQAppSessionMetadata_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQAppSessionMetadata-response-sharingConfiguration"></a>
The new sharing configuration of the updated Q App data collection session.
Type: [SessionSharingConfiguration](API_qapps_SessionSharingConfiguration.md) object

## Errors
<a name="API_qapps_UpdateQAppSessionMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

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
<a name="API_qapps_UpdateQAppSessionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/UpdateQAppSessionMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/UpdateQAppSessionMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/UpdateQAppSessionMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/UpdateQAppSessionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/UpdateQAppSessionMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/UpdateQAppSessionMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/UpdateQAppSessionMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/UpdateQAppSessionMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/UpdateQAppSessionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/UpdateQAppSessionMetadata)
