---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterNodeDetails.html
---

# ClusterNodeDetails
<a name="API_ClusterNodeDetails"></a>

Details of an instance (also called a *node* interchangeably) in a SageMaker HyperPod cluster.

## Contents
<a name="API_ClusterNodeDetails_Contents"></a>

 ** CapacityType **   <a name="sagemaker-Type-ClusterNodeDetails-CapacityType"></a>
The capacity type of the node. Valid values are `OnDemand` and `Spot`. When set to `OnDemand`, the node is launched as an On-Demand instance. When set to `Spot`, the node is launched as a Spot instance.
Type: String
Valid Values: `Spot | OnDemand`
Required: No

 ** CurrentImageId **   <a name="sagemaker-Type-ClusterNodeDetails-CurrentImageId"></a>
The ID of the Amazon Machine Image (AMI) currently in use by the node.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 21.
Pattern: `ami-[0-9a-fA-F]{8,17}|default`
Required: No

 ** CurrentImageReleaseVersion **   <a name="sagemaker-Type-ClusterNodeDetails-CurrentImageReleaseVersion"></a>
The version of the HyperPod-managed AMI currently running on the node.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: No

 ** DesiredImageId **   <a name="sagemaker-Type-ClusterNodeDetails-DesiredImageId"></a>
The ID of the Amazon Machine Image (AMI) desired for the node.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 21.
Pattern: `ami-[0-9a-fA-F]{8,17}|default`
Required: No

 ** DesiredImageReleaseVersion **   <a name="sagemaker-Type-ClusterNodeDetails-DesiredImageReleaseVersion"></a>
The desired version of the HyperPod-managed AMI for the node. This may differ from the current version when an update is pending.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: No

 ** ImageVersionStatus **   <a name="sagemaker-Type-ClusterNodeDetails-ImageVersionStatus"></a>
The status of the image version for the cluster node.
Type: String
Valid Values: `UpToDate | UpdateAvailable | SecurityUpdateRequired | EndOfLife`
Required: No

 ** InstanceGroupName **   <a name="sagemaker-Type-ClusterNodeDetails-InstanceGroupName"></a>
The instance group name in which the instance is.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** InstanceId **   <a name="sagemaker-Type-ClusterNodeDetails-InstanceId"></a>
The ID of the instance.
Type: String
Required: No

 ** InstanceStatus **   <a name="sagemaker-Type-ClusterNodeDetails-InstanceStatus"></a>
The status of the instance.
Type: [ClusterInstanceStatusDetails](API_ClusterInstanceStatusDetails.md) object
Required: No

 ** InstanceStorageConfigs **   <a name="sagemaker-Type-ClusterNodeDetails-InstanceStorageConfigs"></a>
