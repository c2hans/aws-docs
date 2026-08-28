---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups-launch-template-overrides.html
---

# Use multiple launch templates
<a name="ec2-auto-scaling-mixed-instances-groups-launch-template-overrides"></a>

In addition to using multiple instance types, you can also use multiple launch templates.

For example, say that you configure an Auto Scaling group for compute-intensive applications and want to include a mix of C5, C5a, and C6g instance types. However, C6g instances feature an AWS Graviton processor based on 64-bit Arm architecture, while the C5 and C5a instances run on 64-bit Intel x86 processors. The AMIs for C5 and C5a instances both work on each of those instances, but not on C6g instances. To solve this problem, use a different launch template for C6g instances. You can still use the same launch template for C5 and C5a instances.

This section contains procedures for using the AWS CLI to perform tasks related to using multiple launch templates. Currently, this feature is available only if you use the AWS CLI or an SDK, and is not available from the console.

**Topics**
+ [Configure an Auto Scaling group to use multiple launch templates](#configue-auto-scaling-group-to-use-multiple-launch-templates)
+ [Related resources](#multiple-launch-templates-related-resources)

## Configure an Auto Scaling group to use multiple launch templates
<a name="configue-auto-scaling-group-to-use-multiple-launch-templates"></a>

You can configure an Auto Scaling group to use multiple launch templates, as shown in the following examples.

**To configure a new Auto Scaling group to use multiple launch templates (AWS CLI)**
Use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command. For example, the following command creates a new Auto Scaling group. It specifies the `c5.large`, `c5a.large`, and `c6g.large` instance types and defines a new launch template for the `c6g.large` instance type to ensure that an appropriate AMI is used to launch Arm instances. Amazon EC2 Auto Scaling uses the order of instance types to determine which instance type to use first when fulfilling On-Demand capacity.

```
aws autoscaling create-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The `config.json` file contains the following content.

```
{
  "AutoScalingGroupName":"{{my-asg}}",
  "MixedInstancesPolicy":{
    "LaunchTemplate":{
      "LaunchTemplateSpecification":{
        "LaunchTemplateName":"{{my-launch-template-for-x86}}",
        "Version":"{{$Latest}}"
      },
      "Overrides":[
        {
          "InstanceType":"{{c6g.large}}",
          "LaunchTemplateSpecification": {
            "LaunchTemplateName": "{{my-launch-template-for-arm}}",
            "Version": "{{$Latest}}"
          }
        },
        {
          "InstanceType":"{{c5.large}}"
        },
        {
          "InstanceType":"{{c5a.large}}"
        }
      ]
    },
    "InstancesDistribution":{
      "OnDemandBaseCapacity": {{1}},
      "OnDemandPercentageAboveBaseCapacity": {{50}},
      "SpotAllocationStrategy": "capacity-optimized"
    }
  },
  "MinSize":{{1}},
  "MaxSize":{{5}},
  "DesiredCapacity":{{3}},
  "VPCZoneIdentifier":"{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}",
  "Tags":[ ]
}
```

**To configure an existing Auto Scaling group to use multiple launch templates (AWS CLI)**
Use the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command. For example, the following command assigns the launch template named `{{my-launch-template-for-arm}}` to the `{{c6g.large}}` instance type for the Auto Scaling group named {{`my-asg`}}.

```
aws autoscaling update-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The `config.json` file contains the following content.

```
{
  "AutoScalingGroupName":"{{my-asg}}",
  "MixedInstancesPolicy":{
    "LaunchTemplate":{
      "Overrides":[
        {
          "InstanceType":"{{c6g.large}}",
          "LaunchTemplateSpecification": {
            "LaunchTemplateName": "{{my-launch-template-for-arm}}",
            "Version": "{{$Latest}}"
          }
        },
        {
          "InstanceType":"{{c5.large}}"
        },
        {
          "InstanceType":"{{c5a.large}}"
        }
      ]
    }
  }
}
```

**To configure a new Auto Scaling group to use multiple launch templates with attribute-based instance type selection (AWS CLI)**
Use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command. For example, the following command creates a new Auto Scaling group by specifying a launch template for AWS Graviton instances with an ARM AMI and an additional launch template for AMD or Intel based instances with an x86 AMI. Then, it uses [attribute-based instance selection](create-mixed-instances-group-attribute-based-instance-type-selection.md) twice to select from a wide range of instance types for each CPU architecture. You can add a similar configuration to an existing Auto Scaling group with the [update-autoscaling-group](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/update-auto-scaling-group.html) command.

```
aws autoscaling create-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The `config.json` file contains the following content.

```
{
  "AutoScalingGroupName":"{{my-asg}}",
  "MixedInstancesPolicy":{
    "LaunchTemplate":{
      "LaunchTemplateSpecification":{
        "LaunchTemplateName":"{{my-launch-template-for-arm}}",
        "Version":"{{$Latest}}"
      },
      "Overrides":[
        {
          "InstanceRequirements": {
            "VCpuCount": {"Min": {{2}}},
            "MemoryMiB": {"Min": {{2048}}},
            "CpuManufacturers": ["amazon-web-services"]
          }
         },
         {
           "InstanceRequirements": {
            "VCpuCount": {"Min": {{2}}},
            "MemoryMiB": {"Min": {{2048}}},
            "CpuManufacturers": ["intel", "amd"]
          },
          "LaunchTemplateSpecification": {
            "LaunchTemplateName": "{{my-launch-template-for-x86}}",
            "Version": "{{$Latest}}"
          }
         }
      ]
    },
    "InstancesDistribution":{
      "OnDemandPercentageAboveBaseCapacity": {{0}},
      "SpotAllocationStrategy": "price-capacity-optimized"
    }
  },
  "MinSize":{{1}},
  "MaxSize":{{10}},
  "DesiredCapacity":{{6}},
  "VPCZoneIdentifier":"{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}",
  "Tags":[ ]
}
```

**To verify the launch templates for an Auto Scaling group**
Use one of the following commands:
+ [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) (AWS CLI)
+ [Get-ASAutoScalingGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ASAutoScalingGroup.html) (AWS Tools for Windows PowerShell)

## Related resources
<a name="multiple-launch-templates-related-resources"></a>

You can find an example of specifying multiple launch templates using attribute-based instance type selection in a CloudFormation template on [AWS re:Post](https://repost.aws/articles/ARQeKDQX68TcqipYaaisl6bA/cloudformation-auto-scaling-group-sample-template-for-mixed-x86-intel-amd-and-aws-graviton-instances).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
