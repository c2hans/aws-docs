---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CodeGenEdge.html
---

# CodeGenEdge
<a name="API_CodeGenEdge"></a>

Represents a directional edge in a directed acyclic graph (DAG).

## Contents
<a name="API_CodeGenEdge_Contents"></a>

 ** Source **   <a name="Glue-Type-CodeGenEdge-Source"></a>
The ID of the node at which the edge starts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z_][A-Za-z0-9_]*`
Required: Yes

 ** Target **   <a name="Glue-Type-CodeGenEdge-Target"></a>
The ID of the node at which the edge ends.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z_][A-Za-z0-9_]*`
Required: Yes

 ** TargetParameter **   <a name="Glue-Type-CodeGenEdge-TargetParameter"></a>
The target of the edge.
Type: String
Required: No

## See Also
<a name="API_CodeGenEdge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CodeGenEdge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CodeGenEdge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CodeGenEdge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
