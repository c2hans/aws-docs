---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails.html
---

# AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails
<a name="API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails"></a>

A block device for the instance.

## Contents
<a name="API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails_Contents"></a>

 ** DeviceName **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails-DeviceName"></a>
The device name that is exposed to the EC2 instance. For example, `/dev/sdh` or `xvdh`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Ebs **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails-Ebs"></a>
Parameters that are used to automatically set up Amazon EBS volumes when an instance is launched.
Type: [AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails](API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails.md) object
Required: No

 ** NoDevice **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails-NoDevice"></a>
Whether to suppress the device that is included in the block device mapping of the Amazon Machine Image (AMI).
If `NoDevice` is `true`, then you cannot specify `Ebs`.>
Type: Boolean
Required: No

 ** VirtualName **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails-VirtualName"></a>
The name of the virtual device (for example, `ephemeral0`).
You can provide either `VirtualName` or `Ebs`, but not both.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails)
