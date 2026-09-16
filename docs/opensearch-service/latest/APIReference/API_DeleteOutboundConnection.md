---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteOutboundConnection.html
---

# DeleteOutboundConnection
<a name="API_DeleteOutboundConnection"></a>

Allows the source Amazon OpenSearch Service domain owner to delete an existing outbound cross-cluster search connection. For more information, see [Cross-cluster search for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html).

## Request Syntax
<a name="API_DeleteOutboundConnection_RequestSyntax"></a>

```
DELETE /2021-01-01/opensearch/cc/outboundConnection/{{ConnectionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteOutboundConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionId](#API_DeleteOutboundConnection_RequestSyntax) **   <a name="opensearchservice-DeleteOutboundConnection-request-uri-ConnectionId"></a>
The ID of the outbound connection you want to permanently delete.
Length Constraints: Minimum length of 10. Maximum length of 256.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_DeleteOutboundConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteOutboundConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Connection": {
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
}
```

## Response Elements
<a name="API_DeleteOutboundConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_DeleteOutboundConnection_ResponseSyntax) **   <a name="opensearchservice-DeleteOutboundConnection-response-Connection"></a>
The deleted inbound connection.
Type: [OutboundConnection](API_OutboundConnection.md) object

## Errors
<a name="API_DeleteOutboundConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

## See Also
<a name="API_DeleteOutboundConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DeleteOutboundConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DeleteOutboundConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DeleteOutboundConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DeleteOutboundConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DeleteOutboundConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DeleteOutboundConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DeleteOutboundConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DeleteOutboundConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DeleteOutboundConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DeleteOutboundConnection)
