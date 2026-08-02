---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AcceptInboundConnection.html
---

# AcceptInboundConnection
<a name="API_AcceptInboundConnection"></a>

Allows the destination Amazon OpenSearch Service domain owner to accept an inbound cross-cluster search connection request. For more information, see [Cross-cluster search for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html).

## Request Syntax
<a name="API_AcceptInboundConnection_RequestSyntax"></a>

```
PUT /2021-01-01/opensearch/cc/inboundConnection/{{ConnectionId}}/accept HTTP/1.1
```

## URI Request Parameters
<a name="API_AcceptInboundConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionId](#API_AcceptInboundConnection_RequestSyntax) **   <a name="opensearchservice-AcceptInboundConnection-request-uri-ConnectionId"></a>
The ID of the inbound connection to accept.
Length Constraints: Minimum length of 10. Maximum length of 256.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_AcceptInboundConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_AcceptInboundConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Connection": {
      "ConnectionId": "string",
      "ConnectionMode": "string",
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
}
```

## Response Elements
<a name="API_AcceptInboundConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_AcceptInboundConnection_ResponseSyntax) **   <a name="opensearchservice-AcceptInboundConnection-response-Connection"></a>
Information about the accepted inbound connection.
Type: [InboundConnection](API_InboundConnection.md) object

## Errors
<a name="API_AcceptInboundConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

## See Also
<a name="API_AcceptInboundConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/AcceptInboundConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/AcceptInboundConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AcceptInboundConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/AcceptInboundConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AcceptInboundConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/AcceptInboundConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/AcceptInboundConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/AcceptInboundConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/AcceptInboundConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AcceptInboundConnection)
