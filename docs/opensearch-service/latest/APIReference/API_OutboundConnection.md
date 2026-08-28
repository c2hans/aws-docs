---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OutboundConnection.html
---

# OutboundConnection
<a name="API_OutboundConnection"></a>

Specifies details about an outbound cross-cluster connection.

## Contents
<a name="API_OutboundConnection_Contents"></a>

 ** ConnectionAlias **   <a name="opensearchservice-Type-OutboundConnection-ConnectionAlias"></a>
Name of the connection.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[a-zA-Z][a-zA-Z0-9\-\_]+`
Required: No

 ** ConnectionId **   <a name="opensearchservice-Type-OutboundConnection-ConnectionId"></a>
Unique identifier of the connection.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 256.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** ConnectionMode **   <a name="opensearchservice-Type-OutboundConnection-ConnectionMode"></a>
The connection mode.
Type: String
Valid Values: `DIRECT | VPC_ENDPOINT`
Required: No

 ** ConnectionProperties **   <a name="opensearchservice-Type-OutboundConnection-ConnectionProperties"></a>
Properties for the outbound connection.
Type: [ConnectionProperties](API_ConnectionProperties.md) object
Required: No

 ** ConnectionStatus **   <a name="opensearchservice-Type-OutboundConnection-ConnectionStatus"></a>
Status of the connection.
Type: [OutboundConnectionStatus](API_OutboundConnectionStatus.md) object
Required: No

 ** LocalDomainInfo **   <a name="opensearchservice-Type-OutboundConnection-LocalDomainInfo"></a>
Information about the source (local) domain.
Type: [DomainInformationContainer](API_DomainInformationContainer.md) object
Required: No

 ** RemoteDomainInfo **   <a name="opensearchservice-Type-OutboundConnection-RemoteDomainInfo"></a>
Information about the destination (remote) domain.
Type: [DomainInformationContainer](API_DomainInformationContainer.md) object
Required: No

## See Also
<a name="API_OutboundConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/OutboundConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/OutboundConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/OutboundConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
