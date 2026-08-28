---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InstanceRequirementsRequest.html
---

# InstanceRequirementsRequest
<a name="API_InstanceRequirementsRequest"></a>

The instance requirements for attribute-based instance type selection. Instead of specifying exact instance types, you define requirements such as vCPU count, memory size, network performance, and accelerator specifications. Amazon ECS automatically selects Amazon EC2 instance types that match these requirements, providing flexibility and helping to mitigate capacity constraints.

## Contents
<a name="API_InstanceRequirementsRequest_Contents"></a>

 ** memoryMiB **   <a name="ECS-Type-InstanceRequirementsRequest-memoryMiB"></a>
The minimum and maximum amount of memory in mebibytes (MiB) for the instance types. Amazon ECS selects instance types that have memory within this range.
Type: [MemoryMiBRequest](API_MemoryMiBRequest.md) object
Required: Yes

 ** vCpuCount **   <a name="ECS-Type-InstanceRequirementsRequest-vCpuCount"></a>
The minimum and maximum number of vCPUs for the instance types. Amazon ECS selects instance types that have vCPU counts within this range.
Type: [VCpuCountRangeRequest](API_VCpuCountRangeRequest.md) object
Required: Yes

 ** acceleratorCount **   <a name="ECS-Type-InstanceRequirementsRequest-acceleratorCount"></a>
The minimum and maximum number of accelerators for the instance types. This is used when you need instances with specific numbers of GPUs or other accelerators.
Type: [AcceleratorCountRequest](API_AcceleratorCountRequest.md) object
Required: No

 ** acceleratorManufacturers **   <a name="ECS-Type-InstanceRequirementsRequest-acceleratorManufacturers"></a>
The accelerator manufacturers to include. You can specify `nvidia`, `amd`, `amazon-web-services`, or `xilinx` depending on your accelerator requirements.
Type: Array of strings
Valid Values: `amazon-web-services | amd | nvidia | xilinx | habana`
Required: No

 ** acceleratorNames **   <a name="ECS-Type-InstanceRequirementsRequest-acceleratorNames"></a>
The specific accelerator names to include. For example, you can specify `a100`, `v100`, `k80`, or other specific accelerator models.
Type: Array of strings
Valid Values: `a100 | inferentia | k520 | k80 | m60 | radeon-pro-v520 | t4 | vu9p | v100 | a10g | h100 | t4g`
Required: No

 ** acceleratorTotalMemoryMiB **   <a name="ECS-Type-InstanceRequirementsRequest-acceleratorTotalMemoryMiB"></a>
The minimum and maximum total accelerator memory in mebibytes (MiB). This is important for GPU workloads that require specific amounts of video memory.
Type: [AcceleratorTotalMemoryMiBRequest](API_AcceleratorTotalMemoryMiBRequest.md) object
Required: No

 ** acceleratorTypes **   <a name="ECS-Type-InstanceRequirementsRequest-acceleratorTypes"></a>
The accelerator types to include. You can specify `gpu` for graphics processing units, `fpga` for field programmable gate arrays, or `inference` for machine learning inference accelerators.
Type: Array of strings
Valid Values: `gpu | fpga | inference`
Required: No

 ** allowedInstanceTypes **   <a name="ECS-Type-InstanceRequirementsRequest-allowedInstanceTypes"></a>
The instance types to include in the selection. When specified, Amazon ECS only considers these instance types, subject to the other requirements specified.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\*\-]+`
Required: No

 ** bareMetal **   <a name="ECS-Type-InstanceRequirementsRequest-bareMetal"></a>
Indicates whether to include bare metal instance types. Set to `included` to allow bare metal instances, `excluded` to exclude them, or `required` to use only bare metal instances.
Type: String
Valid Values: `included | required | excluded`
Required: No

 ** baselineEbsBandwidthMbps **   <a name="ECS-Type-InstanceRequirementsRequest-baselineEbsBandwidthMbps"></a>
The minimum and maximum baseline Amazon EBS bandwidth in megabits per second (Mbps). This is important for workloads with high storage I/O requirements.
Type: [BaselineEbsBandwidthMbpsRequest](API_BaselineEbsBandwidthMbpsRequest.md) object
Required: No

 ** burstablePerformance **   <a name="ECS-Type-InstanceRequirementsRequest-burstablePerformance"></a>
Indicates whether to include burstable performance instance types (T2, T3, T3a, T4g). Set to `included` to allow burstable instances, `excluded` to exclude them, or `required` to use only burstable instances.
Type: String
Valid Values: `included | required | excluded`
Required: No

 ** cpuManufacturers **   <a name="ECS-Type-InstanceRequirementsRequest-cpuManufacturers"></a>
The CPU manufacturers to include or exclude. You can specify `intel`, `amd`, or `amazon-web-services` to control which CPU types are used for your workloads.
Type: Array of strings
Valid Values: `intel | amd | amazon-web-services`
Required: No

 ** excludedInstanceTypes **   <a name="ECS-Type-InstanceRequirementsRequest-excludedInstanceTypes"></a>
The instance types to exclude from selection. Use this to prevent Amazon ECS from selecting specific instance types that may not be suitable for your workloads.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\*\-]+`
Required: No

 ** instanceGenerations **   <a name="ECS-Type-InstanceRequirementsRequest-instanceGenerations"></a>
