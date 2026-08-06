---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceGroupDetails.html
---

# ClusterInstanceGroupDetails
<a name="API_ClusterInstanceGroupDetails"></a>

Details of an instance group in a SageMaker HyperPod cluster.

## Contents
<a name="API_ClusterInstanceGroupDetails_Contents"></a>

 ** ActiveOperations **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-ActiveOperations"></a>
A map indicating active operations currently in progress for the instance group of a SageMaker HyperPod cluster. When there is a scaling operation in progress, this map contains a key `Scaling` with value 1.
Type: String to integer map
Valid Keys: `Scaling`
Valid Range: Minimum value of 1.
Required: No

 ** ActiveSoftwareUpdateConfig **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-ActiveSoftwareUpdateConfig"></a>
The configuration to use when updating the AMI versions.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** AutoPatchConfig **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-AutoPatchConfig"></a>
The auto-patching configuration for the instance group, including the current patching strategy and next scheduled patch date.
Type: [ClusterAutoPatchConfigDetails](API_ClusterAutoPatchConfigDetails.md) object
Required: No

 ** CapacityRequirements **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-CapacityRequirements"></a>
The instance capacity requirements for the instance group.
Type: [ClusterCapacityRequirements](API_ClusterCapacityRequirements.md) object
Required: No

 ** CurrentCount **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-CurrentCount"></a>
The number of instances that are currently in the instance group of a SageMaker HyperPod cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** CurrentImageId **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-CurrentImageId"></a>
The ID of the Amazon Machine Image (AMI) currently in use by the instance group.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 21.
Pattern: `ami-[0-9a-fA-F]{8,17}|default`
Required: No

 ** CurrentImageReleaseVersion **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-CurrentImageReleaseVersion"></a>
The version of the HyperPod-managed AMI currently running on the instance group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: No

 ** DesiredImageId **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-DesiredImageId"></a>
The ID of the Amazon Machine Image (AMI) desired for the instance group.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 21.
Pattern: `ami-[0-9a-fA-F]{8,17}|default`
Required: No

 ** DesiredImageReleaseVersion **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-DesiredImageReleaseVersion"></a>
The desired version of the HyperPod-managed AMI for the instance group. This may differ from the current version when an update is pending.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[0-9]+\.[0-9]+\.[0-9]+`
Required: No

 ** ExecutionRole **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-ExecutionRole"></a>
The execution role for the instance group to assume.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** ImageVersionStatus **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-ImageVersionStatus"></a>
The status of the image version for the instance group. Indicates whether the instance group is running the latest image version or if an update is available.
Type: String
Valid Values: `UpToDate | UpdateAvailable | SecurityUpdateRequired | EndOfLife`
Required: No

 ** InstanceGroupName **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-InstanceGroupName"></a>
The name of the instance group of a SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** InstanceRequirements **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-InstanceRequirements"></a>
The instance requirements for the instance group, including the current and desired instance types. This field is present for flexible instance groups that support multiple instance types.
Type: [ClusterInstanceRequirementDetails](API_ClusterInstanceRequirementDetails.md) object
Required: No

 ** InstanceStorageConfigs **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-InstanceStorageConfigs"></a>
The additional storage configurations for the instances in the SageMaker HyperPod cluster instance group.
Type: Array of [ClusterInstanceStorageConfig](API_ClusterInstanceStorageConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

 ** InstanceType **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-InstanceType"></a>
The instance type of the instance group of a SageMaker HyperPod cluster.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5.4xlarge | ml.p6e-gb200.36xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.c5n.large | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.gr6.4xlarge | ml.gr6.8xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge | ml.trn2.3xlarge | ml.trn2.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.i3en.large | ml.i3en.xlarge | ml.i3en.2xlarge | ml.i3en.3xlarge | ml.i3en.6xlarge | ml.i3en.12xlarge | ml.i3en.24xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.r5d.16xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p6-b300.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.c6g.medium | ml.c6g.large | ml.c6g.xlarge | ml.c6g.2xlarge | ml.c6g.4xlarge | ml.c6g.8xlarge | ml.c6g.12xlarge | ml.c6g.16xlarge | ml.c7g.medium | ml.c7g.large | ml.c7g.xlarge | ml.c7g.2xlarge | ml.c7g.4xlarge | ml.c7g.8xlarge | ml.c7g.12xlarge | ml.c7g.16xlarge | ml.c8g.medium | ml.c8g.large | ml.c8g.xlarge | ml.c8g.2xlarge | ml.c8g.4xlarge | ml.c8g.8xlarge | ml.c8g.12xlarge | ml.c8g.16xlarge | ml.c8g.24xlarge | ml.c8g.48xlarge | ml.c6a.large | ml.c6a.xlarge | ml.c6a.2xlarge | ml.c6a.4xlarge | ml.c6a.8xlarge | ml.c6a.12xlarge | ml.c6a.16xlarge | ml.c6a.24xlarge | ml.c6a.32xlarge | ml.c6a.48xlarge | ml.m6a.large | ml.m6a.xlarge | ml.m6a.2xlarge | ml.m6a.4xlarge | ml.m6a.8xlarge | ml.m6a.12xlarge | ml.m6a.16xlarge | ml.m6a.24xlarge | ml.m6a.32xlarge | ml.m6a.48xlarge | ml.m6g.medium | ml.m6g.large | ml.m6g.xlarge | ml.m6g.2xlarge | ml.m6g.4xlarge | ml.m6g.8xlarge | ml.m6g.12xlarge | ml.m6g.16xlarge | ml.m7g.medium | ml.m7g.large | ml.m7g.xlarge | ml.m7g.2xlarge | ml.m7g.4xlarge | ml.m7g.8xlarge | ml.m7g.12xlarge | ml.m7g.16xlarge | ml.m8g.medium | ml.m8g.large | ml.m8g.xlarge | ml.m8g.2xlarge | ml.m8g.4xlarge | ml.m8g.8xlarge | ml.m8g.12xlarge | ml.m8g.16xlarge | ml.m8g.24xlarge | ml.m8g.48xlarge`
Required: No

 ** InstanceTypeDetails **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-InstanceTypeDetails"></a>
