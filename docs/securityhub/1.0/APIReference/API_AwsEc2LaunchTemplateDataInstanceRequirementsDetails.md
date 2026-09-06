---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataInstanceRequirementsDetails.html
---

# AwsEc2LaunchTemplateDataInstanceRequirementsDetails
<a name="API_AwsEc2LaunchTemplateDataInstanceRequirementsDetails"></a>

 The attributes for the Amazon EC2 instance types.

## Contents
<a name="API_AwsEc2LaunchTemplateDataInstanceRequirementsDetails_Contents"></a>

 ** AcceleratorCount **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-AcceleratorCount"></a>
 The minimum and maximum number of accelerators (GPUs, FPGAs, or AWS Inferentia chips) on an instance.
Type: [AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails](API_AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails.md) object
Required: No

 ** AcceleratorManufacturers **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-AcceleratorManufacturers"></a>
Indicates whether instance types must have accelerators by specific manufacturers.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** AcceleratorNames **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-AcceleratorNames"></a>
 The accelerators that must be on the instance type.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** AcceleratorTotalMemoryMiB **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-AcceleratorTotalMemoryMiB"></a>
 The minimum and maximum amount of total accelerator memory, in MiB.
Type: [AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails](API_AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails.md) object
Required: No

 ** AcceleratorTypes **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-AcceleratorTypes"></a>
The accelerator types that must be on the instance type.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** BareMetal **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-BareMetal"></a>
Indicates whether bare metal instance types must be included, excluded, or required.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BaselineEbsBandwidthMbps **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-BaselineEbsBandwidthMbps"></a>
 The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBS optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide*.
Type: [AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails](API_AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails.md) object
Required: No

 ** BurstablePerformance **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-BurstablePerformance"></a>
 Indicates whether burstable performance T instance types are included, excluded, or required. For more information, [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide*.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CpuManufacturers **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-CpuManufacturers"></a>
 The CPU manufacturers to include.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ExcludedInstanceTypes **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-ExcludedInstanceTypes"></a>
 The instance types to exclude.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** InstanceGenerations **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-InstanceGenerations"></a>
 Indicates whether current or previous generation instance types are included.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** LocalStorage **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-LocalStorage"></a>
 Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, see [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide*.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LocalStorageTypes **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-LocalStorageTypes"></a>
 The type of local storage that is required.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** MemoryGiBPerVCpu **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-MemoryGiBPerVCpu"></a>
 The minimum and maximum amount of memory per vCPU, in GiB.
Type: [AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails](API_AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails.md) object
Required: No

 ** MemoryMiB **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-MemoryMiB"></a>
 The minimum and maximum amount of memory, in MiB.
Type: [AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails](API_AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails.md) object
Required: No

 ** NetworkInterfaceCount **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-NetworkInterfaceCount"></a>
 The minimum and maximum number of network interfaces.
Type: [AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails](API_AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails.md) object
Required: No

 ** OnDemandMaxPricePercentageOverLowestPrice **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-OnDemandMaxPricePercentageOverLowestPrice"></a>
 The price protection threshold for On-Demand Instances. This is the maximum you'll pay for an On-Demand Instance, expressed as a percentage above the least expensive current generation M, C, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it excludes instance types priced above your threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
A high value, such as `999999`, turns off price protection.
Type: Integer
Required: No

 ** RequireHibernateSupport **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-RequireHibernateSupport"></a>
 Indicates whether instance types must support hibernation for On-Demand Instances.
Type: Boolean
Required: No

 ** SpotMaxPricePercentageOverLowestPrice **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-SpotMaxPricePercentageOverLowestPrice"></a>
 The price protection threshold for Spot Instances. This is the maximum you'll pay for a Spot Instance, expressed as a percentage above the least expensive current generation M, C, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it excludes instance types priced above your threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
A high value, such as `999999`, turns off price protection.
Type: Integer
Required: No

 ** TotalLocalStorageGB **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-TotalLocalStorageGB"></a>
 The minimum and maximum amount of total local storage, in GB.
Type: [AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails](API_AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails.md) object
Required: No

 ** VCpuCount **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsDetails-VCpuCount"></a>
 The minimum and maximum number of vCPUs.
Type: [AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails](API_AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails.md) object
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataInstanceRequirementsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataInstanceRequirementsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataInstanceRequirementsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataInstanceRequirementsDetails)
