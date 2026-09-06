---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DependencyGraph.html
---

# DependencyGraph
<a name="API_DependencyGraph"></a>

A structure that represents the dependency relationships relevant to an audit finding, containing nodes and edges that show how services and resources are connected.

## Contents
<a name="API_DependencyGraph_Contents"></a>

 ** Edges **   <a name="applicationsignals-Type-DependencyGraph-Edges"></a>
An array of edges representing the connections and relationships between the nodes in the dependency graph.
Type: Array of [Edge](API_Edge.md) objects
Required: No

 ** Nodes **   <a name="applicationsignals-Type-DependencyGraph-Nodes"></a>
An array of nodes representing the services, resources, or other entities in the dependency graph.
Type: Array of [Node](API_Node.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

## See Also
<a name="API_DependencyGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/DependencyGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/DependencyGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/DependencyGraph)
