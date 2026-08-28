---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html
---

# Temporarily remove instances from your Auto Scaling group
<a name="as-enter-exit-standby"></a>

You can put an instance that is in the `InService` state into the `Standby` state, update or troubleshoot the instance, and then return the instance to service. Instances that are on standby are still part of the Auto Scaling group, but they do not actively handle load balancer traffic.

This feature helps you stop and start the instances or reboot them without worrying about Amazon EC2 Auto Scaling terminating the instances as part of its health checks or during scale-in events.

For example, you can change the Amazon Machine Image (AMI) for an Auto Scaling group at any time by changing the launch template or launch configuration. Any subsequent instances that the Auto Scaling group launches use this AMI. However, the Auto Scaling group does not update the instances that are currently in service. You can terminate these instances and let Amazon EC2 Auto Scaling replace them, or use the instance refresh feature to terminate and replace the instances. Or, you can put the instances on standby, update the software, and then put the instances back in service.

Detaching instances from an Auto Scaling group is similar to putting instances on standby. Detaching instances might be useful if you want to attach them to a different group or manage the instances like standalone EC2 instances and possibly terminate them. For more information, see [Detach or attach instances from your Auto Scaling group](ec2-auto-scaling-detach-attach-instances.md).

**Topics**
+ [How the standby state works](#standby-state)
+ [Considerations](#standby-instance-considerations)
+ [Health status of an instance in a standby state](#standby-instance-health-status)
+ [Temporarily remove an instance by setting it to standby](#standby-state)

## How the standby state works
<a name="standby-state"></a>

The standby state works as follows to help you temporarily remove an instance from your Auto Scaling group:

1. You put an instance into the standby state. The instance remains in this state until you exit the standby state.

1. If there is a load balancer target group or Classic Load Balancer attached to your Auto Scaling group, the instance is deregistered from the load balancer. If connection draining is enabled for the load balancer, Elastic Load Balancing waits 300 seconds by default before completing the deregistration process, which helps in-flight requests to complete.

1. You can update or troubleshoot the instance.

1. You return the instance to service by exiting the standby state.

1. If there is a load balancer target group or Classic Load Balancer attached to your Auto Scaling group, the instance is registered with the load balancer.

For more information about the lifecycle of instances in an Auto Scaling group, see [Amazon EC2 Auto Scaling instance lifecycle](ec2-auto-scaling-lifecycle.md).

## Considerations
<a name="standby-instance-considerations"></a>

The following are considerations when moving instances in and out of the standby state:
+ When you put an instance on standby, you can either decrement the desired capacity through this operation, or keep it the same value.
  + If you choose not to decrement the desired capacity of the Auto Scaling group, Amazon EC2 Auto Scaling launches an instance to replace the one on standby. The intention is to help you maintain capacity for your application while one or more instances are on standby.
  + If you choose to decrement the desired capacity of the Auto Scaling group, this prevents the launch of an instance to replace the one on standby.
+ After you put the instance back in service, the desired capacity is incremented to reflect how many instances are in the Auto Scaling group.
+ To do the increment (and decrement), the new desired capacity must be between the minimum and maximum group size. Otherwise, the operation fails.
+ If at anytime after putting an instance on standby, or returning the instance to service by exiting the standby state, your Auto Scaling group is found to not be balanced between Availability Zones, Amazon EC2 Auto Scaling compensates by rebalancing the Availability Zones unless you suspend the `AZRebalance` process. For more information, see [Suspend and resume Amazon EC2 Auto Scaling processes](as-suspend-resume-processes.md).
+ You are billed for instances that are in a standby state.

## Health status of an instance in a standby state
<a name="standby-instance-health-status"></a>

Amazon EC2 Auto Scaling does not perform health checks on instances that are in a standby state. While the instance is in a standby state, its health status reflects the status that it had before you put it on standby. Amazon EC2 Auto Scaling does not perform a health check on the instance until you put it back in service.

For example, if you put a healthy instance on standby and then terminate it, Amazon EC2 Auto Scaling continues to report the instance as healthy. If you attempt to put a terminated instance that was on standby back in service, Amazon EC2 Auto Scaling performs a health check on the instance, determines that it is terminating and unhealthy, and launches a replacement instance. For more information, see [Health checks for instances in an Auto Scaling group](ec2-auto-scaling-health-checks.md).

## Temporarily remove an instance by setting it to standby
<a name="standby-state"></a>

Use one of the following procedures to take an instance out of service temporarily by placing it into standby state.

------
#### [ Console ]

**To temporarily remove an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Instance management** tab, in **Instances**, select an instance.

1. Choose **Actions**, **Set to Standby**.

1. In the **Set to Standby** dialog box, keep the **Replace instance** check box selected to launch a replacement instance. Clear the check box to decrement the desired capacity.

1. When prompted for confirmation, type **standby** to confirm putting the specified instance into the `Standby` state, and then choose **Set to Standby**.

1. You can update or troubleshoot your instance as needed. When you have finished, continue with the next step to return the instance to service.

1. Select the instance, choose **Actions**, **Set to InService**. In the **Set to InService** dialog box, choose **Set to InService**.

------
#### [ AWS CLI ]

To temporarily remove an instance from your Auto Scaling group, use the following example commands. Replace each {{user input placeholder}} with your own information.

**To temporarily remove an instance**

1. Use the following [describe-auto-scaling-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-instances.html) command to identify the instance to update.

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
               "InstanceId": "t3.micro",
               "AutoScalingGroupName": "my-asg",
               "HealthStatus": "HEALTHY",
               "LifecycleState": "InService"
           },
          ...
       ]
   }
   ```

1. Move the instance into a `Standby` state using the following [enter-standby](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/enter-standby.html) command. The `--should-decrement-desired-capacity` option decreases the desired capacity so that the Auto Scaling group does not launch a replacement instance.

   ```
   aws autoscaling enter-standby --instance-ids {{i-05b4f7d5be44822a6}} \
     --auto-scaling-group-name {{my-asg}} --should-decrement-desired-capacity
   ```

   The following is an example response.

   ```
   {
       "Activities": [
           {
               "ActivityId": "3b1839fe-24b0-40d9-80ae-bcd883c2be32",
               "AutoScalingGroupName": "my-asg",
               "Description": "Moving EC2 instance to Standby: i-05b4f7d5be44822a6",
               "Cause": "At 2023-12-15T21:31:26Z instance i-05b4f7d5be44822a6 was moved to standby
                 in response to a user request, shrinking the capacity from 4 to 3.",
               "StartTime": "2023-12-15T21:31:26.150Z",
               "StatusCode": "InProgress",
               "Progress": 50,
               "Details": "{\"Subnet ID\":\"subnet-c934b782\",\"Availability Zone\":\"us-west-2a\"}"
           }
       ]
   }
   ```

1. (Optional) Verify that the instance is in `Standby` using the following [describe-auto-scaling-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-instances.html) command.

   ```
   aws autoscaling describe-auto-scaling-instances --instance-ids {{i-05b4f7d5be44822a6}}
   ```

   The following is an example response. Notice that the status of the instance is now `Standby`.

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
               "LifecycleState": "Standby"
           },
          ...
       ]
   }
   ```

1. You can update or troubleshoot your instance as needed. When you have finished, continue with the next step to return the instance to service.

1. Put the instance back in service using the following [exit-standby](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/exit-standby.html) command.

   ```
   aws autoscaling exit-standby --instance-ids {{i-05b4f7d5be44822a6}} --auto-scaling-group-name {{my-asg}}
   ```

   The following is an example response.

   ```
   {
       "Activities": [
           {
               "ActivityId": "db12b166-cdcc-4c54-8aac-08c5935f8389",
               "AutoScalingGroupName": "my-asg",
               "Description": "Moving EC2 instance out of Standby: i-05b4f7d5be44822a6",
               "Cause": "At 2023-12-15T21:46:14Z instance i-05b4f7d5be44822a6 was moved out of standby in
                  response to a user request, increasing the capacity from 3 to 4.",
               "StartTime": "2023-12-15T21:46:14.678Z",
               "StatusCode": "PreInService",
               "Progress": 30,
               "Details": "{\"Subnet ID\":\"subnet-c934b782\",\"Availability Zone\":\"us-west-2a\"}"
           }
       ]
   }
   ```

1. (Optional) Verify that the instance is back in service using the following `describe-auto-scaling-instances` command.

   ```
   aws autoscaling describe-auto-scaling-instances --instance-ids {{i-05b4f7d5be44822a6}}
   ```

   The following is an example response. Notice that the status of the instance is `InService`.

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
          ...
       ]
   }
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
