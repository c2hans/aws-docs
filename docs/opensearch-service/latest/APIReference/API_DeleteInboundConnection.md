---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteInboundConnection.html
---

# DeleteInboundConnection
<a name="API_DeleteInboundConnection"></a>

Allows the destination Amazon OpenSearch Service domain owner to delete an existing inbound cross-cluster search connection. For more information, see [Cross-cluster search for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html).

## Request Syntax
<a name="API_DeleteInboundConnection_RequestSyntax"></a>

```
DELETE /2021-01-01/opensearch/cc/inboundConnection/{{ConnectionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteInboundConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionId](#API_DeleteInboundConnection_RequestSyntax) **   <a name="opensearchservice-DeleteInboundConnection-request-uri-ConnectionId"></a>
The ID of the inbound connection to permanently delete.
Length Constraints: Minimum length of 10. Maximum length of 256.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_DeleteInboundConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteInboundConnection_ResponseSyntax"></a>

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
<a name="API_DeleteInboundConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_DeleteInboundConnection_ResponseSyntax) **   <a name="opensearchservice-DeleteInboundConnection-response-Connection"></a>
The deleted inbound connection.
Type: [InboundConnection](API_InboundConnection.md) object

## Errors
<a name="API_DeleteInboundConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

## See Also
<a name="API_DeleteInboundConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DeleteInboundConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DeleteInboundConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DeleteInboundConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DeleteInboundConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DeleteInboundConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DeleteInboundConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DeleteInboundConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DeleteInboundConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DeleteInboundConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DeleteInboundConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
