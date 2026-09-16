---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListEventActions.html
---

# ListEventActions
<a name="API_ListEventActions"></a>

This operation lists your event actions.

## Request Syntax
<a name="API_ListEventActions_RequestSyntax"></a>

```
GET /v1/event-actions?eventSourceId={{EventSourceId}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEventActions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EventSourceId](#API_ListEventActions_RequestSyntax) **   <a name="dataexchange-ListEventActions-request-uri-EventSourceId"></a>
The unique identifier for the event source.

 ** [MaxResults](#API_ListEventActions_RequestSyntax) **   <a name="dataexchange-ListEventActions-request-uri-MaxResults"></a>
The maximum number of results returned by a single call.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [NextToken](#API_ListEventActions_RequestSyntax) **   <a name="dataexchange-ListEventActions-request-uri-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.

## Request Body
<a name="API_ListEventActions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEventActions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EventActions": [
      {
         "Action": {
            "ExportRevisionToS3": {
               "Encryption": {
                  "KmsKeyArn": "string",
                  "Type": "string"
               },
               "RevisionDestination": {
                  "Bucket": "string",
                  "KeyPattern": "string"
               }
            }
         },
         "Arn": "string",
         "CreatedAt": "string",
         "Event": {
            "RevisionPublished": {
               "DataSetId": "string"
            }
         },
         "Id": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEventActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventActions](#API_ListEventActions_ResponseSyntax) **   <a name="dataexchange-ListEventActions-response-EventActions"></a>
The event action objects listed by the request.
Type: Array of [EventActionEntry](API_EventActionEntry.md) objects

 ** [NextToken](#API_ListEventActions_ResponseSyntax) **   <a name="dataexchange-ListEventActions-response-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Type: String

## Errors
<a name="API_ListEventActions_Errors"></a>

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
<a name="API_ListEventActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/ListEventActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/ListEventActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ListEventActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/ListEventActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ListEventActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/ListEventActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/ListEventActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/ListEventActions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/ListEventActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ListEventActions)
