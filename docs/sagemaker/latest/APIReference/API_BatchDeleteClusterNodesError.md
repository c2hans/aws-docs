---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDeleteClusterNodesError.html
---

# BatchDeleteClusterNodesError
<a name="API_BatchDeleteClusterNodesError"></a>

Represents an error encountered when deleting a node from a SageMaker HyperPod cluster.

## Contents
<a name="API_BatchDeleteClusterNodesError_Contents"></a>

 ** Code **   <a name="sagemaker-Type-BatchDeleteClusterNodesError-Code"></a>
The error code associated with the error encountered when deleting a node.
The code provides information about the specific issue encountered, such as the node not being found, the node's status being invalid for deletion, or the node ID being in use by another process.
Type: String
Valid Values: `NodeIdNotFound | InvalidNodeStatus | NodeIdInUse`
Required: Yes

 ** Message **   <a name="sagemaker-Type-BatchDeleteClusterNodesError-Message"></a>
A message describing the error encountered when deleting a node.
Type: String
Required: Yes

 ** NodeId **   <a name="sagemaker-Type-BatchDeleteClusterNodesError-NodeId"></a>
The ID of the node that encountered an error during the deletion process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: Yes

## See Also
<a name="API_BatchDeleteClusterNodesError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchDeleteClusterNodesError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchDeleteClusterNodesError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchDeleteClusterNodesError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
