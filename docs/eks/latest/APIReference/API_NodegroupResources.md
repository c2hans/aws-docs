---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_NodegroupResources.html
---

# NodegroupResources
<a name="API_NodegroupResources"></a>

An object representing the resources associated with the node group, such as Auto Scaling groups and security groups for remote access.

## Contents
<a name="API_NodegroupResources_Contents"></a>

 ** autoScalingGroups **   <a name="AmazonEKS-Type-NodegroupResources-autoScalingGroups"></a>
The Auto Scaling groups associated with the node group.
Type: Array of [AutoScalingGroup](API_AutoScalingGroup.md) objects
Required: No

 ** remoteAccessSecurityGroup **   <a name="AmazonEKS-Type-NodegroupResources-remoteAccessSecurityGroup"></a>
The remote access security group associated with the node group. This security group controls SSH access to the nodes.
Type: String
Required: No

## See Also
<a name="API_NodegroupResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/NodegroupResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/NodegroupResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/NodegroupResources)
