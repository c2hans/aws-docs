---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceGroupSpecification.html
---

# ClusterInstanceGroupSpecification
<a name="API_ClusterInstanceGroupSpecification"></a>

The specifications of an instance group that you need to define.

## Contents
<a name="API_ClusterInstanceGroupSpecification_Contents"></a>

 ** ExecutionRole **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-ExecutionRole"></a>
Specifies an IAM execution role to be assumed by the instance group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** InstanceCount **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-InstanceCount"></a>
Specifies the number of instances to add to the instance group of a SageMaker HyperPod cluster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6758.
Required: Yes

 ** InstanceGroupName **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-InstanceGroupName"></a>
Specifies the name of the instance group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** AutoPatchConfig **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-AutoPatchConfig"></a>
The configuration for automatic OS security patching. If present, the system automatically applies PATCH AMI updates to this instance group.
Type: [ClusterAutoPatchConfig](API_ClusterAutoPatchConfig.md) object
Required: No

 ** CapacityRequirements **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-CapacityRequirements"></a>
Specifies the capacity requirements for the instance group.
Type: [ClusterCapacityRequirements](API_ClusterCapacityRequirements.md) object
Required: No

 ** ImageId **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-ImageId"></a>
When configuring your HyperPod cluster, you can specify an image ID using one of the following options:
+  `HyperPodPublicAmiId`: Use a HyperPod public AMI
+  `CustomAmiId`: Use your custom AMI
+  `default`: Use the default latest system image. For clusters with continuous scaling node provisioning mode, new instance groups inherit the AMI from the earliest existing instance group
If you choose to use a custom AMI (`CustomAmiId`), ensure it meets the following requirements:
+ Encryption: The custom AMI must be unencrypted.
+ Ownership: The custom AMI must be owned by the same AWS account that is creating the HyperPod cluster.
+ Volume support: Only the primary AMI snapshot volume is supported; additional AMI volumes are not supported.
When updating the instance group's AMI through the `UpdateClusterSoftware` operation, if an instance group uses a custom AMI, you must provide an `ImageId` or use the default as input. Note that if you don't specify an instance group in your `UpdateClusterSoftware` request, then all of the instance groups are patched with the specified image.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 21.
Pattern: `ami-[0-9a-fA-F]{8,17}|default`
Required: No

 ** ImageReleaseVersion **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-ImageReleaseVersion"></a>
The version of the HyperPod-managed AMI to use for the instance group. Uses semantic versioning in the format `MAJOR.MINOR.PATCH` (for example, `1.2.3`). If omitted, the latest available version is used.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: No

 ** InstanceRequirements **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-InstanceRequirements"></a>
The instance requirements for the instance group, including the instance types to use. Use this to create a flexible instance group that supports multiple instance types. The `InstanceType` and `InstanceRequirements` properties are mutually exclusive.
Type: [ClusterInstanceRequirements](API_ClusterInstanceRequirements.md) object
Required: No

 ** InstanceStorageConfigs **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-InstanceStorageConfigs"></a>
