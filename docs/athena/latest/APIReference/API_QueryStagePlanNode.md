---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_QueryStagePlanNode.html
---

# QueryStagePlanNode
<a name="API_QueryStagePlanNode"></a>

Stage plan information such as name, identifier, sub plans, and remote sources.

## Contents
<a name="API_QueryStagePlanNode_Contents"></a>

 ** Children **   <a name="athena-Type-QueryStagePlanNode-Children"></a>
Stage plan information such as name, identifier, sub plans, and remote sources of child plan nodes/
Type: Array of [QueryStagePlanNode](#API_QueryStagePlanNode) objects
Required: No

 ** Identifier **   <a name="athena-Type-QueryStagePlanNode-Identifier"></a>
Information about the operation this query stage plan node is performing.
Type: String
Required: No

 ** Name **   <a name="athena-Type-QueryStagePlanNode-Name"></a>
Name of the query stage plan that describes the operation this stage is performing as part of query execution.
Type: String
Required: No

 ** RemoteSources **   <a name="athena-Type-QueryStagePlanNode-RemoteSources"></a>
Source plan node IDs.
Type: Array of strings
Required: No

## See Also
<a name="API_QueryStagePlanNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/QueryStagePlanNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/QueryStagePlanNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/QueryStagePlanNode)
