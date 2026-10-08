---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CancelExportJobV2.html
---

# CancelExportJobV2
<a name="API_CancelExportJobV2"></a>

Cancels a findings export job that is in progress. Security Hub transitions a running job to the `CANCELLED` state and returns the `ExportJobId` and its new `Status`. Canceling a job that is already in the `CANCELLED` state succeeds and returns the same result, so you can safely retry a cancel request.

You can't cancel an export job that has already reached a terminal `SUCCEEDED` or `FAILED` state; in that case, this operation returns a `ConflictException`. If no export job matches the `ExportJobId` that you provide, this operation returns a `ResourceNotFoundException`.

The `Status` value returned by this operation reflects the cancellation immediately, even though the job can take a short time to stop completely.

## Request Syntax
<a name="API_CancelExportJobV2_RequestSyntax"></a>

```
POST /exportjobsv2/{{ExportJobId}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelExportJobV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExportJobId](#API_CancelExportJobV2_RequestSyntax) **   <a name="securityhub-CancelExportJobV2-request-uri-ExportJobId"></a>
The unique identifier of the export job to cancel. This is the value returned by `StartExportJobV2`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9]+$`
Required: Yes

## Request Body
<a name="API_CancelExportJobV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelExportJobV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ExportJobId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_CancelExportJobV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportJobId](#API_CancelExportJobV2_ResponseSyntax) **   <a name="securityhub-CancelExportJobV2-response-ExportJobId"></a>
The unique identifier of the export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9]+$`

 ** [Status](#API_CancelExportJobV2_ResponseSyntax) **   <a name="securityhub-CancelExportJobV2-response-Status"></a>
The state of the export job after the cancel request.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | CANCELLED`

## Errors
<a name="API_CancelExportJobV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_CancelExportJobV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/CancelExportJobV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/CancelExportJobV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CancelExportJobV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/CancelExportJobV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CancelExportJobV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/CancelExportJobV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/CancelExportJobV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/CancelExportJobV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/CancelExportJobV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CancelExportJobV2)
