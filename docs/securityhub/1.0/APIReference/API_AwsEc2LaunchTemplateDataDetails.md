---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataDetails.html
---

# AwsEc2LaunchTemplateDataDetails
<a name="API_AwsEc2LaunchTemplateDataDetails"></a>

 The information to include in an Amazon Elastic Compute Cloud (Amazon EC2) launch template.

## Contents
<a name="API_AwsEc2LaunchTemplateDataDetails_Contents"></a>

 ** BlockDeviceMappingSet **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-BlockDeviceMappingSet"></a>
 Information about a block device mapping for an Amazon EC2 launch template.
Type: Array of [AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails](API_AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails.md) objects
Required: No

 ** CapacityReservationSpecification **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-CapacityReservationSpecification"></a>
 Specifies an instance's Capacity Reservation targeting option. You can specify only one option at a time.
Type: [AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails](API_AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails.md) object
Required: No

 ** CpuOptions **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-CpuOptions"></a>
 Specifies the CPU options for an instance. For more information, see [Optimize CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) in the *Amazon Elastic Compute Cloud User Guide*.
Type: [AwsEc2LaunchTemplateDataCpuOptionsDetails](API_AwsEc2LaunchTemplateDataCpuOptionsDetails.md) object
Required: No

 ** CreditSpecification **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-CreditSpecification"></a>
 Specifies the credit option for CPU usage of a T2, T3, or T3a instance.
Type: [AwsEc2LaunchTemplateDataCreditSpecificationDetails](API_AwsEc2LaunchTemplateDataCreditSpecificationDetails.md) object
Required: No

 ** DisableApiStop **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-DisableApiStop"></a>
 Indicates whether to enable the instance for stop protection. For more information, see [Enable stop protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html#Using_StopProtection) in the *Amazon EC2 User Guide*.
Type: Boolean
Required: No

 ** DisableApiTermination **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-DisableApiTermination"></a>
 If you set this parameter to `true`, you can't terminate the instance using the Amazon EC2 console, AWS CLI, or API. If set to `true`, you can.
Type: Boolean
Required: No

 ** EbsOptimized **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-EbsOptimized"></a>
 Indicates whether the instance is optimized for Amazon EBS I/O.
Type: Boolean
Required: No

 ** ElasticGpuSpecificationSet **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-ElasticGpuSpecificationSet"></a>
 Provides details about Elastic Graphics accelerators to associate with the instance.
Type: Array of [AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails](API_AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails.md) objects
Required: No

 ** ElasticInferenceAcceleratorSet **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-ElasticInferenceAcceleratorSet"></a>
 The Amazon Elastic Inference accelerator for the instance.
Type: Array of [AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails](API_AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails.md) objects
Required: No

 ** EnclaveOptions **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-EnclaveOptions"></a>
 Indicates whether the Amazon EC2 instance is enabled for AWS Nitro Enclaves.
Type: [AwsEc2LaunchTemplateDataEnclaveOptionsDetails](API_AwsEc2LaunchTemplateDataEnclaveOptionsDetails.md) object
Required: No

 ** HibernationOptions **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-HibernationOptions"></a>
 Specifies whether your Amazon EC2 instance is configured for hibernation.
Type: [AwsEc2LaunchTemplateDataHibernationOptionsDetails](API_AwsEc2LaunchTemplateDataHibernationOptionsDetails.md) object
Required: No

 ** IamInstanceProfile **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-IamInstanceProfile"></a>
 The name or Amazon Resource Name (ARN) of an IAM instance profile.
Type: [AwsEc2LaunchTemplateDataIamInstanceProfileDetails](API_AwsEc2LaunchTemplateDataIamInstanceProfileDetails.md) object
Required: No

 ** ImageId **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-ImageId"></a>
 The ID of the Amazon Machine Image (AMI).
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceInitiatedShutdownBehavior **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-InstanceInitiatedShutdownBehavior"></a>
 Provides the options for specifying the instance initiated shutdown behavior.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceMarketOptions **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-InstanceMarketOptions"></a>
 Specifies the market (purchasing) option for an instance.
Type: [AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails](API_AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails.md) object
Required: No

 ** InstanceRequirements **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-InstanceRequirements"></a>
 The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes. If you specify `InstanceRequirements`, you can't specify `InstanceType`.
Type: [AwsEc2LaunchTemplateDataInstanceRequirementsDetails](API_AwsEc2LaunchTemplateDataInstanceRequirementsDetails.md) object
Required: No

 ** InstanceType **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-InstanceType"></a>
 The instance type. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*. If you specify `InstanceType`, you can't specify `InstanceRequirements`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KernelId **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-KernelId"></a>
 The ID of the kernel.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeyName **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-KeyName"></a>
 The name of the key pair that allows users to connect to the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LicenseSet **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-LicenseSet"></a>
 Specifies a license configuration for an instance.
Type: Array of [AwsEc2LaunchTemplateDataLicenseSetDetails](API_AwsEc2LaunchTemplateDataLicenseSetDetails.md) objects
Required: No

 ** MaintenanceOptions **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-MaintenanceOptions"></a>
 The maintenance options of your instance.
Type: [AwsEc2LaunchTemplateDataMaintenanceOptionsDetails](API_AwsEc2LaunchTemplateDataMaintenanceOptionsDetails.md) object
Required: No

 ** MetadataOptions **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-MetadataOptions"></a>
 The metadata options for the instance. For more information, see [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*.
Type: [AwsEc2LaunchTemplateDataMetadataOptionsDetails](API_AwsEc2LaunchTemplateDataMetadataOptionsDetails.md) object
Required: No

 ** Monitoring **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-Monitoring"></a>
 The monitoring for the instance.
Type: [AwsEc2LaunchTemplateDataMonitoringDetails](API_AwsEc2LaunchTemplateDataMonitoringDetails.md) object
Required: No

 ** NetworkInterfaceSet **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-NetworkInterfaceSet"></a>
 Specifies the parameters for a network interface that is attached to the instance.
Type: Array of [AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails](API_AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails.md) objects
Required: No

 ** Placement **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-Placement"></a>
 Specifies the placement of an instance.
Type: [AwsEc2LaunchTemplateDataPlacementDetails](API_AwsEc2LaunchTemplateDataPlacementDetails.md) object
Required: No

 ** PrivateDnsNameOptions **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-PrivateDnsNameOptions"></a>
 The options for the instance hostname.
Type: [AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails](API_AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails.md) object
Required: No

 ** RamDiskId **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-RamDiskId"></a>
 The ID of the RAM disk.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecurityGroupIdSet **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-SecurityGroupIdSet"></a>
 One or more security group IDs.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SecurityGroupSet **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-SecurityGroupSet"></a>
 One or more security group names. For a nondefault VPC, you must use security group IDs instead. You cannot specify both a security group ID and security name in the same request.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** UserData **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataDetails-UserData"></a>
 The user data to make available to the instance.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataDetails)
