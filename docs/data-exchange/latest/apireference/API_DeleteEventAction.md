---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_DeleteEventAction.html
---

# DeleteEventAction
<a name="API_DeleteEventAction"></a>

This operation deletes the event action.

## Request Syntax
<a name="API_DeleteEventAction_RequestSyntax"></a>

```
DELETE /v1/event-actions/{{EventActionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteEventAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EventActionId](#API_DeleteEventAction_RequestSyntax) **   <a name="dataexchange-DeleteEventAction-request-uri-EventActionId"></a>
The unique identifier for the event action.
Required: Yes

## Request Body
<a name="API_DeleteEventAction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteEventAction_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteEventAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteEventAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DeleteEventAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/DeleteEventAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/DeleteEventAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/DeleteEventAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/DeleteEventAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/DeleteEventAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/DeleteEventAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/DeleteEventAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/DeleteEventAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/DeleteEventAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/DeleteEventAction)
