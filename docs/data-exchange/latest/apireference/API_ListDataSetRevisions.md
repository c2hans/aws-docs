---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListDataSetRevisions.html
---

# ListDataSetRevisions
<a name="API_ListDataSetRevisions"></a>

This operation lists a data set's revisions sorted by CreatedAt in descending order.

## Request Syntax
<a name="API_ListDataSetRevisions_RequestSyntax"></a>

```
GET /v1/data-sets/{{DataSetId}}/revisions?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSetRevisions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSetId](#API_ListDataSetRevisions_RequestSyntax) **   <a name="dataexchange-ListDataSetRevisions-request-uri-DataSetId"></a>
The unique identifier for a data set.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** [MaxResults](#API_ListDataSetRevisions_RequestSyntax) **   <a name="dataexchange-ListDataSetRevisions-request-uri-MaxResults"></a>
The maximum number of results returned by a single call.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [NextToken](#API_ListDataSetRevisions_RequestSyntax) **   <a name="dataexchange-ListDataSetRevisions-request-uri-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.

## Request Body
<a name="API_ListDataSetRevisions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSetRevisions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Revisions": [
      {
         "Arn": "string",
         "Comment": "string",
         "CreatedAt": "string",
         "DataSetId": "string",
         "Finalized": boolean,
         "Id": "string",
         "RevocationComment": "string",
         "Revoked": boolean,
         "RevokedAt": "string",
         "SourceId": "string",
         "UpdatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListDataSetRevisions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListDataSetRevisions_ResponseSyntax) **   <a name="dataexchange-ListDataSetRevisions-response-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Type: String

 ** [Revisions](#API_ListDataSetRevisions_ResponseSyntax) **   <a name="dataexchange-ListDataSetRevisions-response-Revisions"></a>
The asset objects listed by the request.
Type: Array of [RevisionEntry](API_RevisionEntry.md) objects

## Errors
<a name="API_ListDataSetRevisions_Errors"></a>

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
<a name="API_ListDataSetRevisions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/ListDataSetRevisions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/ListDataSetRevisions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ListDataSetRevisions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/ListDataSetRevisions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ListDataSetRevisions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/ListDataSetRevisions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/ListDataSetRevisions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/ListDataSetRevisions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/ListDataSetRevisions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ListDataSetRevisions)
