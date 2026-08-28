---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_WorkflowGraph.html
---

# WorkflowGraph
<a name="API_WorkflowGraph"></a>

A workflow graph represents the complete workflow containing all the AWS Glue components present in the workflow and all the directed connections between them.

## Contents
<a name="API_WorkflowGraph_Contents"></a>

 ** Edges **   <a name="Glue-Type-WorkflowGraph-Edges"></a>
A list of all the directed connections between the nodes belonging to the workflow.
Type: Array of [Edge](API_Edge.md) objects
Required: No

 ** Nodes **   <a name="Glue-Type-WorkflowGraph-Nodes"></a>
A list of the the AWS Glue components belong to the workflow represented as nodes.
Type: Array of [Node](API_Node.md) objects
Required: No

## See Also
<a name="API_WorkflowGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/WorkflowGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/WorkflowGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/WorkflowGraph)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
