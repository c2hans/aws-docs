---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateCodeScan.html
---

# CreateCodeScan
<a name="API_CreateCodeScan"></a>

Creates an explicit scan request for one environment. CP creates durable work before any queue delivery occurs.

Retrying a request that succeeded, with the same clientToken on the same environment, returns the original scan instead of starting another one. Token handling is not yet atomic: requests with the same token that run at the same time, or a retry after a request that failed partway through, can leave an additional scan, which may end in the FAILED state with a message that it was superseded. Deleting the environment makes its tokens unusable; a later request with one of them returns ResourceNotFoundException.

Each environment can have a limited number of scans in progress at the same time. Once that limit is enforced, a request that would exceed it returns ServiceQuotaExceededException; wait for a scan to finish (ListCodeScans shows each scan's status), then retry.

## Request Syntax
<a name="API_CreateCodeScan_RequestSyntax"></a>

```
POST /environments/{{environmentId}}/code-scans HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCodeScan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_CreateCodeScan_RequestSyntax) **   <a name="continuum-CreateCodeScan-request-uri-environmentId"></a>
The identifier of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_CreateCodeScan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateCodeScan_RequestSyntax) **   <a name="continuum-CreateCodeScan-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[!-~]{1,128}`
Required: No

## Response Syntax
<a name="API_CreateCodeScan_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "scan": {
      "completedAt": "string",
      "createdAt": "string",
      "failureMessage": "string",
      "failureStage": "string",
      "origin": "string",
      "scanRunId": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_CreateCodeScan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [scan](#API_CreateCodeScan_ResponseSyntax) **   <a name="continuum-CreateCodeScan-response-scan"></a>
The scan.
Type: [CodeScanSummary](API_CodeScanSummary.md) object

## Errors
<a name="API_CreateCodeScan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed a service quota. Review your quota and request an increase if needed.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateCodeScan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/CreateCodeScan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/CreateCodeScan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/CreateCodeScan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/CreateCodeScan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/CreateCodeScan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/CreateCodeScan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/CreateCodeScan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/CreateCodeScan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/CreateCodeScan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/CreateCodeScan)
