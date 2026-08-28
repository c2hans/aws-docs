---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-customermanagedworkercapabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet CustomerManagedWorkerCapabilities
<a name="aws-properties-deadline-fleet-customermanagedworkercapabilities"></a>

The worker capabilities for a customer managed workflow.

## Syntax
<a name="aws-properties-deadline-fleet-customermanagedworkercapabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-customermanagedworkercapabilities-syntax.json"></a>

```
{
  "[AcceleratorCount](#cfn-deadline-fleet-customermanagedworkercapabilities-acceleratorcount)" : {{AcceleratorCountRange}},
  "[AcceleratorTotalMemoryMiB](#cfn-deadline-fleet-customermanagedworkercapabilities-acceleratortotalmemorymib)" : {{AcceleratorTotalMemoryMiBRange}},
  "[AcceleratorTypes](#cfn-deadline-fleet-customermanagedworkercapabilities-acceleratortypes)" : {{[ String, ... ]}},
  "[CpuArchitectureType](#cfn-deadline-fleet-customermanagedworkercapabilities-cpuarchitecturetype)" : {{String}},
  "[CustomAmounts](#cfn-deadline-fleet-customermanagedworkercapabilities-customamounts)" : {{[ FleetAmountCapability, ... ]}},
  "[CustomAttributes](#cfn-deadline-fleet-customermanagedworkercapabilities-customattributes)" : {{[ FleetAttributeCapability, ... ]}},
  "[MemoryMiB](#cfn-deadline-fleet-customermanagedworkercapabilities-memorymib)" : {{MemoryMiBRange}},
  "[OsFamily](#cfn-deadline-fleet-customermanagedworkercapabilities-osfamily)" : {{String}},
  "[VCpuCount](#cfn-deadline-fleet-customermanagedworkercapabilities-vcpucount)" : {{VCpuCountRange}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-customermanagedworkercapabilities-syntax.yaml"></a>

```
  [AcceleratorCount](#cfn-deadline-fleet-customermanagedworkercapabilities-acceleratorcount): {{
    AcceleratorCountRange}}
  [AcceleratorTotalMemoryMiB](#cfn-deadline-fleet-customermanagedworkercapabilities-acceleratortotalmemorymib): {{
    AcceleratorTotalMemoryMiBRange}}
  [AcceleratorTypes](#cfn-deadline-fleet-customermanagedworkercapabilities-acceleratortypes): {{
    - String}}
  [CpuArchitectureType](#cfn-deadline-fleet-customermanagedworkercapabilities-cpuarchitecturetype): {{String}}
  [CustomAmounts](#cfn-deadline-fleet-customermanagedworkercapabilities-customamounts): {{
    - FleetAmountCapability}}
  [CustomAttributes](#cfn-deadline-fleet-customermanagedworkercapabilities-customattributes): {{
    - FleetAttributeCapability}}
  [MemoryMiB](#cfn-deadline-fleet-customermanagedworkercapabilities-memorymib): {{
    MemoryMiBRange}}
  [OsFamily](#cfn-deadline-fleet-customermanagedworkercapabilities-osfamily): {{String}}
  [VCpuCount](#cfn-deadline-fleet-customermanagedworkercapabilities-vcpucount): {{
    VCpuCountRange}}
```

## Properties
<a name="aws-properties-deadline-fleet-customermanagedworkercapabilities-properties"></a>

`AcceleratorCount`  <a name="cfn-deadline-fleet-customermanagedworkercapabilities-acceleratorcount"></a>
The range of the accelerator.
*Required*: No
*Type*: [AcceleratorCountRange](aws-properties-deadline-fleet-acceleratorcountrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorTotalMemoryMiB`  <a name="cfn-deadline-fleet-customermanagedworkercapabilities-acceleratortotalmemorymib"></a>
The total memory (MiB) for the customer managed worker capabilities.
*Required*: No
*Type*: [AcceleratorTotalMemoryMiBRange](aws-properties-deadline-fleet-acceleratortotalmemorymibrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AcceleratorTypes`  <a name="cfn-deadline-fleet-customermanagedworkercapabilities-acceleratortypes"></a>
The accelerator types for the customer managed worker capabilities.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CpuArchitectureType`  <a name="cfn-deadline-fleet-customermanagedworkercapabilities-cpuarchitecturetype"></a>
The CPU architecture type for the customer managed worker capabilities.
*Required*: Yes
*Type*: String
*Allowed values*: `x86_64 | arm64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAmounts`  <a name="cfn-deadline-fleet-customermanagedworkercapabilities-customamounts"></a>
Custom requirement ranges for customer managed worker capabilities.
*Required*: No
*Type*: Array of [FleetAmountCapability](aws-properties-deadline-fleet-fleetamountcapability.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAttributes`  <a name="cfn-deadline-fleet-customermanagedworkercapabilities-customattributes"></a>
Custom attributes for the customer manged worker capabilities.
*Required*: No
*Type*: Array of [FleetAttributeCapability](aws-properties-deadline-fleet-fleetattributecapability.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryMiB`  <a name="cfn-deadline-fleet-customermanagedworkercapabilities-memorymib"></a>
The memory (MiB).
*Required*: Yes
*Type*: [MemoryMiBRange](aws-properties-deadline-fleet-memorymibrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OsFamily`  <a name="cfn-deadline-fleet-customermanagedworkercapabilities-osfamily"></a>
The operating system (OS) family.
*Required*: Yes
*Type*: String
*Allowed values*: `WINDOWS | LINUX | MACOS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VCpuCount`  <a name="cfn-deadline-fleet-customermanagedworkercapabilities-vcpucount"></a>
The vCPU count for the customer manged worker capabilities.
*Required*: Yes
*Type*: [VCpuCountRange](aws-properties-deadline-fleet-vcpucountrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
