---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GraphDataSummary.html
---

# GraphDataSummary
<a name="API_GraphDataSummary"></a>

Summary information about the graph.

## Contents
<a name="API_GraphDataSummary_Contents"></a>

 ** edgeLabels **   <a name="neptunegraph-Type-GraphDataSummary-edgeLabels"></a>
A list of the edge labels in the graph.
Type: Array of strings
Required: No

 ** edgeProperties **   <a name="neptunegraph-Type-GraphDataSummary-edgeProperties"></a>
A list of the distinct edge properties in the graph, along with the count of edges where each property is used.
Type: Array of string to long maps
Required: No

 ** edgeStructures **   <a name="neptunegraph-Type-GraphDataSummary-edgeStructures"></a>
This field is only present when the requested mode is DETAILED. It contains a list of edge structures.
Type: Array of [EdgeStructure](API_EdgeStructure.md) objects
Required: No

 ** nodeLabels **   <a name="neptunegraph-Type-GraphDataSummary-nodeLabels"></a>
A list of distinct node labels in the graph.
Type: Array of strings
Required: No

 ** nodeProperties **   <a name="neptunegraph-Type-GraphDataSummary-nodeProperties"></a>
A list of the distinct node properties in the graph, along with the count of nodes where each property is used.
Type: Array of string to long maps
Required: No

 ** nodeStructures **   <a name="neptunegraph-Type-GraphDataSummary-nodeStructures"></a>
This field is only present when the requested mode is DETAILED. It contains a list of node structures.
Type: Array of [NodeStructure](API_NodeStructure.md) objects
Required: No

 ** numEdgeLabels **   <a name="neptunegraph-Type-GraphDataSummary-numEdgeLabels"></a>
The number of unique edge labels in the graph.
Type: Long
Required: No

 ** numEdgeProperties **   <a name="neptunegraph-Type-GraphDataSummary-numEdgeProperties"></a>
The number of edge properties in the graph.
Type: Long
Required: No

 ** numEdges **   <a name="neptunegraph-Type-GraphDataSummary-numEdges"></a>
The number of edges in the graph.
Type: Long
Required: No

 ** numNodeLabels **   <a name="neptunegraph-Type-GraphDataSummary-numNodeLabels"></a>
The number of distinct node labels in the graph.
Type: Long
Required: No

 ** numNodeProperties **   <a name="neptunegraph-Type-GraphDataSummary-numNodeProperties"></a>
The number of distinct node properties in the graph.
Type: Long
Required: No

 ** numNodes **   <a name="neptunegraph-Type-GraphDataSummary-numNodes"></a>
The number of nodes in the graph.
Type: Long
Required: No

 ** totalEdgePropertyValues **   <a name="neptunegraph-Type-GraphDataSummary-totalEdgePropertyValues"></a>
The total number of usages of all edge properties.
Type: Long
Required: No

 ** totalNodePropertyValues **   <a name="neptunegraph-Type-GraphDataSummary-totalNodePropertyValues"></a>
The total number of usages of all node properties.
Type: Long
Required: No

## See Also
<a name="API_GraphDataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/GraphDataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/GraphDataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/GraphDataSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
