---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateOutboundConnection.html
---

# CreateOutboundConnection
<a name="API_CreateOutboundConnection"></a>

Creates a new cross-cluster search connection from a source Amazon OpenSearch Service domain to a destination domain. For more information, see [Cross-cluster search for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html).

## Request Syntax
<a name="API_CreateOutboundConnection_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/cc/outboundConnection HTTP/1.1
Content-type: application/json

{
   "ConnectionAlias": "{{string}}",
   "ConnectionMode": "{{string}}",
   "ConnectionProperties": {
      "CrossClusterSearch": {
         "SkipUnavailable": "{{string}}"
      },
      "Endpoint": "{{string}}"
   },
   "LocalDomainInfo": {
      "AWSDomainInformation": {
         "DomainName": "{{string}}",
         "OwnerId": "{{string}}",
         "Region": "{{string}}"
      }
   },
   "RemoteDomainInfo": {
      "AWSDomainInformation": {
         "DomainName": "{{string}}",
         "OwnerId": "{{string}}",
         "Region": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateOutboundConnection_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateOutboundConnection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConnectionAlias](#API_CreateOutboundConnection_RequestSyntax) **   <a name="opensearchservice-CreateOutboundConnection-request-ConnectionAlias"></a>
Name of the connection.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[a-zA-Z][a-zA-Z0-9\-\_]+`
Required: Yes

 ** [ConnectionMode](#API_CreateOutboundConnection_RequestSyntax) **   <a name="opensearchservice-CreateOutboundConnection-request-ConnectionMode"></a>
The connection mode.
Type: String
Valid Values: `DIRECT | VPC_ENDPOINT`
Required: No

 ** [ConnectionProperties](#API_CreateOutboundConnection_RequestSyntax) **   <a name="opensearchservice-CreateOutboundConnection-request-ConnectionProperties"></a>
The `ConnectionProperties` for the outbound connection.
Type: [ConnectionProperties](API_ConnectionProperties.md) object
Required: No

 ** [LocalDomainInfo](#API_CreateOutboundConnection_RequestSyntax) **   <a name="opensearchservice-CreateOutboundConnection-request-LocalDomainInfo"></a>
Name and Region of the source (local) domain.
Type: [DomainInformationContainer](API_DomainInformationContainer.md) object
Required: Yes

 ** [RemoteDomainInfo](#API_CreateOutboundConnection_RequestSyntax) **   <a name="opensearchservice-CreateOutboundConnection-request-RemoteDomainInfo"></a>
Name and Region of the destination (remote) domain.
Type: [DomainInformationContainer](API_DomainInformationContainer.md) object
Required: Yes

## Response Syntax
<a name="API_CreateOutboundConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_CreateOutboundConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionAlias](#API_CreateOutboundConnection_ResponseSyntax) **   <a name="opensearchservice-CreateOutboundConnection-response-ConnectionAlias"></a>
Name of the connection.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[a-zA-Z][a-zA-Z0-9\-\_]+`

 ** [ConnectionId](#API_CreateOutboundConnection_ResponseSyntax) **   <a name="opensearchservice-CreateOutboundConnection-response-ConnectionId"></a>
The unique identifier for the created outbound connection, which is used for subsequent operations on the connection.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 256.
Pattern: `[a-z][a-z0-9\-]+`

 ** [ConnectionMode](#API_CreateOutboundConnection_ResponseSyntax) **   <a name="opensearchservice-CreateOutboundConnection-response-ConnectionMode"></a>
The connection mode.
Type: String
Valid Values: `DIRECT | VPC_ENDPOINT`

 ** [ConnectionProperties](#API_CreateOutboundConnection_ResponseSyntax) **   <a name="opensearchservice-CreateOutboundConnection-response-ConnectionProperties"></a>
The `ConnectionProperties` for the newly created connection.
Type: [ConnectionProperties](API_ConnectionProperties.md) object

 ** [ConnectionStatus](#API_CreateOutboundConnection_ResponseSyntax) **   <a name="opensearchservice-CreateOutboundConnection-response-ConnectionStatus"></a>
The status of the connection.
Type: [OutboundConnectionStatus](API_OutboundConnectionStatus.md) object

 ** [LocalDomainInfo](#API_CreateOutboundConnection_ResponseSyntax) **   <a name="opensearchservice-CreateOutboundConnection-response-LocalDomainInfo"></a>
Information about the source (local) domain.
Type: [DomainInformationContainer](API_DomainInformationContainer.md) object

 ** [RemoteDomainInfo](#API_CreateOutboundConnection_ResponseSyntax) **   <a name="opensearchservice-CreateOutboundConnection-response-RemoteDomainInfo"></a>
Information about the destination (remote) domain.
Type: [DomainInformationContainer](API_DomainInformationContainer.md) object

## Errors
<a name="API_CreateOutboundConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceAlreadyExistsException **
An exception for creating a resource that already exists.
HTTP Status Code: 409

## See Also
<a name="API_CreateOutboundConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/CreateOutboundConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/CreateOutboundConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CreateOutboundConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/CreateOutboundConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CreateOutboundConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/CreateOutboundConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/CreateOutboundConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/CreateOutboundConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/CreateOutboundConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CreateOutboundConnection)
