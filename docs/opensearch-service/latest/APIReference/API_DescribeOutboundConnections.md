---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeOutboundConnections.html
---

# DescribeOutboundConnections
<a name="API_DescribeOutboundConnections"></a>

Lists all the outbound cross-cluster connections for a local (source) Amazon OpenSearch Service domain. For more information, see [Cross-cluster search for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html).

## Request Syntax
<a name="API_DescribeOutboundConnections_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/cc/outboundConnection/search HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeOutboundConnections_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeOutboundConnections_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeOutboundConnections_RequestSyntax) **   <a name="opensearchservice-DescribeOutboundConnections-request-Filters"></a>
List of filter names and values that you can use for requests.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_DescribeOutboundConnections_RequestSyntax) **   <a name="opensearchservice-DescribeOutboundConnections-request-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeOutboundConnections_RequestSyntax) **   <a name="opensearchservice-DescribeOutboundConnections-request-NextToken"></a>
If your initial `DescribeOutboundConnections` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `DescribeOutboundConnections` operations, which returns results in the next page.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeOutboundConnections_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Connections": [
      {
         "ConnectionAlias": "string",
         "ConnectionId": "string",
         "ConnectionMode": "string",
         "ConnectionProperties": {
            "CrossClusterSearch": {
               "SkipUnavailable": "string"
            },
            "Endpoint": "string"
         },
         "ConnectionStatus": {
            "Message": "string",
            "StatusCode": "string"
         },
         "LocalDomainInfo": {
            "AWSDomainInformation": {
               "DomainName": "string",
               "OwnerId": "string",
               "Region": "string"
            }
         },
         "RemoteDomainInfo": {
            "AWSDomainInformation": {
               "DomainName": "string",
               "OwnerId": "string",
               "Region": "string"
            }
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeOutboundConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connections](#API_DescribeOutboundConnections_ResponseSyntax) **   <a name="opensearchservice-DescribeOutboundConnections-response-Connections"></a>
List of outbound connections that match the filter criteria.
Type: Array of [OutboundConnection](API_OutboundConnection.md) objects

 ** [NextToken](#API_DescribeOutboundConnections_ResponseSyntax) **   <a name="opensearchservice-DescribeOutboundConnections-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_DescribeOutboundConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InvalidPaginationTokenException **
Request processing failed because you provided an invalid pagination token.
HTTP Status Code: 400

## See Also
<a name="API_DescribeOutboundConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeOutboundConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeOutboundConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeOutboundConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeOutboundConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeOutboundConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeOutboundConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeOutboundConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeOutboundConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeOutboundConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeOutboundConnections)
