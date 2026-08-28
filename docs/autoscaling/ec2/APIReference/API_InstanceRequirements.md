---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html
---

# InstanceRequirements
<a name="API_InstanceRequirements"></a>

The attributes for the instance types for a mixed instances policy. Amazon EC2 Auto Scaling uses your specified requirements to identify instance types. Then, it uses your On-Demand and Spot allocation strategies to launch instances from these instance types.

When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.

To limit the list of instance types from which Amazon EC2 Auto Scaling can identify matching instance types, you can use one of the following parameters, but not both in the same request:
+  `AllowedInstanceTypes` - The instance types to include in the list. All other instance types are ignored, even if they match your specified attributes.
+  `ExcludedInstanceTypes` - The instance types to exclude from the list, even if they match your specified attributes.

**Note**
You must specify `VCpuCount` and `MemoryMiB`. All other attributes are optional. Any unspecified optional attribute is set to its default.

For more information, see [Create a mixed instances group using attribute-based instance type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html) in the *Amazon EC2 Auto Scaling User Guide*. For help determining which instance types match your attributes before you apply them to your Auto Scaling group, see [Preview instance types with specified attributes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-get-instance-types-from-instance-requirements) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_InstanceRequirements_Contents"></a>

 ** MemoryMiB **
The minimum and maximum instance memory size for an instance type, in MiB.
Type: [MemoryMiBRequest](API_MemoryMiBRequest.md) object
Required: Yes

 ** VCpuCount **
The minimum and maximum number of vCPUs for an instance type.
Type: [VCpuCountRequest](API_VCpuCountRequest.md) object
Required: Yes

 ** AcceleratorCount **
The minimum and maximum number of accelerators (GPUs, FPGAs, or AWS Inferentia chips) for an instance type.
To exclude accelerator-enabled instance types, set `Max` to `0`.
Default: No minimum or maximum limits
Type: [AcceleratorCountRequest](API_AcceleratorCountRequest.md) object
Required: No

 ** AcceleratorManufacturers.member.N **
Indicates whether instance types must have accelerators by specific manufacturers.
+ For instance types with NVIDIA devices, specify `nvidia`.
+ For instance types with AMD devices, specify `amd`.
+ For instance types with AWS devices, specify `amazon-web-services`.
+ For instance types with Xilinx devices, specify `xilinx`.
Default: Any manufacturer
Type: Array of strings
Valid Values: `nvidia | amd | amazon-web-services | xilinx`
Required: No

 ** AcceleratorNames.member.N **
Lists the accelerators that must be on an instance type.
+ For instance types with NVIDIA A100 GPUs, specify `a100`.
+ For instance types with NVIDIA V100 GPUs, specify `v100`.
+ For instance types with NVIDIA K80 GPUs, specify `k80`.
+ For instance types with NVIDIA T4 GPUs, specify `t4`.
+ For instance types with NVIDIA M60 GPUs, specify `m60`.
+ For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520`.
+ For instance types with Xilinx VU9P FPGAs, specify `vu9p`.
Default: Any accelerator
Type: Array of strings
Valid Values: `a100 | v100 | k80 | t4 | m60 | radeon-pro-v520 | vu9p`
Required: No

 ** AcceleratorTotalMemoryMiB **
The minimum and maximum total memory size for the accelerators on an instance type, in MiB.
Default: No minimum or maximum limits
Type: [AcceleratorTotalMemoryMiBRequest](API_AcceleratorTotalMemoryMiBRequest.md) object
Required: No

 ** AcceleratorTypes.member.N **
Lists the accelerator types that must be on an instance type.
+ For instance types with GPU accelerators, specify `gpu`.
+ For instance types with FPGA accelerators, specify `fpga`.
+ For instance types with inference accelerators, specify `inference`.
Default: Any accelerator type
Type: Array of strings
Valid Values: `gpu | fpga | inference`
Required: No

 ** AllowedInstanceTypes.member.N **
The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.
You can use strings with one or more wild cards, represented by an asterisk (`*`), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge`, `c5*.*`, `m5a.*`, `r*`, `*3*`.
For example, if you specify `c5*`, Amazon EC2 Auto Scaling will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*`, Amazon EC2 Auto Scaling will allow all the M5a instance types, but not the M5n instance types.
If you specify `AllowedInstanceTypes`, you can't specify `ExcludedInstanceTypes`.
Default: All instance types
Type: Array of strings
Array Members: Maximum number of 400 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\*\-]+`
Required: No

 ** BareMetal **
Indicates whether bare metal instance types are included, excluded, or required.
Default: `excluded`
Type: String
Valid Values: `included | excluded | required`
Required: No

 ** BaselineEbsBandwidthMbps **
