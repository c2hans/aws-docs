---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-capacity-rebalancing-console-cli.html
---

# Enable Capacity Rebalancing to proactively replace at-risk Spot Instances
<a name="enable-capacity-rebalancing-console-cli"></a>

You can use the AWS Management Console or AWS CLI to enable Capacity Rebalancing for your Auto Scaling group. When Capacity Rebalancing is enabled, Amazon EC2 Auto Scaling attempts to proactively replace the Spot Instances in your group that have received an EC2 instance rebalance recommendation.

## Enable Capacity Rebalancing (console)
<a name="enable-capacity-rebalancing-console"></a>

You can enable or disable Capacity Rebalancing when you create or update an Auto Scaling group.

**To enable Capacity Rebalancing for a new Auto Scaling group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Choose **Create Auto Scaling group**.

1. For **Step 1: Choose launch template or configuration**, enter a name for the Auto Scaling group, choose a launch template, and then choose **Next** to proceed to the next step.

1. For **Step 2: Choose instance launch options**, for **Instance type requirements**, choose settings to create a mixed instances group. This includes the instance types that it can launch, instance purchase options, and allocation strategies for Spot and On-Demand Instances. By default, these settings are not configured. To configure them, you must select **Override launch template**. For more information about creating a mixed instances group, see [Auto Scaling groups with multiple instance types and purchase options](ec2-auto-scaling-mixed-instances-groups.md).

1. Under **Network**, choose the options as desired. Verify that the subnets you want to use are in different Availability Zones.

1. Under the **Allocation strategies** section, choose a Spot allocation strategy. Enable or disable Capacity Rebalancing by selecting or clearing the check box under **Capacity Rebalancing**. You only see this option when you request a percentage of the Auto Scaling group to be launched as Spot Instances in the **Instance purchase options** section.

1. Create the Auto Scaling group.

1. (Optional) Add lifecycle hooks as needed. For more information, see [Add lifecycle hooks to your Auto Scaling group](adding-lifecycle-hooks.md).

**To enable or disable Capacity Rebalancing for an existing Auto Scaling group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group. A split pane opens in the bottom of the page.

1. On the **Details** tab, choose **Allocation strategies**, **Edit**.

1. Under the **Allocation strategies** section, enable or disable Capacity Rebalancing by selecting or clearing the check box under **Capacity Rebalancing**.

1. Choose **Update**.

## Enable Capacity Rebalancing (AWS CLI)
<a name="enable-capacity-rebalancing-aws-cli"></a>

The following examples show how to use the AWS CLI to enable and disable Capacity Rebalancing.