The instance generations to include. You can specify `current` to use the latest generation instances, or `previous` to include previous generation instances for cost optimization.
Type: Array of strings
Valid Values: `current | previous`
Required: No

 ** localStorage **   <a name="ECS-Type-InstanceRequirementsRequest-localStorage"></a>
Indicates whether to include instance types with local storage. Set to `included` to allow local storage, `excluded` to exclude it, or `required` to use only instances with local storage.
Type: String
Valid Values: `included | required | excluded`
Required: No

 ** localStorageTypes **   <a name="ECS-Type-InstanceRequirementsRequest-localStorageTypes"></a>
The local storage types to include. You can specify `hdd` for hard disk drives, `ssd` for solid state drives, or both.
Type: Array of strings
Valid Values: `hdd | ssd`
Required: No

 ** maxSpotPriceAsPercentageOfOptimalOnDemandPrice **   <a name="ECS-Type-InstanceRequirementsRequest-maxSpotPriceAsPercentageOfOptimalOnDemandPrice"></a>
The maximum price for Spot instances as a percentage of the optimal On-Demand price. This provides more precise cost control for Spot instance selection.
Type: Integer
Required: No

 ** memoryGiBPerVCpu **   <a name="ECS-Type-InstanceRequirementsRequest-memoryGiBPerVCpu"></a>
The minimum and maximum amount of memory per vCPU in gibibytes (GiB). This helps ensure that instance types have the appropriate memory-to-CPU ratio for your workloads.
Type: [MemoryGiBPerVCpuRequest](API_MemoryGiBPerVCpuRequest.md) object
Required: No

 ** networkBandwidthGbps **   <a name="ECS-Type-InstanceRequirementsRequest-networkBandwidthGbps"></a>
The minimum and maximum network bandwidth in gigabits per second (Gbps). This is crucial for network-intensive workloads that require high throughput.
Type: [NetworkBandwidthGbpsRequest](API_NetworkBandwidthGbpsRequest.md) object
Required: No

 ** networkInterfaceCount **   <a name="ECS-Type-InstanceRequirementsRequest-networkInterfaceCount"></a>
The minimum and maximum number of network interfaces for the instance types. This is useful for workloads that require multiple network interfaces.
Type: [NetworkInterfaceCountRequest](API_NetworkInterfaceCountRequest.md) object
Required: No

 ** onDemandMaxPricePercentageOverLowestPrice **   <a name="ECS-Type-InstanceRequirementsRequest-onDemandMaxPricePercentageOverLowestPrice"></a>
The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon ECS selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.
Type: Integer
Required: No

 ** requireHibernateSupport **   <a name="ECS-Type-InstanceRequirementsRequest-requireHibernateSupport"></a>
Indicates whether the instance types must support hibernation. When set to `true`, only instance types that support hibernation are selected.
Type: Boolean
Required: No

 ** spotMaxPricePercentageOverLowestPrice **   <a name="ECS-Type-InstanceRequirementsRequest-spotMaxPricePercentageOverLowestPrice"></a>
The maximum price for Spot instances as a percentage over the lowest priced On-Demand instance. This helps control Spot instance costs while maintaining access to capacity.
Type: Integer
Required: No

 ** totalLocalStorageGB **   <a name="ECS-Type-InstanceRequirementsRequest-totalLocalStorageGB"></a>
The minimum and maximum total local storage in gigabytes (GB) for instance types with local storage.
Type: [TotalLocalStorageGBRequest](API_TotalLocalStorageGBRequest.md) object
Required: No

## See Also
<a name="API_InstanceRequirementsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/InstanceRequirementsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/InstanceRequirementsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/InstanceRequirementsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
