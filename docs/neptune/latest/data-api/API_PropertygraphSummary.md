---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_PropertygraphSummary.html
---

# PropertygraphSummary
<a name="API_PropertygraphSummary"></a>

The graph summary API returns a read-only list of node and edge labels and property keys, along with counts of nodes, edges, and properties. See [Graph summary response for a property graph (PG)](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-graph-summary.html#neptune-graph-summary-pg-response).

## Contents
<a name="API_PropertygraphSummary_Contents"></a>

 ** edgeLabels **   <a name="neptunedata-Type-PropertygraphSummary-edgeLabels"></a>
A list of the distinct edge labels in the graph.
Type: Array of strings
Required: No

 ** edgeProperties **   <a name="neptunedata-Type-PropertygraphSummary-edgeProperties"></a>
A list of the distinct edge properties in the graph, along with the count of edges where each property is used.
Type: Array of string to long maps
Required: No

 ** edgeStructures **   <a name="neptunedata-Type-PropertygraphSummary-edgeStructures"></a>
This field is only present when the requested mode is `DETAILED`. It contains a list of edge structures.
Type: Array of [EdgeStructure](API_EdgeStructure.md) objects
Required: No

 ** nodeLabels **   <a name="neptunedata-Type-PropertygraphSummary-nodeLabels"></a>
A list of the distinct node labels in the graph.
Type: Array of strings
Required: No

 ** nodeProperties **   <a name="neptunedata-Type-PropertygraphSummary-nodeProperties"></a>
The number of distinct node properties in the graph.
Type: Array of string to long maps
Required: No

 ** nodeStructures **   <a name="neptunedata-Type-PropertygraphSummary-nodeStructures"></a>
This field is only present when the requested mode is `DETAILED`. It contains a list of node structures.
Type: Array of [NodeStructure](API_NodeStructure.md) objects
Required: No

 ** numEdgeLabels **   <a name="neptunedata-Type-PropertygraphSummary-numEdgeLabels"></a>
The number of distinct edge labels in the graph.
Type: Long
Required: No

 ** numEdgeProperties **   <a name="neptunedata-Type-PropertygraphSummary-numEdgeProperties"></a>
The number of distinct edge properties in the graph.
Type: Long
Required: No

 ** numEdges **   <a name="neptunedata-Type-PropertygraphSummary-numEdges"></a>
The number of edges in the graph.
Type: Long
Required: No

 ** numNodeLabels **   <a name="neptunedata-Type-PropertygraphSummary-numNodeLabels"></a>
The number of distinct node labels in the graph.
Type: Long
Required: No

 ** numNodeProperties **   <a name="neptunedata-Type-PropertygraphSummary-numNodeProperties"></a>
A list of the distinct node properties in the graph, along with the count of nodes where each property is used.
Type: Long
Required: No

 ** numNodes **   <a name="neptunedata-Type-PropertygraphSummary-numNodes"></a>
The number of nodes in the graph.
Type: Long
Required: No

 ** totalEdgePropertyValues **   <a name="neptunedata-Type-PropertygraphSummary-totalEdgePropertyValues"></a>
The total number of usages of all edge properties.
Type: Long
Required: No

 ** totalNodePropertyValues **   <a name="neptunedata-Type-PropertygraphSummary-totalNodePropertyValues"></a>
The total number of usages of all node properties.
Type: Long
Required: No

## See Also
<a name="API_PropertygraphSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/PropertygraphSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/PropertygraphSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/PropertygraphSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
