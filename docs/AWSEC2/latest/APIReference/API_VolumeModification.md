---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VolumeModification.html
---

# VolumeModification
<a name="API_VolumeModification"></a>

Describes the modification status of an EBS volume.

## Contents
<a name="API_VolumeModification_Contents"></a>

 ** endTime **
The modification completion or failure time.
Type: Timestamp
Required: No

 ** modificationState **
The current modification state.
Type: String
Valid Values: `modifying | optimizing | completed | failed`
Required: No

 ** operator **
The service provider that manages the resource.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** originalIops **
The original IOPS rate of the volume.
Type: Integer
Required: No

 ** originalMultiAttachEnabled **
The original setting for Amazon EBS Multi-Attach.
Type: Boolean
Required: No

 ** originalSize **
The original size of the volume, in GiB.
Type: Integer
Required: No

 ** originalThroughput **
The original throughput of the volume, in MiB/s.
Type: Integer
Required: No

 ** originalVolumeType **
The original EBS volume type of the volume.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

 ** progress **
The modification progress, from 0 to 100 percent complete.
Type: Long
Required: No

 ** startTime **
The modification start time.
Type: Timestamp
Required: No

 ** statusMessage **
A status message about the modification progress or failure.
Type: String
Required: No

 ** targetIops **
The target IOPS rate of the volume.
Type: Integer
Required: No

 ** targetMultiAttachEnabled **
The target setting for Amazon EBS Multi-Attach.
Type: Boolean
Required: No

 ** targetSize **
The target size of the volume, in GiB.
Type: Integer
Required: No

 ** targetThroughput **
The target throughput of the volume, in MiB/s.
Type: Integer
Required: No

 ** targetVolumeType **
The target EBS volume type of the volume.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

 ** volumeId **
The ID of the volume.
Type: String
Required: No

## See Also
<a name="API_VolumeModification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VolumeModification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VolumeModification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VolumeModification)
