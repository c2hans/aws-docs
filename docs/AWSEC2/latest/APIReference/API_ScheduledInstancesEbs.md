---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ScheduledInstancesEbs.html
---

# ScheduledInstancesEbs
<a name="API_ScheduledInstancesEbs"></a>

Describes an EBS volume for a Scheduled Instance.

## Contents
<a name="API_ScheduledInstancesEbs_Contents"></a>

 ** DeleteOnTermination **
Indicates whether the volume is deleted on instance termination.
Type: Boolean
Required: No

 ** Encrypted **
Indicates whether the volume is encrypted. You can attached encrypted volumes only to instances that support them.
Type: Boolean
Required: No

 ** Iops **
The number of I/O operations per second (IOPS) to provision for a `gp3`, `io1`, or `io2` volume.
Type: Integer
Required: No

 ** SnapshotId **
The ID of the snapshot.
Type: String
Required: No

 ** VolumeSize **
The size of the volume, in GiB.
Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.
Type: Integer
Required: No

 ** VolumeType **
The volume type.
Default: `gp2`
Type: String
Required: No

## See Also
<a name="API_ScheduledInstancesEbs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ScheduledInstancesEbs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ScheduledInstancesEbs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ScheduledInstancesEbs)
