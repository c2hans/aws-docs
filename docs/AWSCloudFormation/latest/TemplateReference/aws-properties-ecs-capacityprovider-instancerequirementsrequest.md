---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-instancerequirementsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider InstanceRequirementsRequest
<a name="aws-properties-ecs-capacityprovider-instancerequirementsrequest"></a>

The instance requirements for attribute-based instance type selection. Instead of specifying exact instance types, you define requirements such as vCPU count, memory size, network performance, and accelerator specifications. Amazon ECS automatically selects Amazon EC2 instance types that match these requirements, providing flexibility and helping to mitigate capacity constraints.

## Syntax
<a name="aws-properties-ecs-capacityprovider-instancerequirementsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-instancerequirementsrequest-syntax.json"></a>

```
{
  "[AcceleratorCount](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratorcount)" : {{AcceleratorCountRequest}},
  "[AcceleratorManufacturers](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratormanufacturers)" : {{[ String, ... ]}},
  "[AcceleratorNames](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratornames)" : {{[ String, ... ]}},
  "[AcceleratorTotalMemoryMiB](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratortotalmemorymib)" : {{AcceleratorTotalMemoryMiBRequest}},
  "[AcceleratorTypes](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratortypes)" : {{[ String, ... ]}},
  "[AllowedInstanceTypes](#cfn-ecs-capacityprovider-instancerequirementsrequest-allowedinstancetypes)" : {{[ String, ... ]}},
  "[BareMetal](#cfn-ecs-capacityprovider-instancerequirementsrequest-baremetal)" : {{String}},
  "[BaselineEbsBandwidthMbps](#cfn-ecs-capacityprovider-instancerequirementsrequest-baselineebsbandwidthmbps)" : {{BaselineEbsBandwidthMbpsRequest}},
  "[BurstablePerformance](#cfn-ecs-capacityprovider-instancerequirementsrequest-burstableperformance)" : {{String}},
  "[CpuManufacturers](#cfn-ecs-capacityprovider-instancerequirementsrequest-cpumanufacturers)" : {{[ String, ... ]}},
  "[ExcludedInstanceTypes](#cfn-ecs-capacityprovider-instancerequirementsrequest-excludedinstancetypes)" : {{[ String, ... ]}},
  "[InstanceGenerations](#cfn-ecs-capacityprovider-instancerequirementsrequest-instancegenerations)" : {{[ String, ... ]}},
  "[LocalStorage](#cfn-ecs-capacityprovider-instancerequirementsrequest-localstorage)" : {{String}},
  "[LocalStorageTypes](#cfn-ecs-capacityprovider-instancerequirementsrequest-localstoragetypes)" : {{[ String, ... ]}},
  "[MaxSpotPriceAsPercentageOfOptimalOnDemandPrice](#cfn-ecs-capacityprovider-instancerequirementsrequest-maxspotpriceaspercentageofoptimalondemandprice)" : {{Integer}},
  "[MemoryGiBPerVCpu](#cfn-ecs-capacityprovider-instancerequirementsrequest-memorygibpervcpu)" : {{MemoryGiBPerVCpuRequest}},
  "[MemoryMiB](#cfn-ecs-capacityprovider-instancerequirementsrequest-memorymib)" : {{MemoryMiBRequest}},
  "[NetworkBandwidthGbps](#cfn-ecs-capacityprovider-instancerequirementsrequest-networkbandwidthgbps)" : {{NetworkBandwidthGbpsRequest}},
  "[NetworkInterfaceCount](#cfn-ecs-capacityprovider-instancerequirementsrequest-networkinterfacecount)" : {{NetworkInterfaceCountRequest}},
  "[OnDemandMaxPricePercentageOverLowestPrice](#cfn-ecs-capacityprovider-instancerequirementsrequest-ondemandmaxpricepercentageoverlowestprice)" : {{Integer}},
  "[RequireHibernateSupport](#cfn-ecs-capacityprovider-instancerequirementsrequest-requirehibernatesupport)" : {{Boolean}},
  "[SpotMaxPricePercentageOverLowestPrice](#cfn-ecs-capacityprovider-instancerequirementsrequest-spotmaxpricepercentageoverlowestprice)" : {{Integer}},
  "[TotalLocalStorageGB](#cfn-ecs-capacityprovider-instancerequirementsrequest-totallocalstoragegb)" : {{TotalLocalStorageGBRequest}},
  "[VCpuCount](#cfn-ecs-capacityprovider-instancerequirementsrequest-vcpucount)" : {{VCpuCountRangeRequest}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-instancerequirementsrequest-syntax.yaml"></a>

```
  [AcceleratorCount](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratorcount): {{
    AcceleratorCountRequest}}
  [AcceleratorManufacturers](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratormanufacturers): {{
    - String}}
  [AcceleratorNames](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratornames): {{
    - String}}
  [AcceleratorTotalMemoryMiB](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratortotalmemorymib): {{
    AcceleratorTotalMemoryMiBRequest}}
  [AcceleratorTypes](#cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratortypes): {{
    - String}}
  [AllowedInstanceTypes](#cfn-ecs-capacityprovider-instancerequirementsrequest-allowedinstancetypes): {{
    - String}}
  [BareMetal](#cfn-ecs-capacityprovider-instancerequirementsrequest-baremetal): {{String}}
  [BaselineEbsBandwidthMbps](#cfn-ecs-capacityprovider-instancerequirementsrequest-baselineebsbandwidthmbps): {{
    BaselineEbsBandwidthMbpsRequest}}
  [BurstablePerformance](#cfn-ecs-capacityprovider-instancerequirementsrequest-burstableperformance): {{String}}
  [CpuManufacturers](#cfn-ecs-capacityprovider-instancerequirementsrequest-cpumanufacturers): {{
    - String}}
  [ExcludedInstanceTypes](#cfn-ecs-capacityprovider-instancerequirementsrequest-excludedinstancetypes): {{
    - String}}
  [InstanceGenerations](#cfn-ecs-capacityprovider-instancerequirementsrequest-instancegenerations): {{
    - String}}
  [LocalStorage](#cfn-ecs-capacityprovider-instancerequirementsrequest-localstorage): {{String}}
  [LocalStorageTypes](#cfn-ecs-capacityprovider-instancerequirementsrequest-localstoragetypes): {{
    - String}}
  [MaxSpotPriceAsPercentageOfOptimalOnDemandPrice](#cfn-ecs-capacityprovider-instancerequirementsrequest-maxspotpriceaspercentageofoptimalondemandprice): {{Integer}}
  [MemoryGiBPerVCpu](#cfn-ecs-capacityprovider-instancerequirementsrequest-memorygibpervcpu): {{
    MemoryGiBPerVCpuRequest}}
  [MemoryMiB](#cfn-ecs-capacityprovider-instancerequirementsrequest-memorymib): {{
    MemoryMiBRequest}}
  [NetworkBandwidthGbps](#cfn-ecs-capacityprovider-instancerequirementsrequest-networkbandwidthgbps): {{
    NetworkBandwidthGbpsRequest}}
  [NetworkInterfaceCount](#cfn-ecs-capacityprovider-instancerequirementsrequest-networkinterfacecount): {{
    NetworkInterfaceCountRequest}}
  [OnDemandMaxPricePercentageOverLowestPrice](#cfn-ecs-capacityprovider-instancerequirementsrequest-ondemandmaxpricepercentageoverlowestprice): {{Integer}}
  [RequireHibernateSupport](#cfn-ecs-capacityprovider-instancerequirementsrequest-requirehibernatesupport): {{Boolean}}
  [SpotMaxPricePercentageOverLowestPrice](#cfn-ecs-capacityprovider-instancerequirementsrequest-spotmaxpricepercentageoverlowestprice): {{Integer}}
  [TotalLocalStorageGB](#cfn-ecs-capacityprovider-instancerequirementsrequest-totallocalstoragegb): {{
    TotalLocalStorageGBRequest}}
  [VCpuCount](#cfn-ecs-capacityprovider-instancerequirementsrequest-vcpucount): {{
    VCpuCountRangeRequest}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-instancerequirementsrequest-properties"></a>

`AcceleratorCount`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratorcount"></a>
The minimum and maximum number of accelerators for the instance types. This is used when you need instances with specific numbers of GPUs or other accelerators.
*Required*: No
*Type*: [AcceleratorCountRequest](aws-properties-ecs-capacityprovider-acceleratorcountrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorManufacturers`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratormanufacturers"></a>
The accelerator manufacturers to include. You can specify `nvidia`, `amd`, `amazon-web-services`, or `xilinx` depending on your accelerator requirements.
*Required*: No
*Type*: Array of String
*Allowed values*: `amazon-web-services | amd | habana | nvidia | xilinx`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorNames`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratornames"></a>
The specific accelerator names to include. For example, you can specify `a100`, `v100`, `k80`, or other specific accelerator models.
*Required*: No
*Type*: Array of String
*Allowed values*: `a10g | a100 | h100 | inferentia | k520 | k80 | m60 | radeon-pro-v520 | t4 | t4g | vu9p | v100 | l40s | l4 | gaudi-hl-205 | inferentia2 | trainium | trainium2 | u30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorTotalMemoryMiB`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratortotalmemorymib"></a>
The minimum and maximum total accelerator memory in mebibytes (MiB). This is important for GPU workloads that require specific amounts of video memory.
*Required*: No
*Type*: [AcceleratorTotalMemoryMiBRequest](aws-properties-ecs-capacityprovider-acceleratortotalmemorymibrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorTypes`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-acceleratortypes"></a>
The accelerator types to include. You can specify `gpu` for graphics processing units, `fpga` for field programmable gate arrays, or `inference` for machine learning inference accelerators.
*Required*: No
*Type*: Array of String
*Allowed values*: `gpu | fpga | inference`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedInstanceTypes`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-allowedinstancetypes"></a>
The instance types to include in the selection. When specified, Amazon ECS only considers these instance types, subject to the other requirements specified.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BareMetal`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-baremetal"></a>
Indicates whether to include bare metal instance types. Set to `included` to allow bare metal instances, `excluded` to exclude them, or `required` to use only bare metal instances.
*Required*: No
*Type*: String
*Allowed values*: `included | required | excluded`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaselineEbsBandwidthMbps`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-baselineebsbandwidthmbps"></a>
The minimum and maximum baseline Amazon EBS bandwidth in megabits per second (Mbps). This is important for workloads with high storage I/O requirements.
*Required*: No
*Type*: [BaselineEbsBandwidthMbpsRequest](aws-properties-ecs-capacityprovider-baselineebsbandwidthmbpsrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BurstablePerformance`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-burstableperformance"></a>
Indicates whether to include burstable performance instance types (T2, T3, T3a, T4g). Set to `included` to allow burstable instances, `excluded` to exclude them, or `required` to use only burstable instances.
*Required*: No
*Type*: String
*Allowed values*: `included | required | excluded`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CpuManufacturers`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-cpumanufacturers"></a>
The CPU manufacturers to include or exclude. You can specify `intel`, `amd`, or `amazon-web-services` to control which CPU types are used for your workloads.
*Required*: No
*Type*: Array of String
*Allowed values*: `intel | amd | amazon-web-services`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludedInstanceTypes`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-excludedinstancetypes"></a>
The instance types to exclude from selection. Use this to prevent Amazon ECS from selecting specific instance types that may not be suitable for your workloads.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceGenerations`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-instancegenerations"></a>
The instance generations to include. You can specify `current` to use the latest generation instances, or `previous` to include previous generation instances for cost optimization.
*Required*: No
*Type*: Array of String
*Allowed values*: `current | previous`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalStorage`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-localstorage"></a>
Indicates whether to include instance types with local storage. Set to `included` to allow local storage, `excluded` to exclude it, or `required` to use only instances with local storage.
*Required*: No
*Type*: String
*Allowed values*: `included | required | excluded`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalStorageTypes`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-localstoragetypes"></a>
The local storage types to include. You can specify `hdd` for hard disk drives, `ssd` for solid state drives, or both.
*Required*: No
*Type*: Array of String
*Allowed values*: `hdd | ssd`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxSpotPriceAsPercentageOfOptimalOnDemandPrice`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-maxspotpriceaspercentageofoptimalondemandprice"></a>
The maximum price for Spot instances as a percentage of the optimal On-Demand price. This provides more precise cost control for Spot instance selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryGiBPerVCpu`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-memorygibpervcpu"></a>
The minimum and maximum amount of memory per vCPU in gibibytes (GiB). This helps ensure that instance types have the appropriate memory-to-CPU ratio for your workloads.
*Required*: No
*Type*: [MemoryGiBPerVCpuRequest](aws-properties-ecs-capacityprovider-memorygibpervcpurequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryMiB`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-memorymib"></a>
The minimum and maximum amount of memory in mebibytes (MiB) for the instance types. Amazon ECS selects instance types that have memory within this range.
*Required*: Yes
*Type*: [MemoryMiBRequest](aws-properties-ecs-capacityprovider-memorymibrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkBandwidthGbps`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-networkbandwidthgbps"></a>
The minimum and maximum network bandwidth in gigabits per second (Gbps). This is crucial for network-intensive workloads that require high throughput.
*Required*: No
*Type*: [NetworkBandwidthGbpsRequest](aws-properties-ecs-capacityprovider-networkbandwidthgbpsrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaceCount`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-networkinterfacecount"></a>
The minimum and maximum number of network interfaces for the instance types. This is useful for workloads that require multiple network interfaces.
*Required*: No
*Type*: [NetworkInterfaceCountRequest](aws-properties-ecs-capacityprovider-networkinterfacecountrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnDemandMaxPricePercentageOverLowestPrice`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-ondemandmaxpricepercentageoverlowestprice"></a>
The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon ECS selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequireHibernateSupport`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-requirehibernatesupport"></a>
Indicates whether the instance types must support hibernation. When set to `true`, only instance types that support hibernation are selected.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpotMaxPricePercentageOverLowestPrice`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-spotmaxpricepercentageoverlowestprice"></a>
The maximum price for Spot instances as a percentage over the lowest priced On-Demand instance. This helps control Spot instance costs while maintaining access to capacity.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalLocalStorageGB`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-totallocalstoragegb"></a>
The minimum and maximum total local storage in gigabytes (GB) for instance types with local storage.
*Required*: No
*Type*: [TotalLocalStorageGBRequest](aws-properties-ecs-capacityprovider-totallocalstoragegbrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VCpuCount`  <a name="cfn-ecs-capacityprovider-instancerequirementsrequest-vcpucount"></a>
The minimum and maximum number of vCPUs for the instance types. Amazon ECS selects instance types that have vCPU counts within this range.
*Required*: Yes
*Type*: [VCpuCountRangeRequest](aws-properties-ecs-capacityprovider-vcpucountrangerequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
