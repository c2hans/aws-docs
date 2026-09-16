---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCodeSecurityScan.html
---

# GetCodeSecurityScan
<a name="API_GetCodeSecurityScan"></a>

Retrieves information about a specific code security scan.

## Request Syntax
<a name="API_GetCodeSecurityScan_RequestSyntax"></a>

```
POST /codesecurity/scan/get HTTP/1.1
Content-type: application/json

{
   "resource": { ... },
   "scanId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetCodeSecurityScan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetCodeSecurityScan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resource](#API_GetCodeSecurityScan_RequestSyntax) **   <a name="inspector2-GetCodeSecurityScan-request-resource"></a>
The resource identifier for the code repository that was scanned.
Type: [CodeSecurityResource](API_CodeSecurityResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [scanId](#API_GetCodeSecurityScan_RequestSyntax) **   <a name="inspector2-GetCodeSecurityScan-request-scanId"></a>
The unique identifier of the scan to retrieve.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_GetCodeSecurityScan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountId": "string",
   "createdAt": number,
   "lastCommitId": "string",
   "resource": { ... },
   "scanId": "string",
   "status": "string",
   "statusReason": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetCodeSecurityScan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountId](#API_GetCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityScan-response-accountId"></a>
The AWS account ID associated with the scan.
Type: String

 ** [createdAt](#API_GetCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityScan-response-createdAt"></a>
The timestamp when the scan was created.
Type: Timestamp

 ** [lastCommitId](#API_GetCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityScan-response-lastCommitId"></a>
The identifier of the last commit that was scanned. This is only returned if the scan was successful or skipped.
Type: String

 ** [resource](#API_GetCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityScan-response-resource"></a>
The resource identifier for the code repository that was scanned.
Type: [CodeSecurityResource](API_CodeSecurityResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [scanId](#API_GetCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityScan-response-scanId"></a>
The unique identifier of the scan.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [status](#API_GetCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityScan-response-status"></a>
The current status of the scan.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | SKIPPED`

 ** [statusReason](#API_GetCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityScan-response-statusReason"></a>
The reason for the current status of the scan.
Type: String

 ** [updatedAt](#API_GetCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityScan-response-updatedAt"></a>
The timestamp when the scan was last updated.
Type: Timestamp

## Errors
<a name="API_GetCodeSecurityScan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred. This exception occurs when the same resource is being modified by concurrent requests.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetCodeSecurityScan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetCodeSecurityScan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetCodeSecurityScan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetCodeSecurityScan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetCodeSecurityScan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetCodeSecurityScan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetCodeSecurityScan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetCodeSecurityScan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetCodeSecurityScan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetCodeSecurityScan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetCodeSecurityScan)
