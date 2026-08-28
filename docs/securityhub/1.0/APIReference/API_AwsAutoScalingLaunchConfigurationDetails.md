---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAutoScalingLaunchConfigurationDetails.html
---

# AwsAutoScalingLaunchConfigurationDetails
<a name="API_AwsAutoScalingLaunchConfigurationDetails"></a>

Details about a launch configuration.

## Contents
<a name="API_AwsAutoScalingLaunchConfigurationDetails_Contents"></a>

 ** AssociatePublicIpAddress **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-AssociatePublicIpAddress"></a>
For Auto Scaling groups that run in a VPC, specifies whether to assign a public IP address to the group's instances.
Type: Boolean
Required: No

 ** BlockDeviceMappings **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-BlockDeviceMappings"></a>
Specifies the block devices for the instance.
Type: Array of [AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails](API_AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails.md) objects
Required: No

 ** ClassicLinkVpcId **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-ClassicLinkVpcId"></a>
The identifier of a ClassicLink-enabled VPC that EC2-Classic instances are linked to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClassicLinkVpcSecurityGroups **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-ClassicLinkVpcSecurityGroups"></a>
The identifiers of one or more security groups for the VPC that is specified in `ClassicLinkVPCId`.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** CreatedTime **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-CreatedTime"></a>
The creation date and time for the launch configuration.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** EbsOptimized **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-EbsOptimized"></a>
Whether the launch configuration is optimized for Amazon EBS I/O.
Type: Boolean
Required: No

 ** IamInstanceProfile **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-IamInstanceProfile"></a>
The name or the ARN of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ImageId **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-ImageId"></a>
The identifier of the Amazon Machine Image (AMI) that is used to launch EC2 instances.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceMonitoring **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-InstanceMonitoring"></a>
Indicates the type of monitoring for instances in the group.
Type: [AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails](API_AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails.md) object
Required: No

 ** InstanceType **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-InstanceType"></a>
The instance type for the instances.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KernelId **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-KernelId"></a>
The identifier of the kernel associated with the AMI.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeyName **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-KeyName"></a>
The name of the key pair.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LaunchConfigurationName **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-LaunchConfigurationName"></a>
The name of the launch configuration.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MetadataOptions **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-MetadataOptions"></a>
The metadata options for the instances.
Type: [AwsAutoScalingLaunchConfigurationMetadataOptions](API_AwsAutoScalingLaunchConfigurationMetadataOptions.md) object
Required: No

 ** PlacementTenancy **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-PlacementTenancy"></a>
The tenancy of the instance. An instance with `dedicated` tenancy runs on isolated, single-tenant hardware and can only be launched into a VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RamdiskId **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-RamdiskId"></a>
The identifier of the RAM disk associated with the AMI.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecurityGroups **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-SecurityGroups"></a>
The security groups to assign to the instances in the Auto Scaling group.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SpotPrice **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-SpotPrice"></a>
The maximum hourly price to be paid for any Spot Instance that is launched to fulfill the request.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserData **   <a name="securityhub-Type-AwsAutoScalingLaunchConfigurationDetails-UserData"></a>
The user data to make available to the launched EC2 instances. Must be base64-encoded text.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAutoScalingLaunchConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAutoScalingLaunchConfigurationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
