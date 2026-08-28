---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html
---

# TaskManagedEBSVolumeConfiguration
<a name="API_TaskManagedEBSVolumeConfiguration"></a>

The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task.

## Contents
<a name="API_TaskManagedEBSVolumeConfiguration_Contents"></a>

 ** roleArn **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-roleArn"></a>
The ARN of the IAM role to associate with this volume. This is the Amazon ECS infrastructure IAM role that is used to manage your AWS infrastructure. We recommend using the Amazon ECS-managed `AmazonECSInfrastructureRolePolicyForVolumes` IAM policy with this role. For more information, see [Amazon ECS infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html) in the *Amazon ECS Developer Guide*.
Type: String
Required: Yes

 ** encrypted **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-encrypted"></a>
Indicates whether the volume should be encrypted. If you turn on Region-level Amazon EBS encryption by default but set this value as `false`, the setting is overridden and the volume is encrypted with the KMS key specified for Amazon EBS encryption by default. This parameter maps 1:1 with the `Encrypted` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference*.
Type: Boolean
Required: No

 ** filesystemType **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-filesystemType"></a>
The Linux filesystem type for the volume. For volumes created from a snapshot, you must specify the same filesystem type that the volume was using when the snapshot was created. If there is a filesystem type mismatch, the task will fail to start.
The available filesystem types are `ext3`, `ext4`, and `xfs`. If no value is specified, the `xfs` filesystem type is used by default.
Type: String
Valid Values: `ext3 | ext4 | xfs | ntfs`
Required: No

 ** iops **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-iops"></a>
The number of I/O operations per second (IOPS). For `gp3`, `io1`, and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
The following are the supported values for each volume type.
+  `gp3`: 3,000 - 16,000 IOPS
+  `io1`: 100 - 64,000 IOPS
+  `io2`: 100 - 256,000 IOPS
This parameter is required for `io1` and `io2` volume types. The default for `gp3` volumes is `3,000 IOPS`. This parameter is not supported for `st1`, `sc1`, or `standard` volume types.
This parameter maps 1:1 with the `Iops` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference*.
Type: Integer
Required: No

 ** kmsKeyId **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-kmsKeyId"></a>
The Amazon Resource Name (ARN) identifier of the AWS Key Management Service key to use for Amazon EBS encryption. When a key is specified using this parameter, it overrides Amazon EBS default encryption or any KMS key that you specified for cluster-level managed storage encryption. This parameter maps 1:1 with the `KmsKeyId` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference*. For more information about encrypting Amazon EBS volumes attached to a task, see [Encrypt data stored in Amazon EBS volumes attached to Amazon ECS tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html).
 AWS authenticates the AWS Key Management Service key asynchronously. Therefore, if you specify an ID, alias, or ARN that is invalid, the action can appear to complete, but eventually fails.
Type: String
Required: No

 ** sizeInGiB **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-sizeInGiB"></a>
The size of the volume in GiB. You must specify either a volume size or a snapshot ID. If you specify a snapshot ID, the snapshot size is used for the volume size by default. You can optionally specify a volume size greater than or equal to the snapshot size. This parameter maps 1:1 with the `Size` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference*.
The following are the supported volume size values for each volume type.
+  `gp2` and `gp3`: 1-16,384
+  `io1` and `io2`: 4-16,384
+  `st1` and `sc1`: 125-16,384
+  `standard`: 1-1,024
Type: Integer
Required: No

 ** snapshotId **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-snapshotId"></a>
The snapshot that Amazon ECS uses to create the volume. You must specify either a snapshot ID or a volume size. This parameter maps 1:1 with the `SnapshotId` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference*.
Type: String
Required: No

 ** tagSpecifications **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-tagSpecifications"></a>
The tags to apply to the volume. Amazon ECS applies service-managed tags by default. This parameter maps 1:1 with the `TagSpecifications.N` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference*.
Type: Array of [EBSTagSpecification](API_EBSTagSpecification.md) objects
Required: No

 ** terminationPolicy **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-terminationPolicy"></a>
The termination policy for the volume when the task exits. This provides a way to control whether Amazon ECS terminates the Amazon EBS volume when the task stops.
Type: [TaskManagedEBSVolumeTerminationPolicy](API_TaskManagedEBSVolumeTerminationPolicy.md) object
Required: No

 ** throughput **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-throughput"></a>
The throughput to provision for a volume, in MiB/s, with a maximum of 1,000 MiB/s. This parameter maps 1:1 with the `Throughput` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference*.
This parameter is only supported for the `gp3` volume type.
Type: Integer
Required: No

 ** volumeInitializationRate **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-volumeInitializationRate"></a>
The rate, in MiB/s, at which data is fetched from a snapshot of an existing Amazon EBS volume to create a new volume for attachment to the task. This property can be specified only if you specify a `snapshotId`. For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the *Amazon EBS User Guide*.
Type: Integer
Required: No

 ** volumeType **   <a name="ECS-Type-TaskManagedEBSVolumeConfiguration-volumeType"></a>
The volume type. This parameter maps 1:1 with the `VolumeType` parameter of the [CreateVolume API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) in the *Amazon EC2 API Reference*. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) in the *Amazon EC2 User Guide*.
The following are the supported volume types.
+ General Purpose SSD: `gp2`\|`gp3`
+ Provisioned IOPS SSD: `io1`\|`io2`
+ Throughput Optimized HDD: `st1`
+ Cold HDD: `sc1`
+ Magnetic: `standard`
**Note**
The magnetic volume type is not supported on Fargate.
Type: String
Required: No

## See Also
<a name="API_TaskManagedEBSVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TaskManagedEBSVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TaskManagedEBSVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TaskManagedEBSVolumeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
