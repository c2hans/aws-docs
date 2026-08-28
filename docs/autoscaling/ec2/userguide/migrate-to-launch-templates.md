---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/migrate-to-launch-templates.html
---

# Migrate your Auto Scaling groups to launch templates
<a name="migrate-to-launch-templates"></a>

As of **January 1, 2023**, new instance types are no longer supported in launch configurations. This applies to any instance types added to an AWS Region after the initial Region launch. In addition, you might be able to create a launch configuration with an instance type that is no longer supported in a Region. For more information, see [Auto Scaling launch configurations](launch-configurations.md).

To migrate your Auto Scaling groups from launch configurations to launch templates, see the following steps.

**Important**
Verify that you have the permissions required to work with launch templates. For more information, see [Permissions to work with launch templates](launch-templates.md#launch-templates-permissions).
Make sure that resources associated with the launch configuration, such as security groups and IAM instance profiles, are not deleted unintentionally.
Test the rollback operation to make sure that changes can be safely reverted.

## Step 1: Find Auto Scaling groups that use launch configurations
<a name="find-groups-that-use-launch-configurations"></a>

To identify whether you have Auto Scaling groups that are still using launch configurations, run the following [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) command using the AWS CLI. Replace {{REGION}} with your AWS Region.

```
aws autoscaling describe-auto-scaling-groups --region {{REGION}} \
  --query 'AutoScalingGroups[?LaunchConfigurationName!=`null`]'
```

The following is example output.

```
[
    {
	"AutoScalingGroupName": "group-1",
	"AutoScalingGroupARN": "{{arn}}",
	"LaunchConfigurationName": "my-launch-config",
	"MinSize": 1,
	"MaxSize": 5,
	"DesiredCapacity": 2,
	"DefaultCooldown": 300,
	"AvailabilityZones": [
            "us-west-2a",
            "us-west-2b",
            "us-west-2c"
        ],
	"LoadBalancerNames": [],
	"TargetGroupARNs": [],
	"HealthCheckType": "EC2",
	"HealthCheckGracePeriod": 300,
	"Instances": [
            {
                "ProtectedFromScaleIn": false,
                "AvailabilityZone": "us-west-2a",
                "LaunchConfigurationName": "my-launch-config",
                "InstanceId": "i-05b4f7d5be44822a6",
                "InstanceType": "t3.micro",
                "HealthStatus": "Healthy",
                "LifecycleState": "InService"
            },
            {
                "ProtectedFromScaleIn": false,
                "AvailabilityZone": "us-west-2b",
                "LaunchConfigurationName": "my-launch-config",
                "InstanceId": "i-0c20ac468fa3049e8",
                "InstanceType": "t3.micro",
                "HealthStatus": "Healthy",
                "LifecycleState": "InService"
            }
	],
	"CreatedTime": "2023-03-09T22:15:11.611Z",
	"SuspendedProcesses": [],
	"VPCZoneIdentifier": "subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782",
	"EnabledMetrics": [],
	"Tags": [
            {
		"ResourceId": "group-1",
		"ResourceType": "auto-scaling-group",
		"Key": "environment",
		"Value": "production",
		"PropagateAtLaunch": true
            }
        ],
	"TerminationPolicies": [
	    "Default"
	],
	"NewInstancesProtectedFromScaleIn": false,
	"ServiceLinkedRoleARN": "{{arn}}",
       "TrafficSources": []
    },

    {{... additional groups ...}}

]
```

Alternatively, to remove everything except the Auto Scaling group names with the names of their respective launch configurations and tags in the output, run the following command:

```
aws autoscaling describe-auto-scaling-groups --region {{REGION}} \
  --query 'AutoScalingGroups[?LaunchConfigurationName!=`null`].{AutoScalingGroupName: AutoScalingGroupName, LaunchConfigurationName: LaunchConfigurationName, Tags: Tags}'
```

The following shows example output.

```
[
    {
        "AutoScalingGroupName": "group-1",
        "LaunchConfigurationName": "my-launch-config",
        "Tags": [
            {
                "ResourceId": "group-1",
                "ResourceType": "auto-scaling-group",
                "Key": "environment",
                "Value": "production",
                "PropagateAtLaunch": true
            }
        ]
    },

    {{... additional groups ...}}

]
```

For more information about filtering, see [Filtering AWS CLI output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html) in the *AWS Command Line Interface User Guide*.

## Step 2: Copy a launch configuration to a launch template
<a name="copy-launch-config"></a>

You can copy a launch configuration to a launch template using the following procedure. Then, you can add it to your Auto Scaling group.

Copying multiple launch configurations results in identically named launch templates. To change the name given to a launch template during the copying process, you must copy the launch configurations one by one.

**Note**
The copying feature is available only from the console.

**To copy a launch configuration to a launch template (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the left navigation pane, under **Auto Scaling**, choose **Auto Scaling Groups**.

1. Choose **Launch configurations** near the top of the page. When prompted for confirmation, choose **View launch configurations** to confirm that you want to view the **Launch configurations** page.

1. Select the launch configuration you want to copy and choose **Copy to launch template, Copy selected**. This sets up a new launch template with the same name and options as the launch configuration that you selected.

1. For **New launch template name**, you can use the name of the launch configuration (the default) or enter a new name. Launch template names must be unique.

1. (Optional) Select **Create an Auto Scaling group using the new template**.

   You can skip this step to finish copying the launch configuration. You do not need to create a new Auto Scaling group.

1. Choose **Copy**.

**To copy all launch configurations to launch templates (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Auto Scaling**, choose **Launch Configurations**.

1. Choose **Copy to launch template, Copy all**. This copies each launch configuration in the current Region to a new launch template with the same name and options.

1. Choose **Copy**.

## Step 3: Update an Auto Scaling group to use a launch template
<a name="replace-launch-config"></a>

After creating a launch template, you're ready to add it to your Auto Scaling group.

**To update an Auto Scaling group to use a launch template (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

   A split pane opens up in the bottom part of the page, showing information about the group that's selected.

1. On the **Details** tab, choose **Launch configuration**, **Edit**.

1. Choose **Switch to launch template**.

1. For **Launch template**, select your launch template.

1. For **Version**, select the launch template version, as needed. After you create versions of a launch template, you can choose whether the Auto Scaling group uses the default or the latest version of the launch template when scaling out.

1. Choose **Update**.

**To update an Auto Scaling group to use a launch template (AWS CLI)**
The following [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command updates the specified Auto Scaling group to use the initial version of the specified launch template.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --launch-template LaunchTemplateName=my-template-for-auto-scaling,Version='1'
```

For more examples of using CLI commands to update an Auto Scaling group to use a launch template, see [Update an Auto Scaling group to use a launch template](examples-launch-templates-aws-cli.md#update-asg-launch-template-cli).

## Step 4: Replace your instances
<a name="replace-instances"></a>

After you replace the launch configuration with a launch template, any new instances will use the new launch template. Existing instances are not affected.

To update the existing instances, you can start an instance refresh to replace the instances in your Auto Scaling group instead of manually replacing instances a few at a time. For more information, see [Use an instance refresh to update instances in an Auto Scaling group](asg-instance-refresh.md). If the group is large, an instance refresh can be particularly helpful.

Alternatively, you can allow automatic scaling to gradually replace existing instances with new instances based on the group's [termination policies](as-instance-termination.md), or you can terminate them. Manual termination forces your Auto Scaling group to launch new instances to maintain the group's desired capacity. For more information, see [Terminate an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#terminating-instances-console) in the *Amazon EC2 User Guide*.

## Additional information
<a name="migrating-to-launch-templates-more-info"></a>

For more information, see [Amazon EC2 Auto Scaling will no longer add support for new EC2 features to Launch Configurations](https://aws.amazon.com/blogs/compute/amazon-ec2-auto-scaling-will-no-longer-add-support-for-new-ec2-features-to-launch-configurations/) on the AWS Compute Blog.

For a topic that takes you through how to migrate AWS CloudFormation stacks from launch configurations to launch templates, see [Migrate AWS CloudFormation stacks to launch templates](migrate-launch-configurations-with-cloudformation.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
