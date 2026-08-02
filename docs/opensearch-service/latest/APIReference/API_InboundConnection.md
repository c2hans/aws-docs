---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_InboundConnection.html
---

# InboundConnection
<a name="API_InboundConnection"></a>

Describes an inbound cross-cluster connection for Amazon OpenSearch Service. For more information, see [Cross-cluster search for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html).

## Contents
<a name="API_InboundConnection_Contents"></a>

 ** ConnectionId **   <a name="opensearchservice-Type-InboundConnection-ConnectionId"></a>
The unique identifier of the connection.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 256.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** ConnectionMode **   <a name="opensearchservice-Type-InboundConnection-ConnectionMode"></a>
The connection mode.
Type: String
Valid Values: `DIRECT | VPC_ENDPOINT`
Required: No

 ** ConnectionStatus **   <a name="opensearchservice-Type-InboundConnection-ConnectionStatus"></a>
The current status of the connection.
Type: [InboundConnectionStatus](API_InboundConnectionStatus.md) object
Required: No

 ** LocalDomainInfo **   <a name="opensearchservice-Type-InboundConnection-LocalDomainInfo"></a>
Information about the source (local) domain.
Type: [DomainInformationContainer](API_DomainInformationContainer.md) object
Required: No

 ** RemoteDomainInfo **   <a name="opensearchservice-Type-InboundConnection-RemoteDomainInfo"></a>
Information about the destination (remote) domain.
Type: [DomainInformationContainer](API_DomainInformationContainer.md) object
Required: No

## See Also
<a name="API_InboundConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/InboundConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/InboundConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/InboundConnection)
