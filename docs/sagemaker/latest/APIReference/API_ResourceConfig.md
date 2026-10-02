---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceConfig.html
---

# ResourceConfig
<a name="API_ResourceConfig"></a>

Describes the resources, including machine learning (ML) compute instances and ML storage volumes, to use for model training.

## Contents
<a name="API_ResourceConfig_Contents"></a>

 ** InstanceCount **   <a name="sagemaker-Type-ResourceConfig-InstanceCount"></a>
The number of ML compute instances to use. For distributed training, provide a value greater than 1.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** InstanceGroups **   <a name="sagemaker-Type-ResourceConfig-InstanceGroups"></a>
The configuration of a heterogeneous cluster in JSON format.
Type: Array of [InstanceGroup](API_InstanceGroup.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** InstancePlacementConfig **   <a name="sagemaker-Type-ResourceConfig-InstancePlacementConfig"></a>
Configuration for how training job instances are placed and allocated within UltraServers. Only applicable for UltraServer capacity.
Type: [InstancePlacementConfig](API_InstancePlacementConfig.md) object
Required: No

 ** InstancePreferences **   <a name="sagemaker-Type-ResourceConfig-InstancePreferences"></a>
An ordered list of ML compute instance types for the training job, in priority order. SageMaker launches the training job on the first instance type in the list that has available capacity. If capacity is insufficient, SageMaker evaluates the next instance type in the preferred list. Exactly one instance type is selected for the job.
 `InstancePreferences` is mutually exclusive with `InstanceType`, `InstanceGroups`, `InstancePlacementConfig`, and `EnableManagedSpotTraining`, and supports only Flexible Training Plans (FTP) and On-Demand capacity.
Type: Array of [InstancePreference](API_InstancePreference.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** InstanceType **   <a name="sagemaker-Type-ResourceConfig-InstanceType"></a>
The ML compute instance type.
Type: String
Valid Values: `ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5n.xlarge | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.trn2.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.8xlarge | ml.c6i.4xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.r5d.large | ml.r5d.xlarge | ml.r5d.2xlarge | ml.r5d.4xlarge | ml.r5d.8xlarge | ml.r5d.12xlarge | ml.r5d.16xlarge | ml.r5d.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.p6-b200.48xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.m8i.large | ml.m8i.xlarge | ml.m8i.2xlarge | ml.m8i.4xlarge | ml.m8i.8xlarge | ml.m8i.12xlarge | ml.m8i.16xlarge | ml.m8i.24xlarge | ml.m8i.32xlarge | ml.m8i.48xlarge | ml.m8i.96xlarge | ml.c8i.xlarge | ml.c8i.2xlarge | ml.c8i.4xlarge | ml.c8i.8xlarge | ml.c8i.12xlarge | ml.c8i.16xlarge | ml.c8i.24xlarge | ml.c8i.32xlarge | ml.c8i.48xlarge | ml.c8i.96xlarge | ml.r8i.large | ml.r8i.xlarge | ml.r8i.2xlarge | ml.r8i.4xlarge | ml.r8i.8xlarge | ml.r8i.12xlarge | ml.r8i.16xlarge | ml.r8i.24xlarge | ml.r8i.32xlarge | ml.r8i.48xlarge | ml.r8i.96xlarge | ml.m7i-flex.large | ml.m7i-flex.xlarge | ml.m7i-flex.2xlarge | ml.m7i-flex.4xlarge | ml.m7i-flex.8xlarge | ml.m7i-flex.12xlarge | ml.m7i-flex.16xlarge | ml.c7i-flex.xlarge | ml.c7i-flex.2xlarge | ml.c7i-flex.4xlarge | ml.c7i-flex.8xlarge | ml.c7i-flex.12xlarge | ml.c7i-flex.16xlarge | ml.m8i-flex.large | ml.m8i-flex.xlarge | ml.m8i-flex.2xlarge | ml.m8i-flex.4xlarge | ml.m8i-flex.8xlarge | ml.m8i-flex.12xlarge | ml.m8i-flex.16xlarge | ml.c8i-flex.xlarge | ml.c8i-flex.2xlarge | ml.c8i-flex.4xlarge | ml.c8i-flex.8xlarge | ml.c8i-flex.12xlarge | ml.c8i-flex.16xlarge | ml.r8i-flex.large | ml.r8i-flex.xlarge | ml.r8i-flex.2xlarge | ml.r8i-flex.4xlarge | ml.r8i-flex.8xlarge | ml.r8i-flex.12xlarge | ml.r8i-flex.16xlarge`
Required: No

 ** KeepAlivePeriodInSeconds **   <a name="sagemaker-Type-ResourceConfig-KeepAlivePeriodInSeconds"></a>
The duration of time in seconds to retain configured resources in a warm pool for subsequent training jobs.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 21600.
Required: No

 ** SelectedInstanceCount **   <a name="sagemaker-Type-ResourceConfig-SelectedInstanceCount"></a>
The number of instances of `SelectedInstanceType` that the training job launched with. The job is billed for this instance type and count. Returned by `DescribeTrainingJob` after an instance type is selected. This field is read-only and isn't accepted in `CreateTrainingJob` requests.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** SelectedInstanceType **   <a name="sagemaker-Type-ResourceConfig-SelectedInstanceType"></a>
The instance type that SageMaker selected for the job from the provided `InstancePreferences`. The job is billed for this instance type and count. Returned by ` [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html) ` after an instance type is selected. This field is read-only and isn't accepted in `CreateTrainingJob` requests.
Type: String
Valid Values: `ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5n.xlarge | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.trn2.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.8xlarge | ml.c6i.4xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.r5d.large | ml.r5d.xlarge | ml.r5d.2xlarge | ml.r5d.4xlarge | ml.r5d.8xlarge | ml.r5d.12xlarge | ml.r5d.16xlarge | ml.r5d.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.p6-b200.48xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.m8i.large | ml.m8i.xlarge | ml.m8i.2xlarge | ml.m8i.4xlarge | ml.m8i.8xlarge | ml.m8i.12xlarge | ml.m8i.16xlarge | ml.m8i.24xlarge | ml.m8i.32xlarge | ml.m8i.48xlarge | ml.m8i.96xlarge | ml.c8i.xlarge | ml.c8i.2xlarge | ml.c8i.4xlarge | ml.c8i.8xlarge | ml.c8i.12xlarge | ml.c8i.16xlarge | ml.c8i.24xlarge | ml.c8i.32xlarge | ml.c8i.48xlarge | ml.c8i.96xlarge | ml.r8i.large | ml.r8i.xlarge | ml.r8i.2xlarge | ml.r8i.4xlarge | ml.r8i.8xlarge | ml.r8i.12xlarge | ml.r8i.16xlarge | ml.r8i.24xlarge | ml.r8i.32xlarge | ml.r8i.48xlarge | ml.r8i.96xlarge | ml.m7i-flex.large | ml.m7i-flex.xlarge | ml.m7i-flex.2xlarge | ml.m7i-flex.4xlarge | ml.m7i-flex.8xlarge | ml.m7i-flex.12xlarge | ml.m7i-flex.16xlarge | ml.c7i-flex.xlarge | ml.c7i-flex.2xlarge | ml.c7i-flex.4xlarge | ml.c7i-flex.8xlarge | ml.c7i-flex.12xlarge | ml.c7i-flex.16xlarge | ml.m8i-flex.large | ml.m8i-flex.xlarge | ml.m8i-flex.2xlarge | ml.m8i-flex.4xlarge | ml.m8i-flex.8xlarge | ml.m8i-flex.12xlarge | ml.m8i-flex.16xlarge | ml.c8i-flex.xlarge | ml.c8i-flex.2xlarge | ml.c8i-flex.4xlarge | ml.c8i-flex.8xlarge | ml.c8i-flex.12xlarge | ml.c8i-flex.16xlarge | ml.r8i-flex.large | ml.r8i-flex.xlarge | ml.r8i-flex.2xlarge | ml.r8i-flex.4xlarge | ml.r8i-flex.8xlarge | ml.r8i-flex.12xlarge | ml.r8i-flex.16xlarge`
Required: No

 ** TrainingPlanArn **   <a name="sagemaker-Type-ResourceConfig-TrainingPlanArn"></a>
The Amazon Resource Name (ARN); of the training plan to use for this resource configuration.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

 ** VolumeKmsKeyId **   <a name="sagemaker-Type-ResourceConfig-VolumeKmsKeyId"></a>
The AWS KMS key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.
Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You can't request a `VolumeKmsKeyId` when using an instance type with local storage.
For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes).
For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html).
The `VolumeKmsKeyId` can be in any of the following formats:
+ // KMS Key ID

   `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // Amazon Resource Name (ARN) of a KMS Key

   `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** VolumeSizeInGB **   <a name="sagemaker-Type-ResourceConfig-VolumeSizeInGB"></a>
The size of the ML storage volume that you want to provision.
SageMaker automatically selects the volume size for serverless training jobs. You cannot customize this setting.
ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose `File` as the `TrainingInputMode` in the algorithm specification.
When using an ML instance with [NVMe SSD volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#nvme-ssd-volumes), SageMaker doesn't provision Amazon EBS General Purpose SSD (gp2) storage. Available storage is fixed to the NVMe-type instance's storage capacity. SageMaker configures storage paths for training datasets, checkpoints, model artifacts, and outputs to use the entire capacity of the instance storage. For example, ML instance families with the NVMe-type instance storage include `ml.p4d`, `ml.g4dn`, and `ml.g5`.
When using an ML instance with the EBS-only storage option and without instance storage, you must define the size of EBS volume through `VolumeSizeInGB` in the `ResourceConfig` API. For example, ML instance families that use EBS volumes include `ml.c5` and `ml.p2`.
To look up instance types and their instance storage types and volumes, see [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/).
To find the default local paths defined by the SageMaker training platform, see [Amazon SageMaker Training Storage Folders for Training Datasets, Checkpoints, Model Artifacts, and Outputs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html).
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ResourceConfig)
