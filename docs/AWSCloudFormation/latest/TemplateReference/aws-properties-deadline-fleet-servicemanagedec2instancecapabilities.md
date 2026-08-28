---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-servicemanagedec2instancecapabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet ServiceManagedEc2InstanceCapabilities
<a name="aws-properties-deadline-fleet-servicemanagedec2instancecapabilities"></a>

The Amazon EC2 instance capabilities.

## Syntax
<a name="aws-properties-deadline-fleet-servicemanagedec2instancecapabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-servicemanagedec2instancecapabilities-syntax.json"></a>

```
{
  "[AcceleratorCapabilities](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-acceleratorcapabilities)" : {{AcceleratorCapabilities}},
  "[AllowedInstanceTypes](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-allowedinstancetypes)" : {{[ String, ... ]}},
  "[CpuArchitectureType](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-cpuarchitecturetype)" : {{String}},
  "[CustomAmounts](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-customamounts)" : {{[ FleetAmountCapability, ... ]}},
  "[CustomAttributes](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-customattributes)" : {{[ FleetAttributeCapability, ... ]}},
  "[ExcludedInstanceTypes](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-excludedinstancetypes)" : {{[ String, ... ]}},
  "[MemoryMiB](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-memorymib)" : {{MemoryMiBRange}},
  "[OsFamily](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-osfamily)" : {{String}},
  "[RootEbsVolume](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-rootebsvolume)" : {{Ec2EbsVolume}},
  "[VCpuCount](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-vcpucount)" : {{VCpuCountRange}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-servicemanagedec2instancecapabilities-syntax.yaml"></a>

```
  [AcceleratorCapabilities](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-acceleratorcapabilities): {{
    AcceleratorCapabilities}}
  [AllowedInstanceTypes](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-allowedinstancetypes): {{
    - String}}
  [CpuArchitectureType](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-cpuarchitecturetype): {{String}}
  [CustomAmounts](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-customamounts): {{
    - FleetAmountCapability}}
  [CustomAttributes](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-customattributes): {{
    - FleetAttributeCapability}}
  [ExcludedInstanceTypes](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-excludedinstancetypes): {{
    - String}}
  [MemoryMiB](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-memorymib): {{
    MemoryMiBRange}}
  [OsFamily](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-osfamily): {{String}}
  [RootEbsVolume](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-rootebsvolume): {{
    Ec2EbsVolume}}
  [VCpuCount](#cfn-deadline-fleet-servicemanagedec2instancecapabilities-vcpucount): {{
    VCpuCountRange}}
```

## Properties
<a name="aws-properties-deadline-fleet-servicemanagedec2instancecapabilities-properties"></a>

`AcceleratorCapabilities`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-acceleratorcapabilities"></a>
Describes the GPU accelerator capabilities required for worker host instances in this fleet.
*Required*: No
*Type*: [AcceleratorCapabilities](aws-properties-deadline-fleet-acceleratorcapabilities.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedInstanceTypes`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-allowedinstancetypes"></a>
The allowable Amazon EC2 instance types.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CpuArchitectureType`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-cpuarchitecturetype"></a>
The CPU architecture type.
*Required*: Yes
*Type*: String
*Allowed values*: `x86_64 | arm64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAmounts`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-customamounts"></a>
The custom capability amounts to require for instances in this fleet.
*Required*: No
*Type*: Array of [FleetAmountCapability](aws-properties-deadline-fleet-fleetamountcapability.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAttributes`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-customattributes"></a>
The custom capability attributes to require for instances in this fleet.
*Required*: No
*Type*: Array of [FleetAttributeCapability](aws-properties-deadline-fleet-fleetattributecapability.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludedInstanceTypes`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-excludedinstancetypes"></a>
The instance types to exclude from the fleet.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `100 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryMiB`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-memorymib"></a>
The memory, as MiB, for the Amazon EC2 instance type.
*Required*: Yes
*Type*: [MemoryMiBRange](aws-properties-deadline-fleet-memorymibrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OsFamily`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-osfamily"></a>
The operating system (OS) family.
*Required*: Yes
*Type*: String
*Allowed values*: `LINUX | WINDOWS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RootEbsVolume`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-rootebsvolume"></a>
The root EBS volume.
*Required*: No
*Type*: [Ec2EbsVolume](aws-properties-deadline-fleet-ec2ebsvolume.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VCpuCount`  <a name="cfn-deadline-fleet-servicemanagedec2instancecapabilities-vcpucount"></a>
The amount of vCPU to require for instances in this fleet.
*Required*: Yes
*Type*: [VCpuCountRange](aws-properties-deadline-fleet-vcpucountrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
