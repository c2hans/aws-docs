---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_NeighborConnectionDetail.html
---

# NeighborConnectionDetail
<a name="API_NeighborConnectionDetail"></a>

Details about neighboring servers.

## Contents
<a name="API_NeighborConnectionDetail_Contents"></a>

 ** connectionsCount **   <a name="DiscServ-Type-NeighborConnectionDetail-connectionsCount"></a>
The number of open network connections with the neighboring server.
Type: Long
Required: Yes

 ** destinationServerId **   <a name="DiscServ-Type-NeighborConnectionDetail-destinationServerId"></a>
The ID of the server that accepted the network connection.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: Yes

 ** sourceServerId **   <a name="DiscServ-Type-NeighborConnectionDetail-sourceServerId"></a>
The ID of the server that opened the network connection.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: Yes

 ** destinationPort **   <a name="DiscServ-Type-NeighborConnectionDetail-destinationPort"></a>
The destination network port for the connection.
Type: Integer
Required: No

 ** transportProtocol **   <a name="DiscServ-Type-NeighborConnectionDetail-transportProtocol"></a>
The network protocol used for the connection.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_NeighborConnectionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/NeighborConnectionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/NeighborConnectionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/NeighborConnectionDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
