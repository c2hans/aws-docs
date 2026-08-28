---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet InstanceRequirementsRequest
<a name="aws-properties-ec2-ec2fleet-instancerequirementsrequest"></a>

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes.

You must specify `VCpuCount` and `MemoryMiB`. All other attributes are optional. Any unspecified optional attribute is set to its default.

When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.

To limit the list of instance types from which Amazon EC2 can identify matching instance types, you can use one of the following parameters, but not both in the same request:
+ `AllowedInstanceTypes` - The instance types to include in the list. All other instance types are ignored, even if they match your specified attributes.
+ `ExcludedInstanceTypes` - The instance types to exclude from the list, even if they match your specified attributes.

**Note**
If you specify `InstanceRequirements`, you can't specify `InstanceType`.
Attribute-based instance type selection is only supported when using Auto Scaling groups, EC2 Fleet, and Spot Fleet to launch instances. If you plan to use the launch template in the [launch instance wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html), or with the [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) API or [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)AWS CloudFormation resource, you can't specify `InstanceRequirements`.

For more information, see [Specify attributes for instance type selection for EC2 Fleet or Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html) and [Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-properties-ec2-ec2fleet-instancerequirementsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-instancerequirementsrequest-syntax.json"></a>

```
{
  "[AcceleratorCount](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratorcount)" : {{AcceleratorCountRequest}},
  "[AcceleratorManufacturers](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratormanufacturers)" : {{[ String, ... ]}},
  "[AcceleratorNames](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratornames)" : {{[ String, ... ]}},
  "[AcceleratorTotalMemoryMiB](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratortotalmemorymib)" : {{AcceleratorTotalMemoryMiBRequest}},
  "[AcceleratorTypes](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratortypes)" : {{[ String, ... ]}},
  "[AllowedInstanceTypes](#cfn-ec2-ec2fleet-instancerequirementsrequest-allowedinstancetypes)" : {{[ String, ... ]}},
  "[BareMetal](#cfn-ec2-ec2fleet-instancerequirementsrequest-baremetal)" : {{String}},
  "[BaselineEbsBandwidthMbps](#cfn-ec2-ec2fleet-instancerequirementsrequest-baselineebsbandwidthmbps)" : {{BaselineEbsBandwidthMbpsRequest}},
  "[BaselinePerformanceFactors](#cfn-ec2-ec2fleet-instancerequirementsrequest-baselineperformancefactors)" : {{BaselinePerformanceFactorsRequest}},
  "[BurstablePerformance](#cfn-ec2-ec2fleet-instancerequirementsrequest-burstableperformance)" : {{String}},
  "[CpuManufacturers](#cfn-ec2-ec2fleet-instancerequirementsrequest-cpumanufacturers)" : {{[ String, ... ]}},
  "[ExcludedInstanceTypes](#cfn-ec2-ec2fleet-instancerequirementsrequest-excludedinstancetypes)" : {{[ String, ... ]}},
  "[InstanceGenerations](#cfn-ec2-ec2fleet-instancerequirementsrequest-instancegenerations)" : {{[ String, ... ]}},
  "[LocalStorage](#cfn-ec2-ec2fleet-instancerequirementsrequest-localstorage)" : {{String}},
  "[LocalStorageTypes](#cfn-ec2-ec2fleet-instancerequirementsrequest-localstoragetypes)" : {{[ String, ... ]}},
  "[MaxSpotPriceAsPercentageOfOptimalOnDemandPrice](#cfn-ec2-ec2fleet-instancerequirementsrequest-maxspotpriceaspercentageofoptimalondemandprice)" : {{Integer}},
  "[MemoryGiBPerVCpu](#cfn-ec2-ec2fleet-instancerequirementsrequest-memorygibpervcpu)" : {{MemoryGiBPerVCpuRequest}},
  "[MemoryMiB](#cfn-ec2-ec2fleet-instancerequirementsrequest-memorymib)" : {{MemoryMiBRequest}},
  "[NetworkBandwidthGbps](#cfn-ec2-ec2fleet-instancerequirementsrequest-networkbandwidthgbps)" : {{NetworkBandwidthGbpsRequest}},
  "[NetworkInterfaceCount](#cfn-ec2-ec2fleet-instancerequirementsrequest-networkinterfacecount)" : {{NetworkInterfaceCountRequest}},
  "[OnDemandMaxPricePercentageOverLowestPrice](#cfn-ec2-ec2fleet-instancerequirementsrequest-ondemandmaxpricepercentageoverlowestprice)" : {{Integer}},
  "[RequireEncryptionInTransit](#cfn-ec2-ec2fleet-instancerequirementsrequest-requireencryptionintransit)" : {{Boolean}},
  "[RequireHibernateSupport](#cfn-ec2-ec2fleet-instancerequirementsrequest-requirehibernatesupport)" : {{Boolean}},
  "[SpotMaxPricePercentageOverLowestPrice](#cfn-ec2-ec2fleet-instancerequirementsrequest-spotmaxpricepercentageoverlowestprice)" : {{Integer}},
  "[TotalLocalStorageGB](#cfn-ec2-ec2fleet-instancerequirementsrequest-totallocalstoragegb)" : {{TotalLocalStorageGBRequest}},
  "[VCpuCount](#cfn-ec2-ec2fleet-instancerequirementsrequest-vcpucount)" : {{VCpuCountRangeRequest}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-instancerequirementsrequest-syntax.yaml"></a>

```
  [AcceleratorCount](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratorcount): {{
    AcceleratorCountRequest}}
  [AcceleratorManufacturers](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratormanufacturers): {{
    - String}}
  [AcceleratorNames](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratornames): {{
    - String}}
  [AcceleratorTotalMemoryMiB](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratortotalmemorymib): {{
    AcceleratorTotalMemoryMiBRequest}}
  [AcceleratorTypes](#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratortypes): {{
    - String}}
  [AllowedInstanceTypes](#cfn-ec2-ec2fleet-instancerequirementsrequest-allowedinstancetypes): {{
    - String}}
  [BareMetal](#cfn-ec2-ec2fleet-instancerequirementsrequest-baremetal): {{String}}
  [BaselineEbsBandwidthMbps](#cfn-ec2-ec2fleet-instancerequirementsrequest-baselineebsbandwidthmbps): {{
    BaselineEbsBandwidthMbpsRequest}}
  [BaselinePerformanceFactors](#cfn-ec2-ec2fleet-instancerequirementsrequest-baselineperformancefactors): {{
    BaselinePerformanceFactorsRequest}}
  [BurstablePerformance](#cfn-ec2-ec2fleet-instancerequirementsrequest-burstableperformance): {{String}}
  [CpuManufacturers](#cfn-ec2-ec2fleet-instancerequirementsrequest-cpumanufacturers): {{
    - String}}
  [ExcludedInstanceTypes](#cfn-ec2-ec2fleet-instancerequirementsrequest-excludedinstancetypes): {{
    - String}}
  [InstanceGenerations](#cfn-ec2-ec2fleet-instancerequirementsrequest-instancegenerations): {{
    - String}}
  [LocalStorage](#cfn-ec2-ec2fleet-instancerequirementsrequest-localstorage): {{String}}
  [LocalStorageTypes](#cfn-ec2-ec2fleet-instancerequirementsrequest-localstoragetypes): {{
    - String}}
  [MaxSpotPriceAsPercentageOfOptimalOnDemandPrice](#cfn-ec2-ec2fleet-instancerequirementsrequest-maxspotpriceaspercentageofoptimalondemandprice): {{Integer}}
  [MemoryGiBPerVCpu](#cfn-ec2-ec2fleet-instancerequirementsrequest-memorygibpervcpu): {{
    MemoryGiBPerVCpuRequest}}
  [MemoryMiB](#cfn-ec2-ec2fleet-instancerequirementsrequest-memorymib): {{
    MemoryMiBRequest}}
  [NetworkBandwidthGbps](#cfn-ec2-ec2fleet-instancerequirementsrequest-networkbandwidthgbps): {{
    NetworkBandwidthGbpsRequest}}
  [NetworkInterfaceCount](#cfn-ec2-ec2fleet-instancerequirementsrequest-networkinterfacecount): {{
    NetworkInterfaceCountRequest}}
  [OnDemandMaxPricePercentageOverLowestPrice](#cfn-ec2-ec2fleet-instancerequirementsrequest-ondemandmaxpricepercentageoverlowestprice): {{Integer}}
  [RequireEncryptionInTransit](#cfn-ec2-ec2fleet-instancerequirementsrequest-requireencryptionintransit): {{Boolean}}
  [RequireHibernateSupport](#cfn-ec2-ec2fleet-instancerequirementsrequest-requirehibernatesupport): {{Boolean}}
  [SpotMaxPricePercentageOverLowestPrice](#cfn-ec2-ec2fleet-instancerequirementsrequest-spotmaxpricepercentageoverlowestprice): {{Integer}}
  [TotalLocalStorageGB](#cfn-ec2-ec2fleet-instancerequirementsrequest-totallocalstoragegb): {{
    TotalLocalStorageGBRequest}}
  [VCpuCount](#cfn-ec2-ec2fleet-instancerequirementsrequest-vcpucount): {{
    VCpuCountRangeRequest}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-instancerequirementsrequest-properties"></a>

`AcceleratorCount`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratorcount"></a>
The minimum and maximum number of accelerators (GPUs, FPGAs, or AWS Inferentia chips) on an instance.
To exclude accelerator-enabled instance types, set `Max` to `0`.
Default: No minimum or maximum limits
*Required*: No
*Type*: [AcceleratorCountRequest](aws-properties-ec2-ec2fleet-acceleratorcountrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AcceleratorManufacturers`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratormanufacturers"></a>
Indicates whether instance types must have accelerators by specific manufacturers.
+ For instance types with AWS devices, specify `amazon-web-services`.
+ For instance types with AMD devices, specify `amd`.
+ For instance types with Habana devices, specify `habana`.
+ For instance types with NVIDIA devices, specify `nvidia`.
+ For instance types with Xilinx devices, specify `xilinx`.
Default: Any manufacturer
*Required*: No
*Type*: Array of String
*Allowed values*: `amazon-web-services | amd | habana | nvidia | xilinx`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AcceleratorNames`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratornames"></a>
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
*Required*: No
*Type*: Array of String
*Allowed values*: `a10g | a100 | h100 | inferentia | k520 | k80 | m60 | radeon-pro-v520 | t4 | t4g | vu9p | v100 | l40s | l4 | gaudi-hl-205 | inferentia2 | trainium | trainium2 | u30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AcceleratorTotalMemoryMiB`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratortotalmemorymib"></a>
The minimum and maximum amount of total accelerator memory, in MiB.
Default: No minimum or maximum limits
*Required*: No
*Type*: [AcceleratorTotalMemoryMiBRequest](aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AcceleratorTypes`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratortypes"></a>
The accelerator types that must be on the instance type.
+ For instance types with FPGA accelerators, specify `fpga`.
+ For instance types with GPU accelerators, specify `gpu`.
+ For instance types with Inference accelerators, specify `inference`.
+ For instance types with Media accelerators, specify `media`.
Default: Any accelerator type
*Required*: No
*Type*: Array of String
*Allowed values*: `gpu | fpga | inference | media`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowedInstanceTypes`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-allowedinstancetypes"></a>
The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.
You can use strings with one or more wild cards, represented by an asterisk (`*`), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge`, `c5*.*`, `m5a.*`, `r*`, `*3*`.
For example, if you specify `c5*`,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*`, Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.
If you specify `AllowedInstanceTypes`, you can't specify `ExcludedInstanceTypes`.
Default: All instance types
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BareMetal`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-baremetal"></a>
Indicates whether bare metal instance types must be included, excluded, or required.
+ To include bare metal instance types, specify `included`.
+ To require only bare metal instance types, specify `required`.
+ To exclude bare metal instance types, specify `excluded`.
Default: `excluded`
*Required*: No
*Type*: String
*Allowed values*: `included | required | excluded`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BaselineEbsBandwidthMbps`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-baselineebsbandwidthmbps"></a>
The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide*.
Default: No minimum or maximum limits
*Required*: No
*Type*: [BaselineEbsBandwidthMbpsRequest](aws-properties-ec2-ec2fleet-baselineebsbandwidthmbpsrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BaselinePerformanceFactors`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-baselineperformancefactors"></a>
The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see [Performance protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: [BaselinePerformanceFactorsRequest](aws-properties-ec2-ec2fleet-baselineperformancefactorsrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BurstablePerformance`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-burstableperformance"></a>
Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html).
+ To include burstable performance instance types, specify `included`.
+ To require only burstable performance instance types, specify `required`.
+ To exclude burstable performance instance types, specify `excluded`.
Default: `excluded`
*Required*: No
*Type*: String
*Allowed values*: `included | required | excluded`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CpuManufacturers`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-cpumanufacturers"></a>
The CPU manufacturers to include.
+ For instance types with Intel CPUs, specify `intel`.
+ For instance types with AMD CPUs, specify `amd`.
+ For instance types with AWS CPUs, specify `amazon-web-services`.
+ For instance types with Apple CPUs, specify `apple`.
Don't confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.
Default: Any manufacturer
*Required*: No
*Type*: Array of String
*Allowed values*: `intel | amd | amazon-web-services | apple`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExcludedInstanceTypes`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-excludedinstancetypes"></a>
The instance types to exclude.
You can use strings with one or more wild cards, represented by an asterisk (`*`), to exclude an instance family, type, size, or generation. The following are examples: `m5.8xlarge`, `c5*.*`, `m5a.*`, `r*`, `*3*`.
For example, if you specify `c5*`,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*`, Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.
If you specify `ExcludedInstanceTypes`, you can't specify `AllowedInstanceTypes`.
Default: No excluded instance types
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceGenerations`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-instancegenerations"></a>
Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*.
For current generation instance types, specify `current`.
For previous generation instance types, specify `previous`.
Default: Current and previous generation instance types
*Required*: No
*Type*: Array of String
*Allowed values*: `current | previous`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalStorage`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-localstorage"></a>
Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide*.
+ To include instance types with instance store volumes, specify `included`.
+ To require only instance types with instance store volumes, specify `required`.
+ To exclude instance types with instance store volumes, specify `excluded`.
Default: `included`
*Required*: No
*Type*: String
*Allowed values*: `included | required | excluded`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalStorageTypes`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-localstoragetypes"></a>
The type of local storage that is required.
+ For instance types with hard disk drive (HDD) storage, specify `hdd`.
+ For instance types with solid state drive (SSD) storage, specify `ssd`.
Default: `hdd` and `ssd`
*Required*: No
*Type*: Array of String
*Allowed values*: `hdd | ssd`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxSpotPriceAsPercentageOfOptimalOnDemandPrice`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-maxspotpriceaspercentageofoptimalondemandprice"></a>
[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib`, the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.
Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you don't specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999`.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemoryGiBPerVCpu`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-memorygibpervcpu"></a>
The minimum and maximum amount of memory per vCPU, in GiB.
Default: No minimum or maximum limits
*Required*: No
*Type*: [MemoryGiBPerVCpuRequest](aws-properties-ec2-ec2fleet-memorygibpervcpurequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemoryMiB`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-memorymib"></a>
The minimum and maximum amount of memory, in MiB.
*Required*: No
*Type*: [MemoryMiBRequest](aws-properties-ec2-ec2fleet-memorymibrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkBandwidthGbps`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-networkbandwidthgbps"></a>
The minimum and maximum amount of baseline network bandwidth, in gigabits per second (Gbps). For more information, see [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) in the *Amazon EC2 User Guide*.
Default: No minimum or maximum limits
*Required*: No
*Type*: [NetworkBandwidthGbpsRequest](aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkInterfaceCount`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-networkinterfacecount"></a>
The minimum and maximum number of network interfaces.
Default: No minimum or maximum limits
*Required*: No
*Type*: [NetworkInterfaceCountRequest](aws-properties-ec2-ec2fleet-networkinterfacecountrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OnDemandMaxPricePercentageOverLowestPrice`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-ondemandmaxpricepercentageoverlowestprice"></a>
[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
To indicate no price protection threshold, specify a high value, such as `999999`.
This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html).
If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib`, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.
Default: `20`
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequireEncryptionInTransit`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-requireencryptionintransit"></a>
Specifies whether instance types must support encrypting in-transit traffic between instances. For more information, including the supported instance types, see [Encryption in transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) in the *Amazon EC2 User Guide*.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequireHibernateSupport`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-requirehibernatesupport"></a>
Indicates whether instance types must support hibernation for On-Demand Instances.
This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html).
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpotMaxPricePercentageOverLowestPrice`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-spotmaxpricepercentageoverlowestprice"></a>
[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib`, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.
This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html).
Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you don't specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999`.
Default: `100`
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TotalLocalStorageGB`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-totallocalstoragegb"></a>
The minimum and maximum amount of total local storage, in GB.
Default: No minimum or maximum limits
*Required*: No
*Type*: [TotalLocalStorageGBRequest](aws-properties-ec2-ec2fleet-totallocalstoragegbrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VCpuCount`  <a name="cfn-ec2-ec2fleet-instancerequirementsrequest-vcpucount"></a>
The minimum and maximum number of vCPUs.
*Required*: No
*Type*: [VCpuCountRangeRequest](aws-properties-ec2-ec2fleet-vcpucountrangerequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
