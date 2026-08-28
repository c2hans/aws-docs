---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-instancerequirements.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate InstanceRequirements
<a name="aws-properties-ec2-launchtemplate-instancerequirements"></a>

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
<a name="aws-properties-ec2-launchtemplate-instancerequirements-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-instancerequirements-syntax.json"></a>

```
{
  "[AcceleratorCount](#cfn-ec2-launchtemplate-instancerequirements-acceleratorcount)" : {{AcceleratorCount}},
  "[AcceleratorManufacturers](#cfn-ec2-launchtemplate-instancerequirements-acceleratormanufacturers)" : {{[ String, ... ]}},
  "[AcceleratorNames](#cfn-ec2-launchtemplate-instancerequirements-acceleratornames)" : {{[ String, ... ]}},
  "[AcceleratorTotalMemoryMiB](#cfn-ec2-launchtemplate-instancerequirements-acceleratortotalmemorymib)" : {{AcceleratorTotalMemoryMiB}},
  "[AcceleratorTypes](#cfn-ec2-launchtemplate-instancerequirements-acceleratortypes)" : {{[ String, ... ]}},
  "[AllowedInstanceTypes](#cfn-ec2-launchtemplate-instancerequirements-allowedinstancetypes)" : {{[ String, ... ]}},
  "[BareMetal](#cfn-ec2-launchtemplate-instancerequirements-baremetal)" : {{String}},
  "[BaselineEbsBandwidthMbps](#cfn-ec2-launchtemplate-instancerequirements-baselineebsbandwidthmbps)" : {{BaselineEbsBandwidthMbps}},
  "[BaselinePerformanceFactors](#cfn-ec2-launchtemplate-instancerequirements-baselineperformancefactors)" : {{BaselinePerformanceFactors}},
  "[BurstablePerformance](#cfn-ec2-launchtemplate-instancerequirements-burstableperformance)" : {{String}},
  "[CpuManufacturers](#cfn-ec2-launchtemplate-instancerequirements-cpumanufacturers)" : {{[ String, ... ]}},
  "[ExcludedInstanceTypes](#cfn-ec2-launchtemplate-instancerequirements-excludedinstancetypes)" : {{[ String, ... ]}},
  "[InstanceGenerations](#cfn-ec2-launchtemplate-instancerequirements-instancegenerations)" : {{[ String, ... ]}},
  "[LocalStorage](#cfn-ec2-launchtemplate-instancerequirements-localstorage)" : {{String}},
  "[LocalStorageTypes](#cfn-ec2-launchtemplate-instancerequirements-localstoragetypes)" : {{[ String, ... ]}},
  "[MaxSpotPriceAsPercentageOfOptimalOnDemandPrice](#cfn-ec2-launchtemplate-instancerequirements-maxspotpriceaspercentageofoptimalondemandprice)" : {{Integer}},
  "[MemoryGiBPerVCpu](#cfn-ec2-launchtemplate-instancerequirements-memorygibpervcpu)" : {{MemoryGiBPerVCpu}},
  "[MemoryMiB](#cfn-ec2-launchtemplate-instancerequirements-memorymib)" : {{MemoryMiB}},
  "[NetworkBandwidthGbps](#cfn-ec2-launchtemplate-instancerequirements-networkbandwidthgbps)" : {{NetworkBandwidthGbps}},
  "[NetworkInterfaceCount](#cfn-ec2-launchtemplate-instancerequirements-networkinterfacecount)" : {{NetworkInterfaceCount}},
  "[OnDemandMaxPricePercentageOverLowestPrice](#cfn-ec2-launchtemplate-instancerequirements-ondemandmaxpricepercentageoverlowestprice)" : {{Integer}},
  "[RequireHibernateSupport](#cfn-ec2-launchtemplate-instancerequirements-requirehibernatesupport)" : {{Boolean}},
  "[SpotMaxPricePercentageOverLowestPrice](#cfn-ec2-launchtemplate-instancerequirements-spotmaxpricepercentageoverlowestprice)" : {{Integer}},
  "[TotalLocalStorageGB](#cfn-ec2-launchtemplate-instancerequirements-totallocalstoragegb)" : {{TotalLocalStorageGB}},
  "[VCpuCount](#cfn-ec2-launchtemplate-instancerequirements-vcpucount)" : {{VCpuCount}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-instancerequirements-syntax.yaml"></a>

```
  [AcceleratorCount](#cfn-ec2-launchtemplate-instancerequirements-acceleratorcount): {{
    AcceleratorCount}}
  [AcceleratorManufacturers](#cfn-ec2-launchtemplate-instancerequirements-acceleratormanufacturers): {{
    - String}}
  [AcceleratorNames](#cfn-ec2-launchtemplate-instancerequirements-acceleratornames): {{
    - String}}
  [AcceleratorTotalMemoryMiB](#cfn-ec2-launchtemplate-instancerequirements-acceleratortotalmemorymib): {{
    AcceleratorTotalMemoryMiB}}
  [AcceleratorTypes](#cfn-ec2-launchtemplate-instancerequirements-acceleratortypes): {{
    - String}}
  [AllowedInstanceTypes](#cfn-ec2-launchtemplate-instancerequirements-allowedinstancetypes): {{
    - String}}
  [BareMetal](#cfn-ec2-launchtemplate-instancerequirements-baremetal): {{String}}
  [BaselineEbsBandwidthMbps](#cfn-ec2-launchtemplate-instancerequirements-baselineebsbandwidthmbps): {{
    BaselineEbsBandwidthMbps}}
  [BaselinePerformanceFactors](#cfn-ec2-launchtemplate-instancerequirements-baselineperformancefactors): {{
    BaselinePerformanceFactors}}
  [BurstablePerformance](#cfn-ec2-launchtemplate-instancerequirements-burstableperformance): {{String}}
  [CpuManufacturers](#cfn-ec2-launchtemplate-instancerequirements-cpumanufacturers): {{
    - String}}
  [ExcludedInstanceTypes](#cfn-ec2-launchtemplate-instancerequirements-excludedinstancetypes): {{
    - String}}
  [InstanceGenerations](#cfn-ec2-launchtemplate-instancerequirements-instancegenerations): {{
    - String}}
  [LocalStorage](#cfn-ec2-launchtemplate-instancerequirements-localstorage): {{String}}
  [LocalStorageTypes](#cfn-ec2-launchtemplate-instancerequirements-localstoragetypes): {{
    - String}}
  [MaxSpotPriceAsPercentageOfOptimalOnDemandPrice](#cfn-ec2-launchtemplate-instancerequirements-maxspotpriceaspercentageofoptimalondemandprice): {{Integer}}
  [MemoryGiBPerVCpu](#cfn-ec2-launchtemplate-instancerequirements-memorygibpervcpu): {{
    MemoryGiBPerVCpu}}
  [MemoryMiB](#cfn-ec2-launchtemplate-instancerequirements-memorymib): {{
    MemoryMiB}}
  [NetworkBandwidthGbps](#cfn-ec2-launchtemplate-instancerequirements-networkbandwidthgbps): {{
    NetworkBandwidthGbps}}
  [NetworkInterfaceCount](#cfn-ec2-launchtemplate-instancerequirements-networkinterfacecount): {{
    NetworkInterfaceCount}}
  [OnDemandMaxPricePercentageOverLowestPrice](#cfn-ec2-launchtemplate-instancerequirements-ondemandmaxpricepercentageoverlowestprice): {{Integer}}
  [RequireHibernateSupport](#cfn-ec2-launchtemplate-instancerequirements-requirehibernatesupport): {{Boolean}}
  [SpotMaxPricePercentageOverLowestPrice](#cfn-ec2-launchtemplate-instancerequirements-spotmaxpricepercentageoverlowestprice): {{Integer}}
  [TotalLocalStorageGB](#cfn-ec2-launchtemplate-instancerequirements-totallocalstoragegb): {{
    TotalLocalStorageGB}}
  [VCpuCount](#cfn-ec2-launchtemplate-instancerequirements-vcpucount): {{
    VCpuCount}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-instancerequirements-properties"></a>

`AcceleratorCount`  <a name="cfn-ec2-launchtemplate-instancerequirements-acceleratorcount"></a>
The minimum and maximum number of accelerators (GPUs, FPGAs, or AWS Inferentia chips) on an instance.
To exclude accelerator-enabled instance types, set `Max` to `0`.
Default: No minimum or maximum limits
*Required*: No
*Type*: [AcceleratorCount](aws-properties-ec2-launchtemplate-acceleratorcount.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorManufacturers`  <a name="cfn-ec2-launchtemplate-instancerequirements-acceleratormanufacturers"></a>
Indicates whether instance types must have accelerators by specific manufacturers.
+ For instance types with AWS devices, specify `amazon-web-services`.
+ For instance types with AMD devices, specify `amd`.
+ For instance types with Habana devices, specify `habana`.
+ For instance types with NVIDIA devices, specify `nvidia`.
+ For instance types with Xilinx devices, specify `xilinx`.
Default: Any manufacturer
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorNames`  <a name="cfn-ec2-launchtemplate-instancerequirements-acceleratornames"></a>
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
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorTotalMemoryMiB`  <a name="cfn-ec2-launchtemplate-instancerequirements-acceleratortotalmemorymib"></a>
The minimum and maximum amount of total accelerator memory, in MiB.
Default: No minimum or maximum limits
*Required*: No
*Type*: [AcceleratorTotalMemoryMiB](aws-properties-ec2-launchtemplate-acceleratortotalmemorymib.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorTypes`  <a name="cfn-ec2-launchtemplate-instancerequirements-acceleratortypes"></a>
The accelerator types that must be on the instance type.
+ For instance types with FPGA accelerators, specify `fpga`.
+ For instance types with GPU accelerators, specify `gpu`.
+ For instance types with Inference accelerators, specify `inference`.
+ For instance types with Media accelerators, specify `media`.
Default: Any accelerator type
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedInstanceTypes`  <a name="cfn-ec2-launchtemplate-instancerequirements-allowedinstancetypes"></a>
The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.
You can use strings with one or more wild cards, represented by an asterisk (`*`), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge`, `c5*.*`, `m5a.*`, `r*`, `*3*`.
For example, if you specify `c5*`,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*`, Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.
If you specify `AllowedInstanceTypes`, you can't specify `ExcludedInstanceTypes`.
Default: All instance types
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BareMetal`  <a name="cfn-ec2-launchtemplate-instancerequirements-baremetal"></a>
Indicates whether bare metal instance types must be included, excluded, or required.
+ To include bare metal instance types, specify `included`.
+ To require only bare metal instance types, specify `required`.
+ To exclude bare metal instance types, specify `excluded`.
Default: `excluded`
*Required*: No
*Type*: String
*Allowed values*: `included | required | excluded`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaselineEbsBandwidthMbps`  <a name="cfn-ec2-launchtemplate-instancerequirements-baselineebsbandwidthmbps"></a>
The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide*.
Default: No minimum or maximum limits
*Required*: No
*Type*: [BaselineEbsBandwidthMbps](aws-properties-ec2-launchtemplate-baselineebsbandwidthmbps.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaselinePerformanceFactors`  <a name="cfn-ec2-launchtemplate-instancerequirements-baselineperformancefactors"></a>
The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see [Performance protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: [BaselinePerformanceFactors](aws-properties-ec2-launchtemplate-baselineperformancefactors.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BurstablePerformance`  <a name="cfn-ec2-launchtemplate-instancerequirements-burstableperformance"></a>
Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html).
+ To include burstable performance instance types, specify `included`.
+ To require only burstable performance instance types, specify `required`.
+ To exclude burstable performance instance types, specify `excluded`.
Default: `excluded`
*Required*: No
*Type*: String
*Allowed values*: `included | required | excluded`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CpuManufacturers`  <a name="cfn-ec2-launchtemplate-instancerequirements-cpumanufacturers"></a>
The CPU manufacturers to include.
+ For instance types with Intel CPUs, specify `intel`.
+ For instance types with AMD CPUs, specify `amd`.
+ For instance types with AWS CPUs, specify `amazon-web-services`.
+ For instance types with Apple CPUs, specify `apple`.
Don't confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.
Default: Any manufacturer
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludedInstanceTypes`  <a name="cfn-ec2-launchtemplate-instancerequirements-excludedinstancetypes"></a>
The instance types to exclude.
You can use strings with one or more wild cards, represented by an asterisk (`*`), to exclude an instance type, size, or generation. The following are examples: `m5.8xlarge`, `c5*.*`, `m5a.*`, `r*`, `*3*`.
For example, if you specify `c5*`,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*`, Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.
If you specify `ExcludedInstanceTypes`, you can't specify `AllowedInstanceTypes`.
Default: No excluded instance types
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceGenerations`  <a name="cfn-ec2-launchtemplate-instancerequirements-instancegenerations"></a>
Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*.
For current generation instance types, specify `current`.
For previous generation instance types, specify `previous`.
Default: Current and previous generation instance types
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalStorage`  <a name="cfn-ec2-launchtemplate-instancerequirements-localstorage"></a>
Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide*.
+ To include instance types with instance store volumes, specify `included`.
+ To require only instance types with instance store volumes, specify `required`.
+ To exclude instance types with instance store volumes, specify `excluded`.
Default: `included`
*Required*: No
*Type*: String
*Allowed values*: `included | required | excluded`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalStorageTypes`  <a name="cfn-ec2-launchtemplate-instancerequirements-localstoragetypes"></a>
The type of local storage that is required.
+ For instance types with hard disk drive (HDD) storage, specify `hdd`.
+ For instance types with solid state drive (SSD) storage, specify `ssd`.
Default: `hdd` and `ssd`
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxSpotPriceAsPercentageOfOptimalOnDemandPrice`  <a name="cfn-ec2-launchtemplate-instancerequirements-maxspotpriceaspercentageofoptimalondemandprice"></a>
[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib`, the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.
Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you don't specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryGiBPerVCpu`  <a name="cfn-ec2-launchtemplate-instancerequirements-memorygibpervcpu"></a>
The minimum and maximum amount of memory per vCPU, in GiB.
Default: No minimum or maximum limits
*Required*: No
*Type*: [MemoryGiBPerVCpu](aws-properties-ec2-launchtemplate-memorygibpervcpu.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryMiB`  <a name="cfn-ec2-launchtemplate-instancerequirements-memorymib"></a>
The minimum and maximum amount of memory, in MiB.
*Required*: No
*Type*: [MemoryMiB](aws-properties-ec2-launchtemplate-memorymib.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkBandwidthGbps`  <a name="cfn-ec2-launchtemplate-instancerequirements-networkbandwidthgbps"></a>
The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).
Default: No minimum or maximum limits
*Required*: No
*Type*: [NetworkBandwidthGbps](aws-properties-ec2-launchtemplate-networkbandwidthgbps.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaceCount`  <a name="cfn-ec2-launchtemplate-instancerequirements-networkinterfacecount"></a>
The minimum and maximum number of network interfaces.
Default: No minimum or maximum limits
*Required*: No
*Type*: [NetworkInterfaceCount](aws-properties-ec2-launchtemplate-networkinterfacecount.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnDemandMaxPricePercentageOverLowestPrice`  <a name="cfn-ec2-launchtemplate-instancerequirements-ondemandmaxpricepercentageoverlowestprice"></a>
[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
To turn off price protection, specify a high value, such as `999999`.
This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html).
If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib`, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.
Default: `20`
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequireHibernateSupport`  <a name="cfn-ec2-launchtemplate-instancerequirements-requirehibernatesupport"></a>
Indicates whether instance types must support hibernation for On-Demand Instances.
This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html).
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpotMaxPricePercentageOverLowestPrice`  <a name="cfn-ec2-launchtemplate-instancerequirements-spotmaxpricepercentageoverlowestprice"></a>
[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.
The parameter accepts an integer, which Amazon EC2 interprets as a percentage.
If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib`, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.
This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html).
Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you don't specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999`.
Default: `100`
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalLocalStorageGB`  <a name="cfn-ec2-launchtemplate-instancerequirements-totallocalstoragegb"></a>
The minimum and maximum amount of total local storage, in GB.
Default: No minimum or maximum limits
*Required*: No
*Type*: [TotalLocalStorageGB](aws-properties-ec2-launchtemplate-totallocalstoragegb.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VCpuCount`  <a name="cfn-ec2-launchtemplate-instancerequirements-vcpucount"></a>
The minimum and maximum number of vCPUs.
*Required*: No
*Type*: [VCpuCount](aws-properties-ec2-launchtemplate-vcpucount.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
