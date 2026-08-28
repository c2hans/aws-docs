---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails.html
---

# AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails
<a name="API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails"></a>

Parameters that are used to automatically set up EBS volumes when an instance is launched.

## Contents
<a name="API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails_Contents"></a>

 ** DeleteOnTermination **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails-DeleteOnTermination"></a>
Whether to delete the volume when the instance is terminated.
Type: Boolean
Required: No

 ** Encrypted **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails-Encrypted"></a>
Whether to encrypt the volume.
Type: Boolean
Required: No

 ** Iops **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails-Iops"></a>
The number of input/output (I/O) operations per second (IOPS) to provision for the volume.
Only supported for `gp3` or `io1` volumes. Required for `io1` volumes. Not used with `standard`, `gp2`, `st1`, or `sc1` volumes.
Type: Integer
Required: No

 ** SnapshotId **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails-SnapshotId"></a>
The snapshot ID of the volume to use.
You must specify either `VolumeSize` or `SnapshotId`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VolumeSize **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails-VolumeSize"></a>
The volume size, in GiBs. The following are the supported volumes sizes for each volume type:
+ gp2 and gp3: 1-16,384
+ io1: 4-16,384
+ st1 and sc1: 125-16,384
+ standard: 1-1,024
You must specify either `SnapshotId` or `VolumeSize`. If you specify both `SnapshotId` and `VolumeSize`, the volume size must be equal or greater than the size of the snapshot.
Type: Integer
Required: No

 ** VolumeType **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails-VolumeType"></a>
The volume type. Valid values are as follows:
+  `gp2`
+  `gp3`
+  `io1`
+  `sc1`
+  `st1`
+  `standard`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
