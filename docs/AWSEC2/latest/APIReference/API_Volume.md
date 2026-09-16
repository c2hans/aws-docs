---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Volume.html
---

# Volume
<a name="API_Volume"></a>

Describes a volume.

## Contents
<a name="API_Volume_Contents"></a>

 ** AttachmentSet.N **
This parameter is not returned by CreateVolume.
Information about the volume attachments.
Type: Array of [VolumeAttachment](API_VolumeAttachment.md) objects
Required: No

 ** availabilityZone **
The Availability Zone for the volume.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone for the volume.
Type: String
Required: No

 ** createTime **
The time stamp when volume creation was initiated.
Type: Timestamp
Required: No

 ** encrypted **
Indicates whether the volume is encrypted.
Type: Boolean
Required: No

 ** fastRestored **
This parameter is not returned by CreateVolume.
Indicates whether the volume was created using fast snapshot restore.
Type: Boolean
Required: No

 ** iops **
The number of I/O operations per second (IOPS). For `gp3`, `io1`, and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
Type: Integer
Required: No

 ** kmsKeyId **
The Amazon Resource Name (ARN) of the AWS KMS key that was used to protect the volume encryption key for the volume.
Type: String
Required: No

 ** multiAttachEnabled **
Indicates whether Amazon EBS Multi-Attach is enabled.
Type: Boolean
Required: No

 ** operator **
The service provider that manages the volume.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** outpostArn **
The Amazon Resource Name (ARN) of the Outpost.
Type: String
Required: No

 ** ownerId **
The ID of the Amazon Web Services account that owns the volume.
Type: String
Required: No

 ** size **
The size of the volume, in GiBs.
Type: Integer
Required: No

 ** snapshotId **
The snapshot from which the volume was created, if applicable.
Type: String
Required: No

 ** sourceVolumeId **
The ID of the source volume from which the volume copy was created. Only for volume copies.
Type: String
Required: No

 ** sseType **
This parameter is not returned by CreateVolume.
Reserved for future use.
Type: String
Valid Values: `sse-ebs | sse-kms | none`
Required: No

 ** status **
The volume state.
Type: String
Valid Values: `creating | available | in-use | deleting | deleted | error`
Required: No

 ** TagSet.N **
Any tags assigned to the volume.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** throughput **
The throughput that the volume supports, in MiB/s.
Type: Integer
Required: No

 ** volumeArn **
The Amazon Resource Name (ARN) of the volume.
Type: String
Required: No

 ** volumeId **
The ID of the volume.
Type: String
Required: No

 ** volumeInitializationRate **
The Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) specified for the volume during creation, in MiB/s. If no volume initialization rate was specified, the value is `null`.
Type: Integer
Required: No

 ** volumeType **
The volume type.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## See Also
<a name="API_Volume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Volume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Volume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Volume)
