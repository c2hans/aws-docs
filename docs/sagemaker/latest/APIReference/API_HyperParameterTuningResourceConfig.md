---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningResourceConfig.html
---

# HyperParameterTuningResourceConfig
<a name="API_HyperParameterTuningResourceConfig"></a>

The configuration of resources, including compute instances and storage volumes for use in training jobs launched by hyperparameter tuning jobs. `HyperParameterTuningResourceConfig` is similar to `ResourceConfig`, but has the additional `InstanceConfigs` and `AllocationStrategy` fields to allow for flexible instance management. Specify one or more instance types, count, and the allocation strategy for instance selection.

**Note**
 `HyperParameterTuningResourceConfig` supports the capabilities of `ResourceConfig` with the exception of `KeepAlivePeriodInSeconds`. Hyperparameter tuning jobs use warm pools by default, which reuse clusters between training jobs.

## Contents
<a name="API_HyperParameterTuningResourceConfig_Contents"></a>

 ** AllocationStrategy **   <a name="sagemaker-Type-HyperParameterTuningResourceConfig-AllocationStrategy"></a>
The strategy that determines the order of preference for resources specified in `InstanceConfigs` used in hyperparameter optimization.
Type: String
Valid Values: `Prioritized`
Required: No

 ** InstanceConfigs **   <a name="sagemaker-Type-HyperParameterTuningResourceConfig-InstanceConfigs"></a>
A list containing the configuration(s) for one or more resources for processing hyperparameter jobs. These resources include compute instances and storage volumes to use in model training jobs launched by hyperparameter tuning jobs. The `AllocationStrategy` controls the order in which multiple configurations provided in `InstanceConfigs` are used.
If you only want to use a single instance configuration inside the `HyperParameterTuningResourceConfig` API, do not provide a value for `InstanceConfigs`. Instead, use `InstanceType`, `VolumeSizeInGB` and `InstanceCount`. If you use `InstanceConfigs`, do not provide values for `InstanceType`, `VolumeSizeInGB` or `InstanceCount`.
Type: Array of [HyperParameterTuningInstanceConfig](API_HyperParameterTuningInstanceConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Required: No

 ** InstanceCount **   <a name="sagemaker-Type-HyperParameterTuningResourceConfig-InstanceCount"></a>
The number of compute instances of type `InstanceType` to use. For [distributed training](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html), select a value greater than 1.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** InstanceType **   <a name="sagemaker-Type-HyperParameterTuningResourceConfig-InstanceType"></a>
The instance type used to run hyperparameter optimization tuning jobs. See [ descriptions of instance types](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) for more information.
Type: String
Valid Values: `ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5n.xlarge | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.trn2.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.8xlarge | ml.c6i.4xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.r5d.large | ml.r5d.xlarge | ml.r5d.2xlarge | ml.r5d.4xlarge | ml.r5d.8xlarge | ml.r5d.12xlarge | ml.r5d.16xlarge | ml.r5d.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.p6-b200.48xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge`
Required: No

 ** VolumeKmsKeyId **   <a name="sagemaker-Type-HyperParameterTuningResourceConfig-VolumeKmsKeyId"></a>
A key used by AWS Key Management Service to encrypt data on the storage volume attached to the compute instances used to run the training job. You can use either of the following formats to specify a key.
KMS Key ID:
 `"1234abcd-12ab-34cd-56ef-1234567890ab"`
Amazon Resource Name (ARN) of a KMS key:
 `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
Some instances use local storage, which use a [hardware module to encrypt](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) storage volumes. If you choose one of these instance types, you cannot request a `VolumeKmsKeyId`. For a list of instance types that use local storage, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/). For more information about AWS Key Management Service, see [KMS encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-kms-permissions.html) for more information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** VolumeSizeInGB **   <a name="sagemaker-Type-HyperParameterTuningResourceConfig-VolumeSizeInGB"></a>
The volume size in GB for the storage volume to be used in processing hyperparameter optimization jobs (optional). These volumes store model artifacts, incremental states and optionally, scratch space for training algorithms. Do not provide a value for this parameter if a value for `InstanceConfigs` is also specified.
Some instance types have a fixed total local storage size. If you select one of these instances for training, `VolumeSizeInGB` cannot be greater than this total size. For a list of instance types with local instance storage and their sizes, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/).
SageMaker supports only the [General Purpose SSD (gp2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) storage volume type.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_HyperParameterTuningResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HyperParameterTuningResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HyperParameterTuningResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HyperParameterTuningResourceConfig)
