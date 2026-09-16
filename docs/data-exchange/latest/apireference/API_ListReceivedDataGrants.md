---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ListReceivedDataGrants.html
---

# ListReceivedDataGrants
<a name="API_ListReceivedDataGrants"></a>

This operation returns information about all received data grants.

## Request Syntax
<a name="API_ListReceivedDataGrants_RequestSyntax"></a>

```
GET /v1/received-data-grants?acceptanceState={{AcceptanceState}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListReceivedDataGrants_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AcceptanceState](#API_ListReceivedDataGrants_RequestSyntax) **   <a name="dataexchange-ListReceivedDataGrants-request-uri-AcceptanceState"></a>
The acceptance state of the data grants to list.
Valid Values: `PENDING_RECEIVER_ACCEPTANCE | ACCEPTED`

 ** [MaxResults](#API_ListReceivedDataGrants_RequestSyntax) **   <a name="dataexchange-ListReceivedDataGrants-request-uri-MaxResults"></a>
The maximum number of results to be included in the next page.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [NextToken](#API_ListReceivedDataGrants_RequestSyntax) **   <a name="dataexchange-ListReceivedDataGrants-request-uri-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.

## Request Body
<a name="API_ListReceivedDataGrants_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListReceivedDataGrants_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataGrantSummaries": [
      {
         "AcceptanceState": "string",
         "AcceptedAt": "string",
         "Arn": "string",
         "CreatedAt": "string",
         "DataSetId": "string",
         "EndsAt": "string",
         "Id": "string",
         "Name": "string",
         "ReceiverPrincipal": "string",
         "SenderPrincipal": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListReceivedDataGrants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataGrantSummaries](#API_ListReceivedDataGrants_ResponseSyntax) **   <a name="dataexchange-ListReceivedDataGrants-response-DataGrantSummaries"></a>
An object that contains a list of received data grant information.
Type: Array of [ReceivedDataGrantSummariesEntry](API_ReceivedDataGrantSummariesEntry.md) objects

 ** [NextToken](#API_ListReceivedDataGrants_ResponseSyntax) **   <a name="dataexchange-ListReceivedDataGrants-response-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String

## Errors
<a name="API_ListReceivedDataGrants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

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
<a name="API_ListReceivedDataGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/ListReceivedDataGrants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/ListReceivedDataGrants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ListReceivedDataGrants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/ListReceivedDataGrants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ListReceivedDataGrants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/ListReceivedDataGrants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/ListReceivedDataGrants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/ListReceivedDataGrants)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/ListReceivedDataGrants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ListReceivedDataGrants)