The minimum and maximum baseline bandwidth performance for an instance type, in Mbps. For more information, see [Amazon EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide*.
Default: No minimum or maximum limits
Type: [BaselineEbsBandwidthMbpsRequest](API_BaselineEbsBandwidthMbpsRequest.md) object
Required: No

 ** BaselinePerformanceFactors **
 The baseline performance factors for the instance requirements.
Type: [BaselinePerformanceFactorsRequest](API_BaselinePerformanceFactorsRequest.md) object
Required: No

 ** BurstablePerformance **
Indicates whether burstable performance instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide*.
Default: `excluded`
Type: String
Valid Values: `included | excluded | required`
Required: No

 ** CpuManufacturers.member.N **
Lists which specific CPU manufacturers to include.
+ For instance types with Intel CPUs, specify `intel`.
+ For instance types with AMD CPUs, specify `amd`.
+ For instance types with AWS CPUs, specify `amazon-web-services`.
+ For instance types with Apple CPUs, specify `apple`.
Don't confuse the CPU hardware manufacturer with the CPU hardware architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.
Default: Any manufacturer
Type: Array of strings
Valid Values: `intel | amd | amazon-web-services | apple`
Required: No

 ** ExcludedInstanceTypes.member.N **
The instance types to exclude. You can use strings with one or more wild cards, represented by an asterisk (`*`), to exclude an instance family, type, size, or generation. The following are examples: `m5.8xlarge`, `c5*.*`, `m5a.*`, `r*`, `*3*`.
For example, if you specify `c5*`, you are excluding the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*`, Amazon EC2 Auto Scaling will exclude all the M5a instance types, but not the M5n instance types.
If you specify `ExcludedInstanceTypes`, you can't specify `AllowedInstanceTypes`.
Default: No excluded instance types
Type: Array of strings
Array Members: Maximum number of 400 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\*\-]+`
Required: No

 ** InstanceGenerations.member.N **
Indicates whether current or previous generation instance types are included.
+ For current generation instance types, specify `current`. The current generation includes EC2 instance types currently recommended for use. This typically includes the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*.
+ For previous generation instance types, specify `previous`.
Default: Any current or previous generation
Type: Array of strings
Valid Values: `current | previous`
Required: No

 ** LocalStorage **
Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, see [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide*.
Default: `included`
Type: String
Valid Values: `included | excluded | required`
Required: No

 ** LocalStorageTypes.member.N **
Indicates the type of local storage that is required.
+ For instance types with hard disk drive (HDD) storage, specify `hdd`.
+ For instance types with solid state drive (SSD) storage, specify `ssd`.
Default: Any local storage type
Type: Array of strings
Valid Values: `hdd | ssd`
Required: No

 ** MaxSpotPriceAsPercentageOfOptimalOnDemandPrice **
[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.
If you set `DesiredCapacityType` to `vcpu` or `memory-mib`, the price protection threshold is based on the per-vCPU or per-memory price instead of the per instance price.
Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you don't specify either, Amazon EC2 Auto Scaling will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MemoryGiBPerVCpu **
The minimum and maximum amount of memory per vCPU for an instance type, in GiB.
Default: No minimum or maximum limits
Type: [MemoryGiBPerVCpuRequest](API_MemoryGiBPerVCpuRequest.md) object
Required: No

 ** NetworkBandwidthGbps **
The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).
Default: No minimum or maximum limits
Type: [NetworkBandwidthGbpsRequest](API_NetworkBandwidthGbpsRequest.md) object
Required: No

 ** NetworkInterfaceCount **
The minimum and maximum number of network interfaces for an instance type.
Default: No minimum or maximum limits
Type: [NetworkInterfaceCountRequest](API_NetworkInterfaceCountRequest.md) object
Required: No

 ** OnDemandMaxPricePercentageOverLowestPrice **
[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.
To turn off price protection, specify a high value, such as `999999`.
If you set `DesiredCapacityType` to `vcpu` or `memory-mib`, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per instance price.
Default: `20`
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** RequireHibernateSupport **
Indicates whether instance types must provide On-Demand Instance hibernation support.
Default: `false`
Type: Boolean
Required: No

 ** SpotMaxPricePercentageOverLowestPrice **
[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.
If you set `DesiredCapacityType` to `vcpu` or `memory-mib`, the price protection threshold is based on the per-vCPU or per-memory price instead of the per instance price.
Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you don't specify either, Amazon EC2 Auto Scaling will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TotalLocalStorageGB **
The minimum and maximum total local storage size for an instance type, in GB.
Default: No minimum or maximum limits
Type: [TotalLocalStorageGBRequest](API_TotalLocalStorageGBRequest.md) object
Required: No

## See Also
<a name="API_InstanceRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/InstanceRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/InstanceRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/InstanceRequirements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
