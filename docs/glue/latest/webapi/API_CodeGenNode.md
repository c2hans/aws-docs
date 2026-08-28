---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CodeGenNode.html
---

# CodeGenNode
<a name="API_CodeGenNode"></a>

Represents a node in a directed acyclic graph (DAG)

## Contents
<a name="API_CodeGenNode_Contents"></a>

 ** Args **   <a name="Glue-Type-CodeGenNode-Args"></a>
Properties of the node, in the form of name-value pairs.
Type: Array of [CodeGenNodeArg](API_CodeGenNodeArg.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: Yes

 ** Id **   <a name="Glue-Type-CodeGenNode-Id"></a>
A node identifier that is unique within the node's graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z_][A-Za-z0-9_]*`
Required: Yes

 ** NodeType **   <a name="Glue-Type-CodeGenNode-NodeType"></a>
The type of node that this is.
Type: String
Required: Yes

 ** LineNumber **   <a name="Glue-Type-CodeGenNode-LineNumber"></a>
The line number of the node.
Type: Integer
Required: No

## See Also
<a name="API_CodeGenNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CodeGenNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CodeGenNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CodeGenNode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