Details about the instance types in the instance group, including the count and configuration of each instance type. This field is present for flexible instance groups that support multiple instance types.
Type: Array of [ClusterInstanceTypeDetail](API_ClusterInstanceTypeDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** KubernetesConfig **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-KubernetesConfig"></a>
The Kubernetes configuration for the instance group that contains labels and taints to be applied for the nodes in this instance group.
Type: [ClusterKubernetesConfigDetails](API_ClusterKubernetesConfigDetails.md) object
Required: No

 ** LifeCycleConfig **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-LifeCycleConfig"></a>
Details of LifeCycle configuration for the instance group.
Type: [ClusterLifeCycleConfig](API_ClusterLifeCycleConfig.md) object
Required: No

 ** MinCount **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-MinCount"></a>
The minimum number of instances that must be available in the instance group of a SageMaker HyperPod cluster before it transitions to `InService` status.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6758.
Required: No

 ** NetworkInterface **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-NetworkInterface"></a>
The network interface configuration for the instance group.
Type: [ClusterNetworkInterfaceDetails](API_ClusterNetworkInterfaceDetails.md) object
Required: No

 ** OnStartDeepHealthChecks **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-OnStartDeepHealthChecks"></a>
A flag indicating whether deep health checks should be performed when the cluster instance group is created or updated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `InstanceStress | InstanceConnectivity`
Required: No

 ** OverrideVpcConfig **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-OverrideVpcConfig"></a>
The customized Amazon VPC configuration at the instance group level that overrides the default Amazon VPC configuration of the SageMaker HyperPod cluster.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

 ** ScheduledUpdateConfig **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-ScheduledUpdateConfig"></a>
The configuration object of the schedule that SageMaker follows when updating the AMI.
Type: [ScheduledUpdateConfig](API_ScheduledUpdateConfig.md) object
Required: No

 ** SlurmConfig **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-SlurmConfig"></a>
The Slurm configuration for the instance group.
Type: [ClusterSlurmConfigDetails](API_ClusterSlurmConfigDetails.md) object
Required: No

 ** SoftwareUpdateStatus **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-SoftwareUpdateStatus"></a>
Status of the last software udpate request.
Status transitions follow these possible sequences:
+ Pending -> InProgress -> Succeeded
+ Pending -> InProgress -> RollbackInProgress -> RollbackComplete
+ Pending -> InProgress -> RollbackInProgress -> Failed
Type: String
Valid Values: `Pending | InProgress | Succeeded | Failed | RollbackInProgress | RollbackComplete`
Required: No

 ** Status **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-Status"></a>
The current status of the cluster instance group.
+  `InService`: The instance group is active and healthy.
+  `Creating`: The instance group is being provisioned.
+  `Updating`: The instance group is being updated.
+  `Failed`: The instance group has failed to provision or is no longer healthy.
+  `Degraded`: The instance group is degraded, meaning that some instances have failed to provision or are no longer healthy.
+  `Deleting`: The instance group is being deleted.
Type: String
Valid Values: `InService | Creating | Updating | Failed | Degraded | SystemUpdating | Deleting`
Required: No

 ** TargetCount **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-TargetCount"></a>
The number of instances you specified to add to the instance group of a SageMaker HyperPod cluster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6758.
Required: No

 ** TargetStateCount **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-TargetStateCount"></a>
Represents the number of running nodes using the desired Image ID.

1.  **During software update operations:** This count shows the number of nodes running on the desired Image ID. If a rollback occurs, the current image ID and desired image ID (both included in the describe cluster response) swap values. The TargetStateCount then shows the number of nodes running on the newly designated desired image ID (which was previously the current image ID).

1.  **During simultaneous scaling and software update operations:** This count shows the number of instances running on the desired image ID, including any new instances created as part of the scaling request. New nodes are always created using the desired image ID, so TargetStateCount reflects the total count of nodes running on the desired image ID, even during rollback scenarios.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6758.
Required: No

 ** ThreadsPerCore **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-ThreadsPerCore"></a>
The number you specified to `TreadsPerCore` in `CreateCluster` for enabling or disabling multithreading. For instance types that support multithreading, you can specify 1 for disabling multithreading and 2 for enabling multithreading. For more information, see the reference table of [CPU cores and threads per CPU core per instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html) in the *Amazon Elastic Compute Cloud User Guide*.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: No

 ** TrainingPlanArn **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of the training plan associated with this cluster instance group.
For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

 ** TrainingPlanStatus **   <a name="sagemaker-Type-ClusterInstanceGroupDetails-TrainingPlanStatus"></a>
The current status of the training plan associated with this cluster instance group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

## See Also
<a name="API_ClusterInstanceGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterInstanceGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterInstanceGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterInstanceGroupDetails)
