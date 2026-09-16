---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListDataSets.html
---

# ListDataSets
<a name="API_ListDataSets"></a>

This operation lists your data sets. When listing by origin OWNED, results are sorted by CreatedAt in descending order. When listing by origin ENTITLED, there is no order.

## Request Syntax
<a name="API_ListDataSets_RequestSyntax"></a>

```
GET /v1/data-sets?maxResults={{MaxResults}}&nextToken={{NextToken}}&origin={{Origin}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListDataSets_RequestSyntax) **   <a name="dataexchange-ListDataSets-request-uri-MaxResults"></a>
The maximum number of results returned by a single call.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [NextToken](#API_ListDataSets_RequestSyntax) **   <a name="dataexchange-ListDataSets-request-uri-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.

 ** [Origin](#API_ListDataSets_RequestSyntax) **   <a name="dataexchange-ListDataSets-request-uri-Origin"></a>
A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).

## Request Body
<a name="API_ListDataSets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataSets": [
      {
         "Arn": "string",
         "AssetType": "string",
         "CreatedAt": "string",
         "Description": "string",
         "Id": "string",
         "Name": "string",
         "Origin": "string",
         "OriginDetails": {
            "DataGrantId": "string",
            "ProductId": "string"
         },
         "SourceId": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDataSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSets](#API_ListDataSets_ResponseSyntax) **   <a name="dataexchange-ListDataSets-response-DataSets"></a>
The data set objects listed by the request.
Type: Array of [DataSetEntry](API_DataSetEntry.md) objects

 ** [NextToken](#API_ListDataSets_ResponseSyntax) **   <a name="dataexchange-ListDataSets-response-NextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Type: String

## Errors
<a name="API_ListDataSets_Errors"></a>

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
<a name="API_ListDataSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/ListDataSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/ListDataSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ListDataSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/ListDataSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ListDataSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/ListDataSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/ListDataSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/ListDataSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/ListDataSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ListDataSets)
