---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CancelJob.html
---

# CancelJob
<a name="API_CancelJob"></a>

This operation cancels a job. Jobs can be cancelled only when they are in the WAITING state.

## Request Syntax
<a name="API_CancelJob_RequestSyntax"></a>

```
DELETE /v1/jobs/{{JobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [JobId](#API_CancelJob_RequestSyntax) **   <a name="dataexchange-CancelJob-request-uri-JobId"></a>
The unique identifier for a job.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## Request Body
<a name="API_CancelJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelJob_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_CancelJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_CancelJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** Message **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** ResourceId **
The unique identifier for the resource with the conflict.
 ** ResourceType **
The type of the resource with the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
 ** Message **
The resource couldn't be found.
 ** ResourceId **
The unique identifier for the resource that couldn't be found.
 ** ResourceType **
The type of resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** Message **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request was invalid.
 ** ExceptionCause **
The unique identifier for the resource that couldn't be found.
 ** Message **
The message that informs you about what was invalid about the request.
HTTP Status Code: 400

## See Also
<a name="API_CancelJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/CancelJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/CancelJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/CancelJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/CancelJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/CancelJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/CancelJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/CancelJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/CancelJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/CancelJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/CancelJob)
