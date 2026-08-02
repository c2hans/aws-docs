---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VolumeRecycleBinInfo.html
---

# VolumeRecycleBinInfo
<a name="API_VolumeRecycleBinInfo"></a>

Information about a volume that is currently in the Recycle Bin.

## Contents
<a name="API_VolumeRecycleBinInfo_Contents"></a>

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

 ** iops **
The number of I/O operations per second (IOPS) for the volume.
Type: Integer
Required: No

 ** operator **
The service provider that manages the volume.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** outpostArn **
The ARN of the Outpost on which the volume is stored. For more information, see [Amazon EBS volumes on Outposts](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-outposts.html) in the *Amazon EBS User Guide*.
Type: String
Required: No

 ** recycleBinEnterTime **
The date and time when the volume entered the Recycle Bin.
Type: Timestamp
Required: No

 ** recycleBinExitTime **
The date and time when the volume is to be permanently deleted from the Recycle Bin.
Type: Timestamp
Required: No

 ** size **
The size of the volume, in GiB.
Type: Integer
Required: No

 ** snapshotId **
The snapshot from which the volume was created, if applicable.
Type: String
Required: No

 ** sourceVolumeId **
The ID of the source volume.
Type: String
Required: No

 ** state **
The state of the volume.
Type: String
Valid Values: `creating | available | in-use | deleting | deleted | error`
Required: No

 ** throughput **
The throughput that the volume supports, in MiB/s.
Type: Integer
Required: No

 ** volumeId **
The ID of the volume.
Type: String
Required: No

 ** volumeType **
The volume type.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## See Also
<a name="API_VolumeRecycleBinInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VolumeRecycleBinInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VolumeRecycleBinInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VolumeRecycleBinInfo)
