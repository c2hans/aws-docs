---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchRebootClusterNodeLogicalIdsError.html
---

# BatchRebootClusterNodeLogicalIdsError
<a name="API_BatchRebootClusterNodeLogicalIdsError"></a>

Represents an error encountered when rebooting a node (identified by its logical node ID) from a SageMaker HyperPod cluster.

## Contents
<a name="API_BatchRebootClusterNodeLogicalIdsError_Contents"></a>

 ** ErrorCode **   <a name="sagemaker-Type-BatchRebootClusterNodeLogicalIdsError-ErrorCode"></a>
The error code associated with the error encountered when rebooting a node by logical node ID.
Possible values:
+  `InstanceIdNotFound`: The node does not exist in the specified cluster.
+  `InvalidInstanceStatus`: The node is in a state that does not allow rebooting. Wait for the node to finish any ongoing changes before retrying.
+  `InstanceIdInUse`: Another operation is already in progress for this node. Wait for the operation to complete before retrying.
+  `InternalServerError`: An internal error occurred while processing this node.
Type: String
Valid Values: `InstanceIdNotFound | InvalidInstanceStatus | InstanceIdInUse | InternalServerError`
Required: Yes

 ** Message **   <a name="sagemaker-Type-BatchRebootClusterNodeLogicalIdsError-Message"></a>
A human-readable message describing the error encountered when rebooting a node by logical node ID.
Type: String
Required: Yes

 ** NodeLogicalId **   <a name="sagemaker-Type-BatchRebootClusterNodeLogicalIdsError-NodeLogicalId"></a>
The logical node ID of the node that encountered an error during the reboot operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`
Required: Yes

## See Also
<a name="API_BatchRebootClusterNodeLogicalIdsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchRebootClusterNodeLogicalIdsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchRebootClusterNodeLogicalIdsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchRebootClusterNodeLogicalIdsError)
