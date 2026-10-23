---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_DeleteCollector.html
---

# DeleteCollector
<a name="API_DeleteCollector"></a>

Deletes the Collector for the caller's account. The Collector first enters PENDING\_DELETION, then the service removes its schedule, AWS Config service-linked recorder, versioned S3 bucket, KMS key, and persisted record.

## Request Syntax
<a name="API_DeleteCollector_RequestSyntax"></a>

```
DELETE /collectors/{{collectorId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCollector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collectorId](#API_DeleteCollector_RequestSyntax) **   <a name="continuum-DeleteCollector-request-uri-collectorId"></a>
The identifier of the collector.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_DeleteCollector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCollector_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteCollector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteCollector_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteCollector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/DeleteCollector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/DeleteCollector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/DeleteCollector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/DeleteCollector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/DeleteCollector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/DeleteCollector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/DeleteCollector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/DeleteCollector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/DeleteCollector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/DeleteCollector)