Specifies the additional storage configurations for the instances in the SageMaker HyperPod cluster instance group.
Type: Array of [ClusterInstanceStorageConfig](API_ClusterInstanceStorageConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

 ** InstanceType **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-InstanceType"></a>
Specifies the instance type of the instance group.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5.4xlarge | ml.p6e-gb200.36xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.c5n.large | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.gr6.4xlarge | ml.gr6.8xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge | ml.trn2.3xlarge | ml.trn2.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.i3en.large | ml.i3en.xlarge | ml.i3en.2xlarge | ml.i3en.3xlarge | ml.i3en.6xlarge | ml.i3en.12xlarge | ml.i3en.24xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.r5d.16xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p6-b300.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.c6g.medium | ml.c6g.large | ml.c6g.xlarge | ml.c6g.2xlarge | ml.c6g.4xlarge | ml.c6g.8xlarge | ml.c6g.12xlarge | ml.c6g.16xlarge | ml.c7g.medium | ml.c7g.large | ml.c7g.xlarge | ml.c7g.2xlarge | ml.c7g.4xlarge | ml.c7g.8xlarge | ml.c7g.12xlarge | ml.c7g.16xlarge | ml.c8g.medium | ml.c8g.large | ml.c8g.xlarge | ml.c8g.2xlarge | ml.c8g.4xlarge | ml.c8g.8xlarge | ml.c8g.12xlarge | ml.c8g.16xlarge | ml.c8g.24xlarge | ml.c8g.48xlarge | ml.c6a.large | ml.c6a.xlarge | ml.c6a.2xlarge | ml.c6a.4xlarge | ml.c6a.8xlarge | ml.c6a.12xlarge | ml.c6a.16xlarge | ml.c6a.24xlarge | ml.c6a.32xlarge | ml.c6a.48xlarge | ml.m6a.large | ml.m6a.xlarge | ml.m6a.2xlarge | ml.m6a.4xlarge | ml.m6a.8xlarge | ml.m6a.12xlarge | ml.m6a.16xlarge | ml.m6a.24xlarge | ml.m6a.32xlarge | ml.m6a.48xlarge | ml.m6g.medium | ml.m6g.large | ml.m6g.xlarge | ml.m6g.2xlarge | ml.m6g.4xlarge | ml.m6g.8xlarge | ml.m6g.12xlarge | ml.m6g.16xlarge | ml.m7g.medium | ml.m7g.large | ml.m7g.xlarge | ml.m7g.2xlarge | ml.m7g.4xlarge | ml.m7g.8xlarge | ml.m7g.12xlarge | ml.m7g.16xlarge | ml.m8g.medium | ml.m8g.large | ml.m8g.xlarge | ml.m8g.2xlarge | ml.m8g.4xlarge | ml.m8g.8xlarge | ml.m8g.12xlarge | ml.m8g.16xlarge | ml.m8g.24xlarge | ml.m8g.48xlarge`
Required: No

 ** KubernetesConfig **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-KubernetesConfig"></a>
Specifies the Kubernetes configuration for the instance group. You describe what you want the labels and taints to look like, and the cluster works to reconcile the actual state with the declared state for nodes in this instance group.
Type: [ClusterKubernetesConfig](API_ClusterKubernetesConfig.md) object
Required: No

 ** LifeCycleConfig **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-LifeCycleConfig"></a>
Specifies the LifeCycle configuration for the instance group.
Type: [ClusterLifeCycleConfig](API_ClusterLifeCycleConfig.md) object
Required: No

 ** MinInstanceCount **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-MinInstanceCount"></a>
Defines the minimum number of instances required for an instance group to become `InService`. If this threshold isn't met within 3 hours, the instance group rolls back to its previous state - zero instances for new instance groups, or previous settings for existing instance groups. `MinInstanceCount` only affects the initial transition to `InService` and does not guarantee maintaining this minimum afterward.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6758.
Required: No

 ** NetworkInterface **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-NetworkInterface"></a>
The network interface configuration for the instance group.
Type: [ClusterNetworkInterface](API_ClusterNetworkInterface.md) object
Required: No

 ** OnStartDeepHealthChecks **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-OnStartDeepHealthChecks"></a>
A flag indicating whether deep health checks should be performed when the cluster instance group is created or updated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `InstanceStress | InstanceConnectivity`
Required: No

 ** OverrideVpcConfig **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-OverrideVpcConfig"></a>
To configure multi-AZ deployments, customize the Amazon VPC configuration at the instance group level. You can specify different subnets and security groups across different AZs in the instance group specification to override a SageMaker HyperPod cluster's default Amazon VPC configuration. For more information about deploying a cluster in multiple AZs, see [Setting up SageMaker HyperPod clusters across multiple AZs](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-multiple-availability-zones).
When your Amazon VPC and subnets support IPv6, network communications differ based on the cluster orchestration platform:
+ Slurm-orchestrated clusters automatically configure nodes with dual IPv6 and IPv4 addresses, allowing immediate IPv6 network communications.
+ In Amazon EKS-orchestrated clusters, nodes receive dual-stack addressing, but pods can only use IPv6 when the Amazon EKS cluster is explicitly IPv6-enabled. For information about deploying an IPv6 Amazon EKS cluster, see [Amazon EKS IPv6 Cluster Deployment](https://docs.aws.amazon.com/eks/latest/userguide/deploy-ipv6-cluster.html#_deploy_an_ipv6_cluster_with_eksctl).
Additional resources for IPv6 configuration:
+ For information about adding IPv6 support to your VPC, see to [IPv6 Support for VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html).
+ For information about creating a new IPv6-compatible VPC, see [Amazon VPC Creation Guide](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).
+ To configure SageMaker HyperPod with a custom Amazon VPC, see [Custom Amazon VPC Setup for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-optional-vpc).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

 ** ScheduledUpdateConfig **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-ScheduledUpdateConfig"></a>
The configuration object of the schedule that SageMaker uses to update the AMI.
Type: [ScheduledUpdateConfig](API_ScheduledUpdateConfig.md) object
Required: No

 ** SlurmConfig **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-SlurmConfig"></a>
Specifies the Slurm configuration for the instance group.
Type: [ClusterSlurmConfig](API_ClusterSlurmConfig.md) object
Required: No

 ** ThreadsPerCore **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-ThreadsPerCore"></a>
Specifies the value for **Threads per core**. For instance types that support multithreading, you can specify `1` for disabling multithreading and `2` for enabling multithreading. For instance types that doesn't support multithreading, specify `1`. For more information, see the reference table of [CPU cores and threads per CPU core per instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html) in the *Amazon Elastic Compute Cloud User Guide*.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: No

 ** TrainingPlanArn **   <a name="sagemaker-Type-ClusterInstanceGroupSpecification-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of the training plan to use for this cluster instance group.
For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

## See Also
<a name="API_ClusterInstanceGroupSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterInstanceGroupSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterInstanceGroupSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterInstanceGroupSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
