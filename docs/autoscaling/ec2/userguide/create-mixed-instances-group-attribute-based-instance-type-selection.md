---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html
---

# Create mixed instances group using attribute-based instance type selection
<a name="create-mixed-instances-group-attribute-based-instance-type-selection"></a>

Instead of manually choosing instance types for your mixed instances group, you can specify a set of instance attributes that describe your compute requirements. As Amazon EC2 Auto Scaling launches instances, any instance types used by the Auto Scaling group must match your required instance attributes. This is known as *attribute-based instance type selection*.

This approach is ideal for workloads and frameworks that can be flexible about which instance types they use, such as containers, big data, and CI/CD.

The following are benefits of attribute-based instance type selection:
+ **Optimal flexibility for Spot Instances** – Amazon EC2 Auto Scaling can select from a wide range of instance types for launching Spot Instances. This meets the Spot best practice of being flexible about instance types, which gives the Amazon EC2 Spot service a better chance of finding and allocating your required amount of compute capacity.
+ **Easily use the right instance types** – With so many instance types available, finding the right instance types for your workload can be time consuming. When you specify instance attributes, the instance types will automatically have the required attributes for your workload.
+ **Automatic use of new instance types** – Your Auto Scaling groups can use newer generation instance types as they're released. Newer generation instance types are automatically used when they match your requirements and align with the allocation strategies you choose for your Auto Scaling group.

