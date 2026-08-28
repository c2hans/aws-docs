---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.html
---

# Detach or attach instances from your Auto Scaling group
<a name="ec2-auto-scaling-detach-attach-instances"></a>

You can detach instances from your Auto Scaling group. After an instance is detached, that instance becomes independent and can either be managed on its own or attached to a different Auto Scaling group, separate from the original group it belonged to. This can be useful, for example, when you want to perform testing using existing instances that are already running your application.

This topic provides instructions on how to detach and attach instances. When attaching instances, you can also use an existing instance rather than a detached one.

Instead of detaching and re-attaching an instance to the same group, we recommend using the standby procedure to temporarily remove the instance from the group. For more information, see [Temporarily remove instances from your Auto Scaling group](as-enter-exit-standby.md).

**Topics**
+ [Considerations for detaching instances](#detach-instances-considerations)
+ [Considerations for attaching instances](#attach-instances-considerations)
+ [Move an instance to a different group using detach and attach](#detach-attach-instances)

## Considerations for detaching instances
<a name="detach-instances-considerations"></a>

When you detach instances, keep these points in mind:
+ You can detach an instance when it's in the `InService` or `Standby` state, or in a retained state. Instances in a retained state can be detached only if you don't decrement the desired capacity (set `ShouldDecrementDesiredCapacity` to `false`).
+ If you are detaching instances that are in the `Standby` state, exercise caution. Including the `ShouldDecrementDesiredCapacity` flag in the API call when attempting to detach instances after putting them into the `Standby` state might cause other instances to terminate unexpectedly.
+ After you detach an instance, it continues running and incurring charges. To avoid unnecessary charges, make sure to reattach or terminate detached instances when they're no longer needed.
+ You can choose to decrement the desired capacity by the number of instances that you are detaching. If you choose not to decrement the capacity, Amazon EC2 Auto Scaling launches new instances to replace the detached ones to maintain the desired capacity.
+ If the number of instances that you are detaching will bring the Auto Scaling group below its minimum capacity, you must decrement the minimum capacity.
+ If you detach multiple instances from the same Availability Zone without decrementing the desired capacity, the group will rebalance itself unless you suspend the `AZRebalance` process. For more information, see [Suspend and resume Amazon EC2 Auto Scaling processes](as-suspend-resume-processes.md).
+ If you detach an instance from an Auto Scaling group that has an attached load balancer target group or Classic Load Balancer, the instance is deregistered from the load balancer. If connection draining (deregistration delay) is enabled for your load balancer, Amazon EC2 Auto Scaling waits for in-flight requests to complete.

## Considerations for attaching instances
<a name="attach-instances-considerations"></a>

Note the following when attaching instances:
+ Amazon EC2 Auto Scaling treats attached instances the same as instances launched by the group itself. This means that attached instances can be terminated during scale-in events if they're selected. The permissions granted by the AWSServiceRoleForAutoScaling service-linked role allow Amazon EC2 Auto Scaling to do so.
+ When you attach instances, the desired capacity of the group increases by the number of instances being attached. If the desired capacity after adding the new instances exceeds the maximum size of the group, the request to attach more instances fails.
+ If you add instances to your group causing uneven distribution across Availability Zones, Amazon EC2 Auto Scaling rebalances the group to re-establish an even distribution unless you suspend the `AZRebalance` process. For more information, see [Suspend and resume Amazon EC2 Auto Scaling processes](as-suspend-resume-processes.md).
+ If you attach an instance to an Auto Scaling group that has an attached load balancer target group or Classic Load Balancer, the instance is registered with the load balancer.

For an instance to be attached, it must meet the following criteria:
+ The instance is in the `running` state with Amazon EC2.
+ The AMI used to launch the instance must still exist.
+ The instance is not a member of another Auto Scaling group.
+ The instance is launched into one of the Availability Zones defined in the Auto Scaling group.
+ If the Auto Scaling group has an attached load balancer target group or Classic Load Balancer, the instance and the load balancer must both be in the same VPC.

## Move an instance to a different group using detach and attach
<a name="detach-attach-instances"></a>

Use one of the following procedures to detach an instance from your Auto Scaling group and attach it to a different Auto Scaling group.

To create a new Auto Scaling group from a detached instance, see [Create an Auto Scaling group from existing instance using the AWS CLI](create-asg-from-instance.md) (not recommended, creates a launch configuration).

------
#### [ Console ]

**To detach an instance from an Auto Scaling group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Instance management** tab, in **Instances**, select an instance and choose **Actions**, **Detach**.

1. In the **Detach instance** dialog box, keep the **Replace instance** check box selected to launch a replacement instance. Clear the check box to decrement the desired capacity.

1. When prompted for confirmation, type **detach** to confirm removing the specified instance from the Auto Scaling group, and then choose **Detach instance**.

You can now attach the instance to a different Auto Scaling group.

**To attach an instance to an Auto Scaling group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. (Optional) On the navigation pane, under **Auto Scaling**, choose **Auto Scaling Groups**. Select the Auto Scaling group and verify that the maximum size of the Auto Scaling group is large enough that you can add another instance. Otherwise, on the **Details** tab, increase the maximum capacity.

1. On the navigation pane, under **Instances**, choose **Instances**, and then select an instance.

1. Choose **Actions**, **Instance settings**, **Attach to Auto Scaling Group**.

1. On the **Attach to Auto Scaling group** page, for **Auto Scaling Group**, select the Auto Scaling group, and then choose **Attach**.

1. If the instance doesn't meet the criteria, you get an error message with the details. For example, the instance might not be in the same Availability Zone as the Auto Scaling group. Choose **Close** and try again with an Auto Scaling group that meets the criteria.

------
#### [ AWS CLI ]

To detach and attach an instance, use the following example commands. Replace each {{user input placeholder}} with your own information.

**To detach an instance from an Auto Scaling group**

1. To describe the current instances, use the following [describe-auto-scaling-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-instances.html) command.

   ```
   aws autoscaling describe-auto-scaling-instances \
     --query 'AutoScalingInstances[?AutoScalingGroupName==`{{my-asg}}`]'
   ```

   The following example shows the output produced when you run this command.

   Take note of the ID of the instance that you intend to remove from the group. You need this ID in the next step.

   ```
   {
       "AutoScalingInstances": [
           {
               "ProtectedFromScaleIn": false,
               "AvailabilityZone": "us-west-2a",
               "LaunchTemplate": {
                   "LaunchTemplateName": "my-launch-template",
                   "Version": "1",
                   "LaunchTemplateId": "lt-050555ad16a3f9c7f"
               },
               "InstanceId": "i-05b4f7d5be44822a6",
               "InstanceType": "t3.micro",
               "AutoScalingGroupName": "my-asg",
               "HealthStatus": "HEALTHY",
               "LifecycleState": "InService"
           },
           {
               "ProtectedFromScaleIn": false,
               "AvailabilityZone": "us-west-2a",
               "LaunchTemplate": {
                   "LaunchTemplateName": "my-launch-template",
                   "Version": "1",
                   "LaunchTemplateId": "lt-050555ad16a3f9c7f"
               },
               "InstanceId": "i-0c20ac468fa3049e8",
               "InstanceType": "t3.micro",
               "AutoScalingGroupName": "my-asg",
               "HealthStatus": "HEALTHY",
               "LifecycleState": "InService"
           },
           {
               "ProtectedFromScaleIn": false,
               "AvailabilityZone": "us-west-2a",
               "LaunchTemplate": {
                   "LaunchTemplateName": "my-launch-template",
                   "Version": "1",
                   "LaunchTemplateId": "lt-050555ad16a3f9c7f"
               },
               "InstanceId": "i-0787762faf1c28619",
               "InstanceType": "t3.micro",
               "AutoScalingGroupName": "my-asg",
               "HealthStatus": "HEALTHY",
               "LifecycleState": "InService"
           },
           {
               "ProtectedFromScaleIn": false,
               "AvailabilityZone": "us-west-2a",
               "LaunchTemplate": {
                   "LaunchTemplateName": "my-launch-template",
                   "Version": "1",
                   "LaunchTemplateId": "lt-050555ad16a3f9c7f"
               },
               "InstanceId": "i-0f280a4c58d319a8a",
               "InstanceType": "t3.micro",
               "AutoScalingGroupName": "my-asg",
               "HealthStatus": "HEALTHY",
               "LifecycleState": "InService"
           }
       ]
   }
   ```

1. To detach an instance without decrementing the desired capacity, use the following [detach-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/detach-instances.html) command.

   ```
   aws autoscaling detach-instances --instance-ids {{i-05b4f7d5be44822a6}} \
     --auto-scaling-group-name {{my-asg}}
   ```

   To detach an instance and decrement the desired capacity, include the `--should-decrement-desired-capacity` option.

   ```
   aws autoscaling detach-instances --instance-ids {{i-05b4f7d5be44822a6}} \
     --auto-scaling-group-name {{my-asg}} --should-decrement-desired-capacity
   ```

You can now attach the instance to a different Auto Scaling group.

**To attach an instance to an Auto Scaling group**

1. To attach the instance to a different Auto Scaling group, use the following [attach-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-instances.html) command.

   ```
   aws autoscaling attach-instances --instance-ids {{i-05b4f7d5be44822a6}} --auto-scaling-group-name {{my-asg-for-testing}}
   ```

1. To verify the size of the Auto Scaling group after attaching an instance, use the following [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) command.

   ```
   aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names {{my-asg-for-testing}}
   ```

   The following example response shows that the group has two running instances, one of which is the instance you attached.

   ```
   {
       "AutoScalingGroups": [
           {
               "AutoScalingGroupName": "my-asg-for-testing",
               "AutoScalingGroupARN": "{{arn}}",
               "LaunchTemplate": {
                   "LaunchTemplateName": "my-launch-template",
                   "Version": "2",
                   "LaunchTemplateId": "lt-050555ad16a3f9c7f"
               },
               "MinSize": 1,
               "MaxSize": 5,
               "DesiredCapacity": 2,
               ...
               "Instances": [
                   {
                       "ProtectedFromScaleIn": false,
                       "AvailabilityZone": "us-west-2a",
                       "LaunchTemplate": {
                           "LaunchTemplateName": "my-launch-template",
                           "Version": "1",
                           "LaunchTemplateId": "lt-050555ad16a3f9c7f"
                       },
                       "InstanceId": "i-05b4f7d5be44822a6",
                       "InstanceType": "t3.micro",
                       "HealthStatus": "Healthy",
                       "LifecycleState": "InService"
                   },
                   {
                       "ProtectedFromScaleIn": false,
                       "AvailabilityZone": "us-west-2a",
                       "LaunchTemplate": {
                           "LaunchTemplateName": "my-launch-template",
                           "Version": "2",
                           "LaunchTemplateId": "lt-050555ad16a3f9c7f"
                       },
                       "InstanceId": "i-00dcdfffdf5175890",
                       "InstanceType": "t3.micro",
                       "HealthStatus": "Healthy",
                       "LifecycleState": "InService"
                   }
               ],
               ...
           }
       ]
   }
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
