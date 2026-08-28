---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_OutpostConfigResponse.html
---

# OutpostConfigResponse
<a name="API_OutpostConfigResponse"></a>

An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost. This API isn't available for Amazon EKS clusters on the AWS cloud.

## Contents
<a name="API_OutpostConfigResponse_Contents"></a>

 ** controlPlaneInstanceType **   <a name="AmazonEKS-Type-OutpostConfigResponse-controlPlaneInstanceType"></a>
The Amazon EC2 instance type for the Kubernetes control plane instances of your local Amazon EKS cluster on AWS Outposts. The instance type is the same for all control plane instances.
Type: String
Required: Yes

 ** outpostArns **   <a name="AmazonEKS-Type-OutpostConfigResponse-outpostArns"></a>
The ARN of the Outpost that you specified for use with your local Amazon EKS cluster on Outposts.
Type: Array of strings
Required: Yes

 ** controlPlanePlacement **   <a name="AmazonEKS-Type-OutpostConfigResponse-controlPlanePlacement"></a>
An object representing the placement configuration for all the control plane instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.
Type: [ControlPlanePlacementResponse](API_ControlPlanePlacementResponse.md) object
Required: No

 ** etcdInstanceType **   <a name="AmazonEKS-Type-OutpostConfigResponse-etcdInstanceType"></a>
The Amazon EC2 instance type for etcd instances of your local Amazon EKS cluster on AWS Outposts. The instance type is the same for all etcd instances.
Type: String
Required: No

 ** etcdPlacement **   <a name="AmazonEKS-Type-OutpostConfigResponse-etcdPlacement"></a>
An object representing the placement configuration for the etcd instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.
Type: [EtcdPlacementResponse](API_EtcdPlacementResponse.md) object
Required: No

## See Also
<a name="API_OutpostConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/OutpostConfigResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/OutpostConfigResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/OutpostConfigResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