**Topics**
+ [How attribute-based instance type selection works](#how-attribute-based-instance-type-selection-works)
+ [Price protection](#understand-price-protection)
+ [Performance protection](#understand-performance-protection)
+ [Prerequisites](#attribute-based-instance-type-selection-prerequisites)
+ [Create a mixed instances group with attribute-based instance type selection (console)](#attribute-based-instance-type-selection-console)
+ [Create a mixed instances group with attribute-based instance type selection (AWS CLI)](#attribute-based-instance-type-selection-aws-cli)
+ [Example configuration](#attribute-based-instance-type-selection-example-configurations)
+ [Preview your instance types](#attribute-based-instance-type-selection-preview)
+ [Related resources](#attribute-based-instance-type-selection-related-resources)

## How attribute-based instance type selection works
<a name="how-attribute-based-instance-type-selection-works"></a>

With attribute-based instance type selection, instead of providing a list of specific instance types, you provide a list of instance attributes that your instances require, such as:
+ **vCPU count** – The minimum and maximum number of vCPUs per instance.
+ **Memory** – The minimum and maximum GiBs of memory per instance.
+ **Local storage** – Whether to use EBS or instance store volumes for local storage.
+ **Burstable performance** – Whether to use the T instance family, including T4g, T3a, T3, and T2 types.

There are many options available for defining your instance requirements. For a description of each option and the default values, see [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) in the *Amazon EC2 Auto Scaling API Reference*.

When your Auto Scaling group needs to launch an instance, it will search for instance types that match your specified attributes and are available in that Availability Zone. The allocation strategy then determines which of the matching instance types to launch. By default, attribute-based instance type selection has a price protection feature enabled to prevent your Auto Scaling group from launching instance types that exceed your budget thresholds.

By default, you use the number of instances as the unit of measurement when setting the desired capacity of your Auto Scaling group, meaning each instance counts as one unit.

Alternatively, you can set the value for desired capacity to the number of vCPUs or the amount of memory. To do so, use the **Desired capacity type** dropdown field in the AWS Management Console or the `DesiredCapacityType` property in the `CreateAutoScalingGroup` or `UpdateAutoScalingGroup` API operation. Amazon EC2 Auto Scaling then launches the number of instances required to meet the desired vCPU or memory capacity. For example, if you use vCPUs as the desired capacity type and use instances with 2 vCPUs each, a desired capacity of 10 vCPUs would launch 5 instances. This is a useful alternative to [instance weights](ec2-auto-scaling-mixed-instances-groups-instance-weighting.md).

## Price protection
<a name="understand-price-protection"></a>

With price protection, you can specify the maximum price you are willing to pay for EC2 instances launched by your Auto Scaling group. Price protection is a feature that prevents your Auto Scaling group from using instance types that you would consider too expensive even if they happen to fit the attributes that you specified.

Price protection is enabled by default and has separate price thresholds for On-Demand Instances and Spot Instances. When Amazon EC2 Auto Scaling needs to launch new instances, any instance types priced above the relevant threshold are not launched.

**Topics**
+ [On-Demand price protection](#on-demand-price-price-protection)
+ [Spot price protection](#spot-price-price-protection)
+ [Customize price protection](#customize-price-price-protection)

### On-Demand price protection
<a name="on-demand-price-price-protection"></a>

For On-Demand Instances, you define the maximum On-Demand price you're willing to pay as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes.

If an On-Demand price protection value is not explicitly defined, a default maximum On-Demand price of 20 percent higher than the identified On-Demand price will be used.

### Spot price protection
<a name="spot-price-price-protection"></a>

By default, Amazon EC2 Auto Scaling will automatically apply optimal Spot Instance price protection to consistently select from a wide range of instance types. You can also manually set the price protection yourself. However, letting Amazon EC2 Auto Scaling do it for you can improve the likelihood that your Spot capacity is fulfilled.

You can manually specify the price protection using one of the following options. If you manually set the price protection, we recommend using the first option.
+ **A percentage of an identified *On-Demand price*** – The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes.
+ **A percentage higher than an identified *Spot price*** – The identified Spot price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. We do not recommend using this option because Spot prices can fluctuate, and therefore your price protection threshold might also fluctuate.

### Customize price protection
<a name="customize-price-price-protection"></a>

You can customize the price protection thresholds in the Amazon EC2 Auto Scaling console or using the AWS CLI or SDKs.
+ In the console, use the **On-Demand price protection** and **Spot price protection** settings in **Additional instance attributes**.
+ In the [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) structure, to specify the On-Demand Instance price protection threshold, use the `OnDemandMaxPricePercentageOverLowestPrice` property. To specify the Spot Instance price protection threshold, use either the `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` or the `SpotMaxPricePercentageOverLowestPrice` property.

If you set **Desired capacity type** (`DesiredCapacityType`) to **vCPUs** or **Memory GiB**, the price protection applies based on the per vCPU or per memory price instead of the per instance price.

You can also turn off price protection. To indicate no price protection threshold, specify a high percentage value, such as `999999`.

**Note**
If no current generation C, M, or R instance types match your specified attributes, price protection is still applicable. When no match is found, the identified price is from the lowest priced current generation instance types, or failing that, the lowest priced previous generation instance types, that match your attributes.

## Performance protection
<a name="understand-performance-protection"></a>

*Performance protection* is a feature that ensures your Auto Scaling group uses instance types that are similar to or exceed a specified performance baseline. To use performance protection, you specify an instance family as a baseline reference. The capabilities of the specified instance family establish the lowest acceptable level of performance. When Auto Scaling selects instance types, it considers your specified attributes and the performance baseline. Instance types that fall below the performance baseline are automatically excluded from selection, even if they match your other specified attributes. This ensures that all selected instance types offer performance similar to or better than the baseline established by the specified instance family. Auto Scaling uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application.

Currently, this feature only supports CPU performance as a baseline performance factor. The CPU performance of the specified instance family serves as the performance baseline, ensuring that selected instance types are similar to or exceed this baseline. Instance families with the same CPU processors lead to the same filtering results, even if their network or disk performance differs. For example, specifying either `c6in` or `c6i` as the baseline reference would produce identical performance-based filtering results because both instance families use the same CPU processor.

**Unsupported instance families**
The following instance families are not supported for performance protection:
+ `c1`
+ `g3` \| `g3s`
+ `hpc7g`
+ `m1` \| `m2`
+ `mac1` \| `mac2` \| `mac2-m1ultra` \| `mac2-m2` \| `mac2-m2pro`
+ `p3dn` \| `p4d` \| `p5`
+ `t1`
+ `u-12tb1` \| `u-18tb1` \| `u-24tb1` \| `u-3tb1` \| `u-6tb1` \| `u-9tb1` \| `u7i-12tb` \| `u7in-16tb` \| `u7in-24tb` \| `u7in-32tb`

If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.

**Example: Set a CPU performance baseline**
In the following example, the instance requirement is to launch with instance types that have CPU cores that are as performant as the `c6i` instance family. This will filter out instance types with less performant CPU processors, even if they meet your other specified instance requirements such as the number of vCPUs. For example, if your specified instance attributes include 4 vCPUs and 16 GB of memory, an instance type with these attributes but with lower CPU performance than `c6i` will be excluded from selection.

```
"BaselinePerformanceFactors": {
        "Cpu": {
            "References": [
                {
                    "InstanceFamily": "c6i"
                }
            ]
        }
```

**Considerations**
Consider the following when using performance protection:
+ You can specify either instance types or instance attributes, but not both at the same time.
+ You can specify a maximum of four `InstanceRequirements` structures in a request configuration.

## Prerequisites
<a name="attribute-based-instance-type-selection-prerequisites"></a>
+ Create a launch template. For more information, see [Create a launch template for an Auto Scaling group](create-launch-template.md).
+ Verify that the launch template doesn't already request Spot Instances.

## Create a mixed instances group with attribute-based instance type selection (console)
<a name="attribute-based-instance-type-selection-console"></a>

Use the following procedure to create a mixed instances group by using attribute-based instance type selection. To help you move through the steps efficiently, some optional sections are skipped.

For most general purpose workloads, it's enough to specify the number of vCPUs and memory that you need. For advanced use cases, you can specify attributes like storage type, network interfaces, CPU manufacturer, and accelerator type.

To review the best practices for a mixed instances group, see [Setup overview for creating a mixed instances group](mixed-instances-groups-set-up-overview.md).

**To create a mixed instances group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the same AWS Region that you used when you created the launch template.

1. Choose **Create an Auto Scaling group**.

1. On the **Choose launch template or configuration** page, for **Auto Scaling group name**, enter a name for your Auto Scaling group.

1. To choose your launch template, do the following:

   1. For **Launch template**, choose an existing launch template.

   1. For **Launch template version**, choose whether the Auto Scaling group uses the default, the latest, or a specific version of the launch template when scaling out.

   1. Verify that your launch template supports all of the options that you are planning to use, and then choose **Next**.

1. On the **Choose instance launch options** page, do the following:

   1. For **Instance type requirements**, choose **Override launch template**.
**Note**
If you chose a launch template that already contains a set of instance attributes, such as vCPUs and memory, then the instance attributes are displayed. These attributes are added to the Auto Scaling group properties, where you can update them from the Amazon EC2 Auto Scaling console at any time.

   1. Under **Specify instance attributes**, start by entering your vCPUs and memory requirements.
      + For **vCPUs**, enter the desired minimum and maximum number of vCPUs. To specify no limit, select **No minimum**, **No maximum**, or both.
      + For **Memory (GiB)**, enter the desired minimum and maximum amount of memory. To specify no limit, select **No minimum**, **No maximum**, or both.

   1. (Optional) For **Additional instance attributes**, you can optionally specify one or more attributes to express your compute requirements in more detail. Each additional attribute adds further constraints to your request.

   1. Expand **Preview matching instance types** to view the instance types that have your specified attributes.

   1. Under **Instance purchase options**, for **Instances distribution**, specify the percentages of the group to launch as On-Demand Instances and as Spot Instances. If your application is stateless, fault tolerant, and can handle an instance being interrupted, you can specify a higher percentage of Spot Instances.

   1. (Optional) When you specify a percentage for Spot Instances, select **Include On-Demand base capacity** and then specify the minimum amount of the Auto Scaling group's initial capacity that must be fulfilled by On-Demand Instances. Anything beyond the base capacity uses the **Instances distribution** settings to determine how many On-Demand Instances and Spot Instances to launch.

   1. Under **Allocation strategies**, **Lowest price** is automatically selected for the **On-Demand allocation strategy** and cannot be changed.

   1. For **Spot allocation strategy**, choose an allocation strategy. **Price capacity optimized** is selected by default.

   1. For **Capacity Rebalancing**, choose whether to enable or disable Capacity Rebalancing. Use Capacity Rebalancing to automatically respond when your Spot Instances approach termination from a Spot interruption. For more information, see [Capacity Rebalancing in Auto Scaling to replace at-risk Spot Instances](ec2-auto-scaling-capacity-rebalancing.md).

   1. Under **Network**, for **VPC**, choose a VPC. The Auto Scaling group must be created in the same VPC as the security group you specified in your launch template.

   1. For **Availability Zones and subnets**, choose one or more subnets in the specified VPC. Use subnets in multiple Availability Zones for high availability. For more information, see [Considerations when choosing VPC subnets](asg-in-vpc.md#as-vpc-considerations).

   1. Choose **Next**, **Next**.

1. For the **Configure group size and scaling policies** step, do the following:

   1. To measure your desired capacity in units other than instances, choose the appropriate option for **Group size**, **Desired capacity type**. **Units**, **vCPUs**, and **Memory GiB** are supported. By default, Amazon EC2 Auto Scaling specifies **Units**, which translates into number of instances.

   1. For **Desired capacity**, the initial size of your Auto Scaling group.

   1. In the **Scaling** section, under **Scaling limits**, if your new value for **Desired capacity** is greater than **Min desired capacity** and **Max desired capacity**, the **Max desired capacity** is automatically increased to the new desired capacity value. You can change these limits as needed. For more information, see [Set scaling limits for your Auto Scaling group](asg-capacity-limits.md).

1. Choose **Skip to review**.

1. On the **Review** page, choose **Create Auto Scaling group**.

## Create a mixed instances group with attribute-based instance type selection (AWS CLI)
<a name="attribute-based-instance-type-selection-aws-cli"></a>

**To create a mixed instances group using the command line**
Use one of the following commands:
+ [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) (AWS CLI)
+ [New-ASAutoScalingGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/New-ASAutoScalingGroup.html) (AWS Tools for Windows PowerShell)

## Example configuration
<a name="attribute-based-instance-type-selection-example-configurations"></a>

To create an Auto Scaling group with attribute-based instance type selection by using the AWS CLI, use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command.

The following instance attributes are specified:
+ `VCpuCount` – The instance types must have a minimum of four vCPUs and a maximum of eight vCPUs.
+ `MemoryMiB` – The instance types must have a minimum of 16,384 MiB of memory.
+ `CpuManufacturers` – The instance types must have an Intel manufactured CPU.

### JSON
<a name="attribute-based-instance-type-selection-aws-cli-json"></a>

```
aws autoscaling create-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The following is an example `config.json` file.

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "DesiredCapacityType": "units",
    "MixedInstancesPolicy": {
        "LaunchTemplate": {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "{{my-launch-template}}",
                "Version": "{{$Default}}"
            },
            "Overrides": [{
                "InstanceRequirements": {
                    "VCpuCount": {"Min": {{4}}, "Max": {{8}}},
                    "MemoryMiB": {"Min": {{16384}}},
                    "CpuManufacturers": ["intel"]
                }
            }]
        },
        "InstancesDistribution": {
            "OnDemandPercentageAboveBaseCapacity": {{50}},
            "SpotAllocationStrategy": "price-capacity-optimized"
        }
    },
    "MinSize": {{0}},
    "MaxSize": {{100}},
    "DesiredCapacity": {{4}},
    "DesiredCapacityType": "units",
    "VPCZoneIdentifier": "{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}"
}
```

To set the value for desired capacity as the number of vCPUs or the amount of memory, specify `"DesiredCapacityType": "vcpu"` or `"DesiredCapacityType": "memory-mib"` in the file. The default desired capacity type is `units`, which sets the value for desired capacity as the number of instances.

### YAML
<a name="attribute-based-instance-type-selection-aws-cli-yaml"></a>

Alternatively, you can use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create the Auto Scaling group. This references a YAML file as the sole parameter for your Auto Scaling group.

```
aws autoscaling create-auto-scaling-group --cli-input-yaml {{file://~/config.yaml}}
```

The following is an example `config.yaml` file.

```
---
AutoScalingGroupName: {{my-asg}}
DesiredCapacityType: units
MixedInstancesPolicy:
  LaunchTemplate:
    LaunchTemplateSpecification:
      LaunchTemplateName: {{my-launch-template}}
      Version: {{$Default}}
    Overrides:
    - InstanceRequirements:
         VCpuCount:
           Min: 2
           Max: 4
         MemoryMiB:
           Min: 2048
         CpuManufacturers:
         - intel
  InstancesDistribution:
    OnDemandPercentageAboveBaseCapacity: {{50}}
    SpotAllocationStrategy: price-capacity-optimized
MinSize: {{0}}
MaxSize: {{100}}
DesiredCapacity: {{4}}
DesiredCapacityType: units
VPCZoneIdentifier: {{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}
```

To set the value for desired capacity as the number of vCPUs or the amount of memory, specify `DesiredCapacityType: vcpu` or `DesiredCapacityType: memory-mib` in the file. The default desired capacity type is `units`, which sets the value for desired capacity as the number of instances.

For an example of how to use multiple launch templates with attribute-based instance type selection, see [Use multiple launch templates](ec2-auto-scaling-mixed-instances-groups-launch-template-overrides.md).

## Preview your instance types
<a name="attribute-based-instance-type-selection-preview"></a>

You can preview the instance types that match your compute requirements without launching them and adjust your requirements if necessary. When creating your Auto Scaling group in the Amazon EC2 Auto Scaling console, a preview of the instance types appears in the **Preview matching instance types** section on the **Choose instance launch options** page.

Alternatively, you can preview the instance types by making an Amazon EC2 [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) API call using the AWS CLI or an SDK. Pass the `InstanceRequirements` parameters in the request in the exact format that you would use to create or update an Auto Scaling group. For more information, see [Preview instance types with specified attributes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-get-instance-types-from-instance-requirements) in the *Amazon EC2 User Guide*.

## Related resources
<a name="attribute-based-instance-type-selection-related-resources"></a>

To learn more about attribute-based instance type selection, see [Attribute-Based Instance Type Selection for EC2 Auto Scaling and EC2 Fleet](https://aws.amazon.com/blogs/aws/new-attribute-based-instance-type-selection-for-ec2-auto-scaling-and-ec2-fleet/) on the AWS Blog.

You can declare attribute-based instance type selection when you create an Auto Scaling group using CloudFormation. For more information, see the example snippet in the [Auto scaling template snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-autoscaling.html#scenario-mixed-instances-group-template-examples) section of the *CloudFormation User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
