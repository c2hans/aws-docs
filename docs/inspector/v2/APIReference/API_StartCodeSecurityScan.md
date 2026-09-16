---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartCodeSecurityScan.html
---

# StartCodeSecurityScan
<a name="API_StartCodeSecurityScan"></a>

Initiates a code security scan on a specified repository.

## Request Syntax
<a name="API_StartCodeSecurityScan_RequestSyntax"></a>

```
POST /codesecurity/scan/start HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "resource": { ... }
}
```

## URI Request Parameters
<a name="API_StartCodeSecurityScan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartCodeSecurityScan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartCodeSecurityScan_RequestSyntax) **   <a name="inspector2-StartCodeSecurityScan-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** [resource](#API_StartCodeSecurityScan_RequestSyntax) **   <a name="inspector2-StartCodeSecurityScan-request-resource"></a>
The resource identifier for the code repository to scan.
Type: [CodeSecurityResource](API_CodeSecurityResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_StartCodeSecurityScan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "scanId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StartCodeSecurityScan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scanId](#API_StartCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-StartCodeSecurityScan-response-scanId"></a>
The unique identifier of the initiated scan.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [status](#API_StartCodeSecurityScan_ResponseSyntax) **   <a name="inspector2-StartCodeSecurityScan-response-status"></a>
The current status of the initiated scan.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | SKIPPED`

## Errors
<a name="API_StartCodeSecurityScan_Errors"></a>

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
<a name="API_StartCodeSecurityScan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/StartCodeSecurityScan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/StartCodeSecurityScan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/StartCodeSecurityScan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/StartCodeSecurityScan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/StartCodeSecurityScan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/StartCodeSecurityScan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/StartCodeSecurityScan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/StartCodeSecurityScan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/StartCodeSecurityScan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/StartCodeSecurityScan)
