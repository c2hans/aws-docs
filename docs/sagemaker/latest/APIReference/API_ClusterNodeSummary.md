---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterNodeSummary.html
---

# ClusterNodeSummary
<a name="API_ClusterNodeSummary"></a>

Lists a summary of the properties of an instance (also called a *node* interchangeably) of a SageMaker HyperPod cluster.

## Contents
<a name="API_ClusterNodeSummary_Contents"></a>

 ** InstanceGroupName **   <a name="sagemaker-Type-ClusterNodeSummary-InstanceGroupName"></a>
The name of the instance group in which the instance is.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** InstanceId **   <a name="sagemaker-Type-ClusterNodeSummary-InstanceId"></a>
The ID of the instance.
Type: String
Required: Yes

 ** InstanceStatus **   <a name="sagemaker-Type-ClusterNodeSummary-InstanceStatus"></a>
The status of the instance.
Type: [ClusterInstanceStatusDetails](API_ClusterInstanceStatusDetails.md) object
Required: Yes

 ** InstanceType **   <a name="sagemaker-Type-ClusterNodeSummary-InstanceType"></a>
The type of the instance.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5.4xlarge | ml.p6e-gb200.36xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.c5n.large | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.gr6.4xlarge | ml.gr6.8xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge | ml.trn2.3xlarge | ml.trn2.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.i3en.large | ml.i3en.xlarge | ml.i3en.2xlarge | ml.i3en.3xlarge | ml.i3en.6xlarge | ml.i3en.12xlarge | ml.i3en.24xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.r5d.16xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p6-b300.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.c6g.medium | ml.c6g.large | ml.c6g.xlarge | ml.c6g.2xlarge | ml.c6g.4xlarge | ml.c6g.8xlarge | ml.c6g.12xlarge | ml.c6g.16xlarge | ml.c7g.medium | ml.c7g.large | ml.c7g.xlarge | ml.c7g.2xlarge | ml.c7g.4xlarge | ml.c7g.8xlarge | ml.c7g.12xlarge | ml.c7g.16xlarge | ml.c8g.medium | ml.c8g.large | ml.c8g.xlarge | ml.c8g.2xlarge | ml.c8g.4xlarge | ml.c8g.8xlarge | ml.c8g.12xlarge | ml.c8g.16xlarge | ml.c8g.24xlarge | ml.c8g.48xlarge | ml.c6a.large | ml.c6a.xlarge | ml.c6a.2xlarge | ml.c6a.4xlarge | ml.c6a.8xlarge | ml.c6a.12xlarge | ml.c6a.16xlarge | ml.c6a.24xlarge | ml.c6a.32xlarge | ml.c6a.48xlarge | ml.m6a.large | ml.m6a.xlarge | ml.m6a.2xlarge | ml.m6a.4xlarge | ml.m6a.8xlarge | ml.m6a.12xlarge | ml.m6a.16xlarge | ml.m6a.24xlarge | ml.m6a.32xlarge | ml.m6a.48xlarge | ml.m6g.medium | ml.m6g.large | ml.m6g.xlarge | ml.m6g.2xlarge | ml.m6g.4xlarge | ml.m6g.8xlarge | ml.m6g.12xlarge | ml.m6g.16xlarge | ml.m7g.medium | ml.m7g.large | ml.m7g.xlarge | ml.m7g.2xlarge | ml.m7g.4xlarge | ml.m7g.8xlarge | ml.m7g.12xlarge | ml.m7g.16xlarge | ml.m8g.medium | ml.m8g.large | ml.m8g.xlarge | ml.m8g.2xlarge | ml.m8g.4xlarge | ml.m8g.8xlarge | ml.m8g.12xlarge | ml.m8g.16xlarge | ml.m8g.24xlarge | ml.m8g.48xlarge`
Required: Yes

 ** LaunchTime **   <a name="sagemaker-Type-ClusterNodeSummary-LaunchTime"></a>
The time when the instance is launched.
Type: Timestamp
Required: Yes

 ** CurrentImageReleaseVersion **   <a name="sagemaker-Type-ClusterNodeSummary-CurrentImageReleaseVersion"></a>
The version of the HyperPod-managed AMI currently running on the node.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: No

 ** ImageVersionStatus **   <a name="sagemaker-Type-ClusterNodeSummary-ImageVersionStatus"></a>
The status of the image version for the cluster node.
Type: String
Valid Values: `UpToDate | UpdateAvailable | SecurityUpdateRequired | EndOfLife`
Required: No

 ** LastSoftwareUpdateTime **   <a name="sagemaker-Type-ClusterNodeSummary-LastSoftwareUpdateTime"></a>
The time when SageMaker last updated the software of the instances in the cluster.
Type: Timestamp
Required: No

 ** NodeLogicalId **   <a name="sagemaker-Type-ClusterNodeSummary-NodeLogicalId"></a>
A unique identifier for the node that persists throughout its lifecycle, from provisioning request to termination. This identifier can be used to track the node even before it has an assigned `InstanceId`. This field is only included when `IncludeNodeLogicalIds` is set to `True` in the `ListClusterNodes` request.
Type: String
Required: No

 ** PrivateDnsHostname **   <a name="sagemaker-Type-ClusterNodeSummary-PrivateDnsHostname"></a>
The private DNS hostname of the SageMaker HyperPod cluster node.
Type: String
Pattern: `ip-((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)-?\b){4}\..*`
Required: No

 ** UltraServerInfo **   <a name="sagemaker-Type-ClusterNodeSummary-UltraServerInfo"></a>
Contains information about the UltraServer.
Type: [UltraServerInfo](API_UltraServerInfo.md) object
Required: No

## See Also
<a name="API_ClusterNodeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterNodeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterNodeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterNodeSummary)
