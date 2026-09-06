---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchRebootClusterNodesError.html
---

# BatchRebootClusterNodesError
<a name="API_BatchRebootClusterNodesError"></a>

Represents an error encountered when rebooting a node from a SageMaker HyperPod cluster.

## Contents
<a name="API_BatchRebootClusterNodesError_Contents"></a>

 ** ErrorCode **   <a name="sagemaker-Type-BatchRebootClusterNodesError-ErrorCode"></a>
The error code associated with the error encountered when rebooting a node.
Possible values:
+  `InstanceIdNotFound`: The instance does not exist in the specified cluster.
+  `InvalidInstanceStatus`: The instance is in a state that does not allow rebooting. Wait for the instance to finish any ongoing changes before retrying.
+  `InstanceIdInUse`: Another operation is already in progress for this node. Wait for the operation to complete before retrying.
+  `InternalServerError`: An internal error occurred while processing this node.
Type: String
Valid Values: `InstanceIdNotFound | InvalidInstanceStatus | InstanceIdInUse | InternalServerError`
Required: Yes

 ** Message **   <a name="sagemaker-Type-BatchRebootClusterNodesError-Message"></a>
A human-readable message describing the error encountered when rebooting a node.
Type: String
Required: Yes

 ** NodeId **   <a name="sagemaker-Type-BatchRebootClusterNodesError-NodeId"></a>
The EC2 instance ID of the node that encountered an error during the reboot operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: Yes

## See Also
<a name="API_BatchRebootClusterNodesError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchRebootClusterNodesError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchRebootClusterNodesError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchRebootClusterNodesError)
