---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/configue-auto-scaling-group-to-use-weights.html
---

# Configure an Auto Scaling group to use weights
<a name="configue-auto-scaling-group-to-use-weights"></a>

You can configure an Auto Scaling group to use weights, as shown in the following AWS CLI examples. For instructions on using the console, see [Create a mixed instances group by manually choosing instance types](create-mixed-instances-group-manual-instance-type-selection.md).

**To configure a new Auto Scaling group to use weights (AWS CLI)**
Use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command. For example, the following command creates a new Auto Scaling group and assigns weights by specifying the following:
+ The percentage of the group to launch as On-Demand Instances (`0`)
+ The allocation strategy for Spot Instances in each Availability Zone (`capacity-optimized`)
+ The instance types to launch in priority order (`m4.16xlarge`, `m5.24xlarge`)
+ The instance weights that correspond to the relative size difference (vCPUs) between instance types (`16`, `24`)
+ The subnets in which to launch the instances (`subnet-5ea0c127`, `subnet-6194ea3b`, `subnet-c934b782`), each corresponding to a different Availability Zone
+ The launch template (`my-launch-template`) and the launch template version (`$Latest`)

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
                    "InstanceType": "{{m4.16xlarge}}",
                    "WeightedCapacity": {{"16"}}
                },
                {
                    "InstanceType": "{{m5.24xlarge}}",
                    "WeightedCapacity": {{"24"}}
                }
            ]
        },
        "InstancesDistribution": {
            "OnDemandPercentageAboveBaseCapacity": {{0}},
            "SpotAllocationStrategy": "{{capacity-optimized}}"
        }
    },
    "MinSize": {{160}},
    "MaxSize": {{720}},
    "DesiredCapacity": {{480}},
    "VPCZoneIdentifier": "{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}",
    "Tags": []
}
```

**To configure an existing Auto Scaling group to use weights (AWS CLI)**
Use the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command. For example, the following command assigns weights to instance types in an existing Auto Scaling group by specifying the following:
+ The instance types to launch in priority order (`c5.18xlarge`, `c5.24xlarge`, `c5.2xlarge`, `c5.4xlarge`)
+ The instance weights that correspond to the relative size difference (vCPUs) between instance types (`18`, `24`, `2`, `4`)
+ The new, increased desired capacity, which is larger than the largest weight

```
aws autoscaling update-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The `config.json` file contains the following content.

```
{
    "AutoScalingGroupName": "{{my-existing-asg}}",
    "MixedInstancesPolicy": {
        "LaunchTemplate": {
            "Overrides": [
                {
                    "InstanceType": "{{c5.18xlarge}}",
                    "WeightedCapacity": {{"18"}}
                },
                {
                    "InstanceType": "{{c5.24xlarge}}",
                    "WeightedCapacity": {{"24"}}
                },
                {
                    "InstanceType": "{{c5.2xlarge}}",
                    "WeightedCapacity": {{"2"}}
                },
                {
                    "InstanceType": "{{c5.4xlarge}}",
                    "WeightedCapacity": {{"4"}}
                }
            ]
        }
    },
    "MinSize": {{0}},
    "MaxSize": {{100}},
    "DesiredCapacity": {{100}}
}
```

**To verify the weights using the command line**
Use one of the following commands:
+ [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) (AWS CLI)
+ [Get-ASAutoScalingGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ASAutoScalingGroup.html) (AWS Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
