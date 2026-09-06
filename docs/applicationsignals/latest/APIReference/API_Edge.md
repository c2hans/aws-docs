---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Edge.html
---

# Edge
<a name="API_Edge"></a>

A structure that represents a connection between two nodes in a dependency graph, showing the relationship and characteristics of the connection.

## Contents
<a name="API_Edge_Contents"></a>

 ** ConnectionType **   <a name="applicationsignals-Type-Edge-ConnectionType"></a>
The type of connection between the nodes, indicating the nature of the relationship.
Type: String
Valid Values: `INDIRECT | DIRECT`
Required: No

 ** DestinationNodeId **   <a name="applicationsignals-Type-Edge-DestinationNodeId"></a>
The identifier of the destination node in this edge connection.
Type: String
Required: No

 ** Duration **   <a name="applicationsignals-Type-Edge-Duration"></a>
The duration or latency associated with this connection, if applicable.
Type: Double
Required: No

 ** SourceNodeId **   <a name="applicationsignals-Type-Edge-SourceNodeId"></a>
The identifier of the source node in this edge connection.
Type: String
Required: No

## See Also
<a name="API_Edge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/Edge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/Edge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/Edge)