The configurations of additional storage specified to the instance group where the instance (node) is launched.
Type: Array of [ClusterInstanceStorageConfig](API_ClusterInstanceStorageConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

 ** InstanceType **   <a name="sagemaker-Type-ClusterNodeDetails-InstanceType"></a>
The type of the instance.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5.4xlarge | ml.p6e-gb200.36xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.c5n.large | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.gr6.4xlarge | ml.gr6.8xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge | ml.trn2.3xlarge | ml.trn2.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.i3en.large | ml.i3en.xlarge | ml.i3en.2xlarge | ml.i3en.3xlarge | ml.i3en.6xlarge | ml.i3en.12xlarge | ml.i3en.24xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.r5d.16xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p6-b300.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.c6g.medium | ml.c6g.large | ml.c6g.xlarge | ml.c6g.2xlarge | ml.c6g.4xlarge | ml.c6g.8xlarge | ml.c6g.12xlarge | ml.c6g.16xlarge | ml.c7g.medium | ml.c7g.large | ml.c7g.xlarge | ml.c7g.2xlarge | ml.c7g.4xlarge | ml.c7g.8xlarge | ml.c7g.12xlarge | ml.c7g.16xlarge | ml.c8g.medium | ml.c8g.large | ml.c8g.xlarge | ml.c8g.2xlarge | ml.c8g.4xlarge | ml.c8g.8xlarge | ml.c8g.12xlarge | ml.c8g.16xlarge | ml.c8g.24xlarge | ml.c8g.48xlarge | ml.c6a.large | ml.c6a.xlarge | ml.c6a.2xlarge | ml.c6a.4xlarge | ml.c6a.8xlarge | ml.c6a.12xlarge | ml.c6a.16xlarge | ml.c6a.24xlarge | ml.c6a.32xlarge | ml.c6a.48xlarge | ml.m6a.large | ml.m6a.xlarge | ml.m6a.2xlarge | ml.m6a.4xlarge | ml.m6a.8xlarge | ml.m6a.12xlarge | ml.m6a.16xlarge | ml.m6a.24xlarge | ml.m6a.32xlarge | ml.m6a.48xlarge | ml.m6g.medium | ml.m6g.large | ml.m6g.xlarge | ml.m6g.2xlarge | ml.m6g.4xlarge | ml.m6g.8xlarge | ml.m6g.12xlarge | ml.m6g.16xlarge | ml.m7g.medium | ml.m7g.large | ml.m7g.xlarge | ml.m7g.2xlarge | ml.m7g.4xlarge | ml.m7g.8xlarge | ml.m7g.12xlarge | ml.m7g.16xlarge | ml.m8g.medium | ml.m8g.large | ml.m8g.xlarge | ml.m8g.2xlarge | ml.m8g.4xlarge | ml.m8g.8xlarge | ml.m8g.12xlarge | ml.m8g.16xlarge | ml.m8g.24xlarge | ml.m8g.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge`
Required: No

 ** KubernetesConfig **   <a name="sagemaker-Type-ClusterNodeDetails-KubernetesConfig"></a>
The Kubernetes configuration applied to this node, showing both the current and desired state of labels and taints. The cluster works to reconcile the actual state with the declared state.
Type: [ClusterKubernetesConfigNodeDetails](API_ClusterKubernetesConfigNodeDetails.md) object
Required: No

 ** LifeCycleConfig **   <a name="sagemaker-Type-ClusterNodeDetails-LifeCycleConfig"></a>
The LifeCycle configuration applied to the instance.
Type: [ClusterLifeCycleConfig](API_ClusterLifeCycleConfig.md) object
Required: No

 ** NetworkInterface **   <a name="sagemaker-Type-ClusterNodeDetails-NetworkInterface"></a>
The network interface configuration for the cluster node.
Type: [ClusterNetworkInterfaceDetails](API_ClusterNetworkInterfaceDetails.md) object
Required: No

 ** NodeLogicalId **   <a name="sagemaker-Type-ClusterNodeDetails-NodeLogicalId"></a>
A unique identifier for the node that persists throughout its lifecycle, from provisioning request to termination. This identifier can be used to track the node even before it has an assigned `InstanceId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`
Required: No

 ** OverrideVpcConfig **   <a name="sagemaker-Type-ClusterNodeDetails-OverrideVpcConfig"></a>
The customized Amazon VPC configuration at the instance group level that overrides the default Amazon VPC configuration of the SageMaker HyperPod cluster.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

 ** Placement **   <a name="sagemaker-Type-ClusterNodeDetails-Placement"></a>
The placement details of the SageMaker HyperPod cluster node.
Type: [ClusterInstancePlacement](API_ClusterInstancePlacement.md) object
Required: No

 ** PrivateDnsHostname **   <a name="sagemaker-Type-ClusterNodeDetails-PrivateDnsHostname"></a>
The private DNS hostname of the SageMaker HyperPod cluster node.
Type: String
Pattern: `ip-((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)-?\b){4}\..*`
Required: No

 ** PrivatePrimaryIp **   <a name="sagemaker-Type-ClusterNodeDetails-PrivatePrimaryIp"></a>
The private primary IP address of the SageMaker HyperPod cluster node.
Type: String
Pattern: `((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}`
Required: No

 ** PrivatePrimaryIpv6 **   <a name="sagemaker-Type-ClusterNodeDetails-PrivatePrimaryIpv6"></a>
The private primary IPv6 address of the SageMaker HyperPod cluster node when configured with an Amazon VPC that supports IPv6 and includes subnets with IPv6 addressing enabled in either the cluster Amazon VPC configuration or the instance group Amazon VPC configuration.
Type: String
Required: No

 ** ThreadsPerCore **   <a name="sagemaker-Type-ClusterNodeDetails-ThreadsPerCore"></a>
The number of threads per CPU core you specified under `CreateCluster`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: No

 ** UltraServerInfo **   <a name="sagemaker-Type-ClusterNodeDetails-UltraServerInfo"></a>
Contains information about the UltraServer.
Type: [UltraServerInfo](API_UltraServerInfo.md) object
Required: No

## See Also
<a name="API_ClusterNodeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterNodeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterNodeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterNodeDetails)
