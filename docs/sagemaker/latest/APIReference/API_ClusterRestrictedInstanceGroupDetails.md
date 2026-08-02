---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterRestrictedInstanceGroupDetails.html
---

# ClusterRestrictedInstanceGroupDetails
<a name="API_ClusterRestrictedInstanceGroupDetails"></a>

The instance group details of the restricted instance group (RIG).

## Contents
<a name="API_ClusterRestrictedInstanceGroupDetails_Contents"></a>

 ** CurrentCount **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-CurrentCount"></a>
The number of instances that are currently in the restricted instance group of a SageMaker HyperPod cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** EnvironmentConfig **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-EnvironmentConfig"></a>
The configuration for the restricted instance groups (RIG) environment.
Type: [EnvironmentConfigDetails](API_EnvironmentConfigDetails.md) object
Required: No

 ** ExecutionRole **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-ExecutionRole"></a>
The execution role for the restricted instance group to assume.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** InstanceGroupName **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-InstanceGroupName"></a>
The name of the restricted instance group of a SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** InstanceStorageConfigs **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-InstanceStorageConfigs"></a>
The additional storage configurations for the instances in the SageMaker HyperPod cluster restricted instance group.
Type: Array of [ClusterInstanceStorageConfig](API_ClusterInstanceStorageConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

 ** InstanceType **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-InstanceType"></a>
The instance type of the restricted instance group of a SageMaker HyperPod cluster.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5.4xlarge | ml.p6e-gb200.36xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.c5n.large | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.gr6.4xlarge | ml.gr6.8xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge | ml.trn2.3xlarge | ml.trn2.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.i3en.large | ml.i3en.xlarge | ml.i3en.2xlarge | ml.i3en.3xlarge | ml.i3en.6xlarge | ml.i3en.12xlarge | ml.i3en.24xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.r5d.16xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p6-b300.48xlarge`
Required: No

 ** OnStartDeepHealthChecks **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-OnStartDeepHealthChecks"></a>
A flag indicating whether deep health checks should be performed when the cluster's restricted instance group is created or updated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `InstanceStress | InstanceConnectivity`
Required: No

 ** OverrideVpcConfig **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-OverrideVpcConfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

 ** ScheduledUpdateConfig **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-ScheduledUpdateConfig"></a>
The configuration object of the schedule that SageMaker follows when updating the AMI.
Type: [ScheduledUpdateConfig](API_ScheduledUpdateConfig.md) object
Required: No

 ** Status **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-Status"></a>
The current status of the cluster's restricted instance group.
+  `InService`: The restricted instance group is active and healthy.
+  `Creating`: The restricted instance group is being provisioned.
+  `Updating`: The restricted instance group is being updated.
+  `Failed`: The restricted instance group has failed to provision or is no longer healthy.
+  `Degraded`: The restricted instance group is degraded, meaning that some instances have failed to provision or are no longer healthy.
+  `Deleting`: The restricted instance group is being deleted.
Type: String
Valid Values: `InService | Creating | Updating | Failed | Degraded | SystemUpdating | Deleting`
Required: No

 ** TargetCount **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-TargetCount"></a>
The number of instances you specified to add to the restricted instance group of a SageMaker HyperPod cluster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6758.
Required: No

 ** ThreadsPerCore **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-ThreadsPerCore"></a>
The number you specified to `TreadsPerCore` in `CreateCluster` for enabling or disabling multithreading. For instance types that support multithreading, you can specify 1 for disabling multithreading and 2 for enabling multithreading. For more information, see the reference table of [CPU cores and threads per CPU core per instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html) in the *Amazon Elastic Compute Cloud User Guide*.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: No

 ** TrainingPlanArn **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-TrainingPlanArn"></a>
The Amazon Resource Name (ARN) of the training plan to filter clusters by. For more information about reserving GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

 ** TrainingPlanStatus **   <a name="sagemaker-Type-ClusterRestrictedInstanceGroupDetails-TrainingPlanStatus"></a>
The current status of the training plan associated with this cluster restricted instance group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

## See Also
<a name="API_ClusterRestrictedInstanceGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterRestrictedInstanceGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterRestrictedInstanceGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterRestrictedInstanceGroupDetails)
