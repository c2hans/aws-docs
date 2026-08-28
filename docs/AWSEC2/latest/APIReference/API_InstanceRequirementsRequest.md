---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceRequirementsRequest.html
---

# InstanceRequirementsRequest
<a name="API_InstanceRequirementsRequest"></a>

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes.

You must specify `VCpuCount` and `MemoryMiB`. All other attributes are optional. Any unspecified optional attribute is set to its default.

When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.

To limit the list of instance types from which Amazon EC2 can identify matching instance types, you can use one of the following parameters, but not both in the same request:
+  `AllowedInstanceTypes` - The instance types to include in the list. All other instance types are ignored, even if they match your specified attributes.
+  `ExcludedInstanceTypes` - The instance types to exclude from the list, even if they match your specified attributes.

**Note**
If you specify `InstanceRequirements`, you can't specify `InstanceType`.
Attribute-based instance type selection is only supported when using Auto Scaling groups, EC2 Fleet, and Spot Fleet to launch instances. If you plan to use the launch template in the [launch instance wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html), or with the [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) API or [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) AWS CloudFormation resource, you can't specify `InstanceRequirements`.

For more information, see [Specify attributes for instance type selection for EC2 Fleet or Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html) and [Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_InstanceRequirementsRequest_Contents"></a>

 ** MemoryMiB **
The minimum and maximum amount of memory, in MiB.
Type: [MemoryMiBRequest](API_MemoryMiBRequest.md) object
Required: Yes

 ** VCpuCount **
The minimum and maximum number of vCPUs.
Type: [VCpuCountRangeRequest](API_VCpuCountRangeRequest.md) object
Required: Yes

 ** AcceleratorCount **
The minimum and maximum number of accelerators (GPUs, FPGAs, or AWS Inferentia chips) on an instance.
To exclude accelerator-enabled instance types, set `Max` to `0`.
Default: No minimum or maximum limits
Type: [AcceleratorCountRequest](API_AcceleratorCountRequest.md) object
Required: No

 ** AcceleratorManufacturer.N **
Indicates whether instance types must have accelerators by specific manufacturers.
+ For instance types with AWS devices, specify `amazon-web-services`.
+ For instance types with AMD devices, specify `amd`.
+ For instance types with Habana devices, specify `habana`.
+ For instance types with NVIDIA devices, specify `nvidia`.
+ For instance types with Xilinx devices, specify `xilinx`.
Default: Any manufacturer
Type: Array of strings
Valid Values: `amazon-web-services | amd | nvidia | xilinx | habana`
Required: No

 ** AcceleratorName.N **
The accelerators that must be on the instance type.
+ For instance types with NVIDIA A10G GPUs, specify `a10g`.
+ For instance types with NVIDIA A100 GPUs, specify `a100`.
+ For instance types with NVIDIA H100 GPUs, specify `h100`.
+ For instance types with AWS Inferentia chips, specify `inferentia`.
+ For instance types with AWS Inferentia2 chips, specify `inferentia2`.
+ For instance types with Habana Gaudi HL-205 GPUs, specify `gaudi-hl-205`.
+ For instance types with NVIDIA GRID K520 GPUs, specify `k520`.
+ For instance types with NVIDIA K80 GPUs, specify `k80`.
+ For instance types with NVIDIA L4 GPUs, specify `l4`.
+ For instance types with NVIDIA L40S GPUs, specify `l40s`.
+ For instance types with NVIDIA M60 GPUs, specify `m60`.
+ For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520`.
+ For instance types with AWS Trainium chips, specify `trainium`.
+ For instance types with AWS Trainium2 chips, specify `trainium2`.
+ For instance types with NVIDIA T4 GPUs, specify `t4`.
+ For instance types with NVIDIA T4G GPUs, specify `t4g`.
+ For instance types with Xilinx U30 cards, specify `u30`.
+ For instance types with Xilinx VU9P FPGAs, specify `vu9p`.
+ For instance types with NVIDIA V100 GPUs, specify `v100`.
Default: Any accelerator
Type: Array of strings
Valid Values: `a100 | inferentia | k520 | k80 | m60 | radeon-pro-v520 | t4 | vu9p | v100 | a10g | h100 | t4g | l40s | l4 | gaudi-hl-205 | inferentia2 | trainium | trainium2 | u30`
Required: No

 ** AcceleratorTotalMemoryMiB **
The minimum and maximum amount of total accelerator memory, in MiB.
Default: No minimum or maximum limits
Type: [AcceleratorTotalMemoryMiBRequest](API_AcceleratorTotalMemoryMiBRequest.md) object
Required: No

 ** AcceleratorType.N **
The accelerator types that must be on the instance type.
+ For instance types with FPGA accelerators, specify `fpga`.
+ For instance types with GPU accelerators, specify `gpu`.
+ For instance types with Inference accelerators, specify `inference`.
+ For instance types with Media accelerators, specify `media`.
Default: Any accelerator type
Type: Array of strings
Valid Values: `gpu | fpga | inference | media`
Required: No

 ** AllowedInstanceType.N **
The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.
You can use strings with one or more wild cards, represented by an asterisk (`*`), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge`, `c5*.*`, `m5a.*`, `r*`, `*3*`.
For example, if you specify `c5*`,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*`, Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.
If you specify `AllowedInstanceTypes`, you can't specify `ExcludedInstanceTypes`.
Default: All instance types
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\*\-]+`
Required: No

 ** BareMetal **
Indicates whether bare metal instance types must be included, excluded, or required.
+ To include bare metal instance types, specify `included`.
+ To require only bare metal instance types, specify `required`.
+ To exclude bare metal instance types, specify `excluded`.
Default: `excluded`
Type: String
Valid Values: `included | required | excluded`
Required: No

 ** BaselineEbsBandwidthMbps **
The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide*.
Default: No minimum or maximum limits
Type: [BaselineEbsBandwidthMbpsRequest](API_BaselineEbsBandwidthMbpsRequest.md) object
Required: No

 ** BaselinePerformanceFactors **
The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see [Performance protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection) in the *Amazon EC2 User Guide*.
Type: [BaselinePerformanceFactorsRequest](API_BaselinePerformanceFactorsRequest.md) object
Required: No

 ** BurstablePerformance **
Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html).
+ To include burstable performance instance types, specify `included`.
+ To require only burstable performance instance types, specify `required`.
+ To exclude burstable performance instance types, specify `excluded`.
Default: `excluded`
Type: String
Valid Values: `included | required | excluded`
Required: No

 ** CpuManufacturer.N **
The CPU manufacturers to include.
+ For instance types with Intel CPUs, specify `intel`.
+ For instance types with AMD CPUs, specify `amd`.
+ For instance types with AWS CPUs, specify `amazon-web-services`.
+ For instance types with Apple CPUs, specify `apple`.
Don't confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.
Default: Any manufacturer
Type: Array of strings
Valid Values: `intel | amd | amazon-web-services | apple`
Required: No

 ** ExcludedInstanceType.N **
The instance types to exclude.
You can use strings with one or more wild cards, represented by an asterisk (`*`), to exclude an instance family, type, size, or generation. The following are examples: `m5.8xlarge`, `c5*.*`, `m5a.*`, `r*`, `*3*`.
For example, if you specify `c5*`,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*`, Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.
If you specify `ExcludedInstanceTypes`, you can't specify `AllowedInstanceTypes`.
Default: No excluded instance types
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\*\-]+`
Required: No

 ** InstanceGeneration.N **
Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*.
For current generation instance types, specify `current`.
For previous generation instance types, specify `previous`.
Default: Current and previous generation instance types
Type: Array of strings
Valid Values: `current | previous`
Required: No

 ** LocalStorage **
Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide*.
+ To include instance types with instance store volumes, specify `included`.
+ To require only instance types with instance store volumes, specify `required`.
+ To exclude instance types with instance store volumes, specify `excluded`.
Default: `included`
Type: String
Valid Values: `included | required | excluded`
Required: No

 ** LocalStorageType.N **
The type of local storage that is required.
+ For instance types with hard disk drive (HDD) storage, specify `hdd`.
+ For instance types with solid state drive (SSD) storage, specify `ssd`.
Default: `hdd` and `ssd`
Type: Array of strings
Valid Values: `hdd | ssd`
Required: No

 ** MaxSpotPriceAsPercentageOfOptimalOnDemandPrice **
[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib`, the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.
Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you don't specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999`.
Type: Integer
Required: No

 ** MemoryGiBPerVCpu **
The minimum and maximum amount of memory per vCPU, in GiB.
Default: No minimum or maximum limits
Type: [MemoryGiBPerVCpuRequest](API_MemoryGiBPerVCpuRequest.md) object
Required: No

 ** NetworkBandwidthGbps **
The minimum and maximum amount of baseline network bandwidth, in gigabits per second (Gbps). For more information, see [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) in the *Amazon EC2 User Guide*.
Default: No minimum or maximum limits
Type: [NetworkBandwidthGbpsRequest](API_NetworkBandwidthGbpsRequest.md) object
Required: No

 ** NetworkInterfaceCount **
The minimum and maximum number of network interfaces.
Default: No minimum or maximum limits
Type: [NetworkInterfaceCountRequest](API_NetworkInterfaceCountRequest.md) object
Required: No

 ** OnDemandMaxPricePercentageOverLowestPrice **
[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
To indicate no price protection threshold, specify a high value, such as `999999`.
This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html).
If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib`, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.
Default: `20`
Type: Integer
Required: No

 ** RequireEncryptionInTransit **
Specifies whether instance types must support encrypting in-transit traffic between instances. For more information, including the supported instance types, see [Encryption in transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) in the *Amazon EC2 User Guide*.
Default: `false`
Type: Boolean
Required: No

 ** RequireHibernateSupport **
Indicates whether instance types must support hibernation for On-Demand Instances.
This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html).
Default: `false`
Type: Boolean
Required: No

 ** SpotMaxPricePercentageOverLowestPrice **
[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib`, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.
This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html).
Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you don't specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999`.
Default: `100`
Type: Integer
Required: No

 ** TotalLocalStorageGB **
The minimum and maximum amount of total local storage, in GB.
Default: No minimum or maximum limits
Type: [TotalLocalStorageGBRequest](API_TotalLocalStorageGBRequest.md) object
Required: No

## See Also
<a name="API_InstanceRequirementsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceRequirementsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceRequirementsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceRequirementsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
