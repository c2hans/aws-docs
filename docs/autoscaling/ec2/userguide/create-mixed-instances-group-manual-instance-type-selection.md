---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-manual-instance-type-selection.html
---

# Create a mixed instances group by manually choosing instance types
<a name="create-mixed-instances-group-manual-instance-type-selection"></a>

This topic shows you how to launch multiple instance types in a single Auto Scaling group by manually choosing your instance types.

If you prefer to use instance attributes as criteria for selecting instance types, see [Create mixed instances group using attribute-based instance type selection](create-mixed-instances-group-attribute-based-instance-type-selection.md).

**Topics**
+ [Prerequisites](#manual-instance-type-selection-prerequisites)
+ [Create a mixed instances group (console)](#manual-instance-type-selection-console)
+ [Create a mixed instances group (AWS CLI)](#manual-instance-type-selection-aws-cli)
+ [Example configurations](#manual-instance-type-selection-example-configurations)

## Prerequisites
<a name="manual-instance-type-selection-prerequisites"></a>
+ Create a launch template. For more information, see [Create a launch template for an Auto Scaling group](create-launch-template.md).
+ Verify that the launch template doesn't already request Spot Instances.

## Create a mixed instances group (console)
<a name="manual-instance-type-selection-console"></a>

Use the following procedure to create a mixed instances group by manually choosing which instance types your group can launch. To help you move through the steps efficiently, some optional sections are skipped.

To review the best practices for a mixed instances group, see [Setup overview for creating a mixed instances group](mixed-instances-groups-set-up-overview.md).

**To create a mixed instances group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the same AWS Region that you used when you created the launch template.

1. Choose **Create an Auto Scaling group**.

1. On the **Choose launch template or configuration** page, for **Auto Scaling group name**, enter a name for your Auto Scaling group.

1. To choose your launch template, do the following:

   1. For **Launch template**, choose an existing launch template.

   1. For **Launch template version**, choose whether the Auto Scaling group uses the default, the latest, or a specific version of the launch template when scaling out.

   1. Verify that your launch template supports all of the options that you plan to use, and then choose **Next**.

1. On the **Choose instance launch options** page, do the following:

   1. For **Instance type requirements**, choose **Override launch template**, and then choose **Manually add instance types**.

   1. Choose your instance types. You can use our recommendations as a starting point. **Family and generation flexible** is selected by default.
      + To change the order of the instance types, use the arrows. If you choose an allocation strategy that supports prioritization, the instance type order sets their launch priority.
      + To remove an instance type, choose **X**.
      + (Optional) For the boxes in the **Weight** column, assign each instance type a relative weight. To do so, enter the number of units that an instance of that type counts toward the desired capacity of the group. Doing so might be useful if the instance types offer different vCPU, memory, storage, or network bandwidth capabilities. For more information, see [Configure an Auto Scaling group to use instance weights](ec2-auto-scaling-mixed-instances-groups-instance-weighting.md).

        Note that if you choose to use **Size flexible** recommendations, then all instance types that are part of this section automatically have a weight value. If you don't want to specify any weights, clear the boxes in the **Weight** column for all instance types.

   1. Under **Instance purchase options**, for **Instances distribution**, specify the percentages of the group to be launched as On-Demand Instances and Spot Instances respectively. If your application is stateless, fault tolerant, and can handle an instance being interrupted, you can specify a higher percentage of Spot Instances.

   1. (Optional) When you specify a percentage for Spot Instances, select **Include On-Demand base capacity** and then specify the minimum amount of the Auto Scaling group's initial capacity that must be fulfilled by On-Demand Instances. Anything beyond the base capacity uses the **Instances distribution** settings to determine how many On-Demand Instances and Spot Instances to launch.

   1. Under **Allocation strategies**, for **On-Demand allocation strategy**, choose an allocation strategy. When you manually choose your instance types, **Prioritized** is selected by default.

   1. For **Spot allocation strategy**, choose an allocation strategy. **Price capacity optimized** is selected by default.

      If you choose **Capacity optimized**, you can optionally check the **Prioritize instance types** box to let Amazon EC2 Auto Scaling choose which instance type to launch first based on the order your instance types are listed in.

   1. For **Capacity Rebalancing**, choose whether to enable or disable Capacity Rebalancing. Use Capacity Rebalancing to automatically respond when your Spot Instances approach termination from a Spot interruption. For more information, see [Capacity Rebalancing in Auto Scaling to replace at-risk Spot Instances](ec2-auto-scaling-capacity-rebalancing.md).

   1. Under **Network**, for **VPC**, choose a VPC. The Auto Scaling group must be created in the same VPC as the security group you specified in your launch template.

   1. For **Availability Zones and subnets**, choose one or more subnets in the specified VPC. Use subnets in multiple Availability Zones for high availability. For more information, see [Considerations when choosing VPC subnets](asg-in-vpc.md#as-vpc-considerations).

   1. Choose **Next**, **Next**.

1. For the **Configure group size and scaling policies** step, do the following:

   1. Under **Group size**, for **Desired capacity**, enter the initial number of instances to launch.

      By default, the desired capacity is expressed as the number of instances. If you assigned weights to your instance types, you must convert this value to the same unit of measurement that you used to assign weights, such as the number of vCPUs.

   1. In the **Scaling** section, under **Scaling limits**, if your new value for **Desired capacity** is greater than **Min desired capacity** and **Max desired capacity**, the **Max desired capacity** is automatically increased to the new desired capacity value. You can change these limits as needed. For more information, see [Set scaling limits for your Auto Scaling group](asg-capacity-limits.md).

1. Choose **Skip to review**.

1. On the **Review** page, choose **Create Auto Scaling group**.

## Create a mixed instances group (AWS CLI)
<a name="manual-instance-type-selection-aws-cli"></a>

**To create a mixed instances group using the command line**
Use one of the following commands:
+ [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) (AWS CLI)
+ [New-ASAutoScalingGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/New-ASAutoScalingGroup.html) (AWS Tools for Windows PowerShell)

## Example configurations
<a name="manual-instance-type-selection-example-configurations"></a>

The following example configurations show how to create mixed instances groups using different Spot allocation strategies.

**Note**
These examples show how to use a configuration file formatted in JSON or YAML. If you use AWS CLI version 1, you must specify a JSON-formatted configuration file. If you use AWS CLI version 2, you can specify a configuration file formatted in either YAML or JSON.

**Topics**
+ [Example 1: Launch Spot Instances using the `capacity-optimized` allocation strategy](#capacity-optimized-aws-cli)
+ [Example 2: Launch Spot Instances using the `capacity-optimized-prioritized` allocation strategy](#capacity-optimized-prioritized-aws-cli)
+ [Example 3: Launch Spot Instances using the `lowest-price` allocation strategy diversified over two pools](#lowest-price-aws-cli)
+ [Example 4: Launch Spot Instances using the `price-capacity-optimized` allocation strategy](#price-capacity-optimized-aws-cli)

### Example 1: Launch Spot Instances using the `capacity-optimized` allocation strategy
<a name="capacity-optimized-aws-cli"></a>

The following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command creates an Auto Scaling group that specifies the following:
+ The percentage of the group to launch as On-Demand Instances (`0`) and a base number of On-Demand Instances to start with (`1`).
+ The instance types to launch in priority order (`c5.large`, `c5a.large`, `m5.large`, `m5a.large`, `c4.large`, `m4.large`, `c3.large`, `m3.large`) .
+ The subnets in which to launch the instances (`subnet-5ea0c127`, `subnet-6194ea3b`, `subnet-c934b782`). Each corresponds to a different Availability Zone.
+ The launch template (`my-launch-template`) and the launch template version (`$Default`).

When Amazon EC2 Auto Scaling attempts to fulfill your On-Demand capacity, it launches the `c5.large` instance type first. The Spot Instances come from the optimal Spot pool in each Availability Zone based on Spot Instance capacity.

#### JSON
<a name="capacity-optimized-aws-cli-json"></a>

```
aws autoscaling create-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The `config.json` file contains the following content.

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "MixedInstancesPolicy": {
        "LaunchTemplate": {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "{{my-launch-template}}",
                "Version": "{{$Default}}"
            },
            "Overrides": [
                {
                    "InstanceType": "{{c5.large}}"
                },
                {
                    "InstanceType": "{{c5a.large}}"
                },
                {
                    "InstanceType": "{{m5.large}}"
                },
                {
                    "InstanceType": "{{m5a.large}}"
                },
                {
                    "InstanceType": "{{c4.large}}"
                },
                {
                    "InstanceType": "{{m4.large}}"
                },
                {
                    "InstanceType": "{{c3.large}}"
                },
                {
                    "InstanceType": "{{m3.large}}"
                }
            ]
        },
        "InstancesDistribution": {
            "OnDemandBaseCapacity": {{1}},
            "OnDemandPercentageAboveBaseCapacity": {{0}},
            "SpotAllocationStrategy": "capacity-optimized"
        }
    },
    "MinSize": {{1}},
    "MaxSize": {{5}},
    "DesiredCapacity": {{3}},
    "VPCZoneIdentifier": "{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}"
}
```

#### YAML
<a name="capacity-optimized-aws-cli-yaml"></a>

Alternatively, you can use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create the Auto Scaling group. This references a YAML file as the sole parameter for your Auto Scaling group.

```
aws autoscaling create-auto-scaling-group --cli-input-yaml {{file://~/config.yaml}}
```

The `config.yaml` file contains the following content.

```
---
AutoScalingGroupName: {{my-asg}}
MixedInstancesPolicy:
  LaunchTemplate:
    LaunchTemplateSpecification:
      LaunchTemplateName: {{my-launch-template}}
      Version: {{$Default}}
    Overrides:
    - InstanceType: {{c5.large}}
    - InstanceType: {{c5a.large}}
    - InstanceType: {{m5.large}}
    - InstanceType: {{m5a.large}}
    - InstanceType: {{c4.large}}
    - InstanceType: {{m4.large}}
    - InstanceType: {{c3.large}}
    - InstanceType: {{m3.large}}
  InstancesDistribution:
    OnDemandBaseCapacity: {{1}}
    OnDemandPercentageAboveBaseCapacity: {{0}}
    SpotAllocationStrategy: capacity-optimized
MinSize: {{1}}
MaxSize: {{5}}
DesiredCapacity: {{3}}
VPCZoneIdentifier: {{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}
```

### Example 2: Launch Spot Instances using the `capacity-optimized-prioritized` allocation strategy
<a name="capacity-optimized-prioritized-aws-cli"></a>

The following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command creates an Auto Scaling group that specifies the following:
+ The percentage of the group to launch as On-Demand Instances (`0`) and a base number of On-Demand Instances to start with (`1`).
+ The instance types to launch in priority order (`c5.large`, `c5a.large`, `m5.large`, `m5a.large`, `c4.large`, `m4.large`, `c3.large`, `m3.large`) .
+ The subnets in which to launch the instances (`subnet-5ea0c127`, `subnet-6194ea3b`, `subnet-c934b782`). Each corresponds to a different Availability Zone.
+ The launch template (`my-launch-template`) and the launch template version (`$Latest`).

When Amazon EC2 Auto Scaling attempts to fulfill your On-Demand capacity, it launches the `c5.large` instance type first. When Amazon EC2 Auto Scaling attempts to fulfill your Spot capacity, it honors the instance type priorities on a best-effort basis. However, it optimizes for capacity first.

#### JSON
<a name="capacity-optimized-prioritized-aws-cli-json"></a>

```
aws autoscaling create-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The `config.json` file contains the following content.

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "MixedInstancesPolicy": {
        "LaunchTemplate": {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "{{my-launch-template}}",
                "Version": "{{$Latest}}"
            },
            "Overrides": [
                {
                    "InstanceType": "{{c5.large}}"
                },
                {
                    "InstanceType": "{{c5a.large}}"
                },
                {
                    "InstanceType": "{{m5.large}}"
                },
                {
                    "InstanceType": "{{m5a.large}}"
                },
                {
                    "InstanceType": "{{c4.large}}"
                },
                {
                    "InstanceType": "{{m4.large}}"
                },
                {
                    "InstanceType": "{{c3.large}}"
                },
                {
                    "InstanceType": "{{m3.large}}"
                }
            ]
        },
        "InstancesDistribution": {
            "OnDemandBaseCapacity": {{1}},
            "OnDemandPercentageAboveBaseCapacity": {{0}},
            "SpotAllocationStrategy": "capacity-optimized-prioritized"
        }
    },
    "MinSize": {{1}},
    "MaxSize": {{5}},
    "DesiredCapacity": {{3}},
    "VPCZoneIdentifier": "{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}"
}
```

#### YAML
<a name="capacity-optimized-prioritized-aws-cli-yaml"></a>

Alternatively, you can use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create the Auto Scaling group. This references a YAML file as the sole parameter for your Auto Scaling group.

```
aws autoscaling create-auto-scaling-group --cli-input-yaml {{file://~/config.yaml}}
```

The `config.yaml` file contains the following content.

```
---
AutoScalingGroupName: {{my-asg}}
MixedInstancesPolicy:
  LaunchTemplate:
    LaunchTemplateSpecification:
      LaunchTemplateName: {{my-launch-template}}
      Version: {{$Default}}
    Overrides:
    - InstanceType: {{c5.large}}
    - InstanceType: {{c5a.large}}
    - InstanceType: {{m5.large}}
    - InstanceType: {{m5a.large}}
    - InstanceType: {{c4.large}}
    - InstanceType: {{m4.large}}
    - InstanceType: {{c3.large}}
    - InstanceType: {{m3.large}}
  InstancesDistribution:
    OnDemandBaseCapacity: {{1}}
    OnDemandPercentageAboveBaseCapacity: {{0}}
    SpotAllocationStrategy: capacity-optimized-prioritized
MinSize: {{1}}
MaxSize: {{5}}
DesiredCapacity: {{3}}
VPCZoneIdentifier: {{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}
```

### Example 3: Launch Spot Instances using the `lowest-price` allocation strategy diversified over two pools
<a name="lowest-price-aws-cli"></a>

The following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command creates an Auto Scaling group that specifies the following:
+ The percentage of the group to launch as On-Demand Instances (`50`). (This does not specify a base number of On-Demand Instances to start with.)
+ The instance types to launch in priority order (`c5.large`, `c5a.large`, `m5.large`, `m5a.large`, `c4.large`, `m4.large`, `c3.large`, `m3.large`).
+ The subnets in which to launch the instances (`subnet-5ea0c127`, `subnet-6194ea3b`, `subnet-c934b782`). Each corresponds to a different Availability Zone.
+ The launch template (`my-launch-template`) and the launch template version (`$Latest`).

When Amazon EC2 Auto Scaling attempts to fulfill your On-Demand capacity, it launches the `c5.large` instance type first. For your Spot capacity, Amazon EC2 Auto Scaling attempts to launch the Spot Instances evenly across the two lowest priced pools in each Availability Zone.

#### JSON
<a name="lowest-price-aws-cli-json"></a>

```
aws autoscaling create-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The `config.json` file contains the following content.

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "MixedInstancesPolicy": {
        "LaunchTemplate": {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "{{my-launch-template}}",
                "Version": "{{$Latest}}"
            },
            "Overrides": [
                {
                    "InstanceType": "{{c5.large}}"
                },
                {
                    "InstanceType": "{{c5a.large}}"
                },
                {
                    "InstanceType": "{{m5.large}}"
                },
                {
                    "InstanceType": "{{m5a.large}}"
                },
                {
                    "InstanceType": "{{c4.large}}"
                },
                {
                    "InstanceType": "{{m4.large}}"
                },
                {
                    "InstanceType": "{{c3.large}}"
                },
                {
                    "InstanceType": "{{m3.large}}"
                }
            ]
        },
        "InstancesDistribution": {
            "OnDemandPercentageAboveBaseCapacity": {{50}},
            "SpotAllocationStrategy": "lowest-price",
            "SpotInstancePools": {{2}}
        }
    },
    "MinSize": {{1}},
    "MaxSize": {{5}},
    "DesiredCapacity": {{3}},
    "VPCZoneIdentifier": "{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}"
}
```

#### YAML
<a name="lowest-price-aws-cli-yaml"></a>

Alternatively, you can use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create the Auto Scaling group. This references a YAML file as the sole parameter for your Auto Scaling group.

```
aws autoscaling create-auto-scaling-group --cli-input-yaml {{file://~/config.yaml}}
```

The `config.yaml` file contains the following content.

```
---
AutoScalingGroupName: {{my-asg}}
MixedInstancesPolicy:
  LaunchTemplate:
    LaunchTemplateSpecification:
      LaunchTemplateName: {{my-launch-template}}
      Version: {{$Default}}
    Overrides:
    - InstanceType: {{c5.large}}
    - InstanceType: {{c5a.large}}
    - InstanceType: {{m5.large}}
    - InstanceType: {{m5a.large}}
    - InstanceType: {{c4.large}}
    - InstanceType: {{m4.large}}
    - InstanceType: {{c3.large}}
    - InstanceType: {{m3.large}}
  InstancesDistribution:
    OnDemandPercentageAboveBaseCapacity: {{50}}
    SpotAllocationStrategy: lowest-price
    SpotInstancePools: {{2}}
MinSize: {{1}}
MaxSize: {{5}}
DesiredCapacity: {{3}}
VPCZoneIdentifier: {{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}
```

### Example 4: Launch Spot Instances using the `price-capacity-optimized` allocation strategy
<a name="price-capacity-optimized-aws-cli"></a>

The following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command creates an Auto Scaling group that specifies the following:
+ The percentage of the group to launch as On-Demand Instances (`30`). (This does not specify a base number of On-Demand Instances to start with.)
+ The instance types to launch in priority order (`c5.large`, `c5a.large`, `m5.large`, `m5a.large`, `c4.large`, `m4.large`, `c3.large`, `m3.large`).
+ The subnets in which to launch the instances (`subnet-5ea0c127`, `subnet-6194ea3b`, `subnet-c934b782`). Each corresponds to a different Availability Zone.
+ The launch template (`my-launch-template`) and the launch template version (`$Latest`).

When Amazon EC2 Auto Scaling attempts to fulfill your On-Demand capacity, it launches the `c5.large` instance type first. For your Spot capacity, Amazon EC2 Auto Scaling attempts to launch the Spot Instances from Spot Instance pools with the lowest price possible, but also with optimal capacity for the number of instances that are launching.

#### JSON
<a name="price-capacity-optimized-aws-cli-json"></a>

```
aws autoscaling create-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The `config.json` file contains the following content.

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "MixedInstancesPolicy": {
        "LaunchTemplate": {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "{{my-launch-template}}",
                "Version": "{{$Latest}}"
            },
            "Overrides": [
                {
                    "InstanceType": "{{c5.large}}"
                },
                {
                    "InstanceType": "{{c5a.large}}"
                },
                {
                    "InstanceType": "{{m5.large}}"
                },
                {
                    "InstanceType": "{{m5a.large}}"
                },
                {
                    "InstanceType": "{{c4.large}}"
                },
                {
                    "InstanceType": "{{m4.large}}"
                },
                {
                    "InstanceType": "{{c3.large}}"
                },
                {
                    "InstanceType": "{{m3.large}}"
                }
            ]
        },
        "InstancesDistribution": {
            "OnDemandPercentageAboveBaseCapacity": {{30}},
            "SpotAllocationStrategy": "price-capacity-optimized"
        }
    },
    "MinSize": {{1}},
    "MaxSize": {{5}},
    "DesiredCapacity": {{3}},
    "VPCZoneIdentifier": "{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}"
}
```

#### YAML
<a name="price-capacity-optimized-aws-cli-yaml"></a>

Alternatively, you can use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create the Auto Scaling group. This references a YAML file as the sole parameter for your Auto Scaling group.

```
aws autoscaling create-auto-scaling-group --cli-input-yaml {{file://~/config.yaml}}
```

The `config.yaml` file contains the following content.

```
---
AutoScalingGroupName: {{my-asg}}
MixedInstancesPolicy:
  LaunchTemplate:
    LaunchTemplateSpecification:
      LaunchTemplateName: {{my-launch-template}}
      Version: {{$Default}}
    Overrides:
    - InstanceType: {{c5.large}}
    - InstanceType: {{c5a.large}}
    - InstanceType: {{m5.large}}
    - InstanceType: {{m5a.large}}
    - InstanceType: {{c4.large}}
    - InstanceType: {{m4.large}}
    - InstanceType: {{c3.large}}
    - InstanceType: {{m3.large}}
  InstancesDistribution:
    OnDemandPercentageAboveBaseCapacity: {{30}}
    SpotAllocationStrategy: price-capacity-optimized
MinSize: {{1}}
MaxSize: {{5}}
DesiredCapacity: {{3}}
VPCZoneIdentifier: {{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
