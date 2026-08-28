---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_NodeDetails.html
---

# NodeDetails
<a name="API_NodeDetails"></a>

An object that represents the details of a multi-node parallel job node.

## Contents
<a name="API_NodeDetails_Contents"></a>

 ** isMainNode **   <a name="Batch-Type-NodeDetails-isMainNode"></a>
Specifies whether the current node is the main node for a multi-node parallel job.
Type: Boolean
Required: No

 ** nodeIndex **   <a name="Batch-Type-NodeDetails-nodeIndex"></a>
The node index for the node. Node index numbering starts at zero. This index is also available on the node with the `AWS_BATCH_JOB_NODE_INDEX` environment variable.
Type: Integer
Required: No

## See Also
<a name="API_NodeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NodeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NodeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NodeDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