Use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) or [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command with the following parameter:
+ `--capacity-rebalance` / `--no-capacity-rebalance` – Boolean value that indicates whether Capacity Rebalancing is enabled.

Before you call the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command, you need the name of a launch template that is configured for use with an Auto Scaling group. For more information, see [Create a launch template for an Auto Scaling group](create-launch-template.md).

**Note**
The following procedures show how to use a configuration file formatted in JSON or YAML. If you use AWS CLI version 1, you must specify a JSON-formatted configuration file. If you use AWS CLI version 2, you can specify a configuration file formatted in either YAML or JSON.

### JSON
<a name="enable-capacity-rebalancing-aws-cli-json"></a>

**To create and configure a new Auto Scaling group**
+ Use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create a new Auto Scaling group and enable Capacity Rebalancing. This command references a JSON file as the sole parameter for your Auto Scaling group.

  ```
  aws autoscaling create-auto-scaling-group --cli-input-json {{file://~/config.json}}
  ```

  If you don't already have a CLI configuration file that specifies a [mixed instances policy](ec2-auto-scaling-mixed-instances-groups.md), create one.

  Add the following line to the top-level JSON object in the configuration file.

  ```
  {
      "CapacityRebalance": true
  }
  ```

  The following is an example `config.json` file.

  ```
  {
      "AutoScalingGroupName": "{{my-asg}}",
      "DesiredCapacity": {{12}},
      "MinSize": {{12}},
      "MaxSize": {{15}},
      "CapacityRebalance": true,
      "MixedInstancesPolicy": {
          "InstancesDistribution": {
              "OnDemandBaseCapacity": {{0}},
              "OnDemandPercentageAboveBaseCapacity": {{25}},
              "SpotAllocationStrategy": "price-capacity-optimized"
          },
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
          }
      },
      "TargetGroupARNs": "{{arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-alb-target-group/943f017f100becff}}",
      "VPCZoneIdentifier": "{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}"
  }
  ```

### YAML
<a name="enable-capacity-rebalancing-aws-cli-yaml"></a>

**To create and configure a new Auto Scaling group**
+ Use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create a new Auto Scaling group and enable Capacity Rebalancing. This command references a YAML file as the sole parameter for your Auto Scaling group.

  ```
  aws autoscaling create-auto-scaling-group --cli-input-yaml {{file://~/config.yaml}}
  ```

  Add the following line to your configuration file formatted in YAML.

  ```
  CapacityRebalance: true
  ```

  The following is an example `config.yaml` file.

  ```
  ---
  AutoScalingGroupName: {{my-asg}}
  DesiredCapacity: {{12}}
  MinSize: {{12}}
  MaxSize: {{15}}
  CapacityRebalance: true
  MixedInstancesPolicy:
    InstancesDistribution:
      OnDemandBaseCapacity: {{0}}
      OnDemandPercentageAboveBaseCapacity: {{25}}
      SpotAllocationStrategy: price-capacity-optimized
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
  TargetGroupARNs:
  - {{arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-alb-target-group/943f017f100becff}}
  VPCZoneIdentifier: {{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}
  ```

**To enable Capacity Rebalancing for an existing Auto Scaling group**
+ Use the following [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command to enable Capacity Rebalancing.

  ```
  aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
    --capacity-rebalance
  ```

**To verify that Capacity Rebalancing is enabled for an Auto Scaling group**
+ Use the following [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) command to verify that Capacity Rebalancing is enabled and to view the details.

  ```
  aws autoscaling describe-auto-scaling-groups --auto-scaling-group-name {{my-asg}}
  ```

  The following is an example response.

  ```
  {
      "AutoScalingGroups": [
          {
              "AutoScalingGroupName": "my-asg",
              "AutoScalingGroupARN": "{{arn}}",
              ...
              "CapacityRebalance": true
          }
      ]
  }
  ```

**To disable Capacity Rebalancing**
Use the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command with the `--no-capacity-rebalance` option to disable Capacity Rebalancing.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --no-capacity-rebalance
```

## Related resources
<a name="capacity-rebalancing-related-resources"></a>

For more information about Capacity Rebalancing, see [Proactively manage Spot Instance lifecycle using the new Capacity Rebalancing feature for Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/proactively-manage-spot-instance-lifecycle-using-the-new-capacity-rebalancing-feature-for-ec2-auto-scaling/) on the AWS Compute Blog.

For more information about the EC2 instance rebalance recommendations, see [EC2 instance rebalance recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/rebalance-recommendations.html) in the *Amazon EC2 User Guide*.

To learn more about lifecycle hooks, see the following resources.
+ [Tutorial: Configure a lifecycle hook that invokes a Lambda function](tutorial-lifecycle-hook-lambda.md) (using EventBridge)
+ [Tutorial: Use data script and instance metadata to retrieve lifecycle state](tutorial-lifecycle-hook-instance-metadata.md)

## Limitations
<a name="capacity-rebalancing-limitations"></a>
+ Amazon EC2 Auto Scaling can replace the instance that receives the rebalance notification only if the instance isn't protected from scale in. However, scale-in protection doesn't prevent termination from a Spot interruption. For more information, see [Use instance scale-in protection to control instance termination](ec2-auto-scaling-instance-protection.md).
+ Support for Capacity Rebalancing is available in all commercial AWS Regions where Amazon EC2 Auto Scaling is available, except for the Middle East (UAE) Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
