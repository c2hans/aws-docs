---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MoveClusterNodesError.html
---

# MoveClusterNodesError

Describes why a node, identified by its instance ID, could not be moved in a `MoveClusterNodes` request. Contains the instance ID, an error code, and an error message.

## Contents
<a name="API_MoveClusterNodesError_Contents"></a>

 ** Code **   <a name="sagemaker-Type-MoveClusterNodesError-Code"></a>
The error code associated with the error encountered when moving the node. The error code is one of the following values:
+  `NodeIdNotFound`: The node does not exist in the source instance group.
+  `InvalidNodeStatus`: The node is not in a state that allows the move. For example, the node is not `Running`, is not in a subnet of the target instance group, or has an attached Amazon EBS volume that you must detach first.
+  `NodeIdInUse`: Another operation is already in progress for this node. Wait for the operation to complete before retrying.
+  `NodeInstanceTypeMismatch`: The target instance group does not support the node's instance type.
Type: String
Valid Values: `NodeIdNotFound | InvalidNodeStatus | NodeIdInUse | NodeInstanceTypeMismatch`
Required: Yes

 ** Message **   <a name="sagemaker-Type-MoveClusterNodesError-Message"></a>
A human-readable message describing the error encountered when moving the node.
Type: String
Required: Yes

 ** NodeId **   <a name="sagemaker-Type-MoveClusterNodesError-NodeId"></a>
The instance ID of the node that could not be moved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: Yes

## See Also
<a name="API_MoveClusterNodesError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MoveClusterNodesError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MoveClusterNodesError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MoveClusterNodesError)
