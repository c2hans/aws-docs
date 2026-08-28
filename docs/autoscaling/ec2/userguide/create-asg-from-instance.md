---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-from-instance.html
---

# Create an Auto Scaling group from existing instance using the AWS CLI
<a name="create-asg-from-instance"></a>

**Important**
We provide information about launch configurations for customers who have not yet migrated from launch configurations to launch templates. For information about migrating your Auto Scaling groups to launch templates, see [Migrate your Auto Scaling groups to launch templates](migrate-to-launch-templates.md).

If this is your first time creating an Auto Scaling group, we recommend you use the console to create a launch template from an existing EC2 instance. Then use the launch template to create a new Auto Scaling group. For this procedure, see [Create an Auto Scaling group using the Amazon EC2 launch wizard](create-asg-ec2-wizard.md).

The following procedure shows how to create an Auto Scaling group by specifying an existing instance to use as a base for launching other instances. Multiple parameters are required to create an EC2 instance, such as the Amazon Machine Image (AMI) ID, instance type, key pair, and security group. All of this information is also used by Amazon EC2 Auto Scaling to launch instances on your behalf when there is a need to scale. This information is stored in either a launch template or a launch configuration.

When you use an existing instance, Amazon EC2 Auto Scaling creates an Auto Scaling group that launches instances based on a launch configuration that's created at the same time. The new launch configuration has the same name as the Auto Scaling group, and it includes certain configuration details from the identified instance.

The following configuration details are copied from the identified instance into the launch configuration:
+ AMI ID
+ Instance type
+ Key pair
+ Security groups
+ IP address type (public or private)
+ IAM instance profile, if applicable
+ Monitoring (true or false)
+ EBS optimized (true or false)
+ Tenancy setting, if launching into a VPC (shared or dedicated)
+ Kernel ID and RAM disk ID, if applicable
+ User data, if specified
+ Spot (maximum) price

The VPC subnet and Availability Zone are copied from the identified instance to the Auto Scaling group's own resource definition.

If the identified instance is in a placement group, the new Auto Scaling group launches instances into the same placement group as the identified instance. Because the launch configuration settings do not allow a placement group to be specified, the placement group is copied to the `PlacementGroup` attribute of the new Auto Scaling group.

The following configuration details are not copied from your identified instance:
+ Storage: The block devices (EBS volumes and instance store volumes) are not copied from the identified instance. Instead, the block device mapping created as part of creating the AMI determines which devices are used.
+ Number of network interfaces: The network interfaces are not copied from your identified instance. Instead, Amazon EC2 Auto Scaling uses its default settings to create one network interface, which is the primary network interface (eth0).
+ Instance metadata options: The metadata accessible, metadata version, and token response hop limit settings are not copied from the identified instance. Instead, Amazon EC2 Auto Scaling uses its default settings. For more information, see [Configure the instance metadata options](create-launch-config.md#launch-configurations-imds).
+ Load balancers: If the identified instance is registered with one or more load balancers, the information about the load balancer is not copied to the load balancer or target group attribute of the new Auto Scaling group.
+ Tags: If the identified instance has tags, the tags are not copied to the `Tags` attribute of the new Auto Scaling group.

## Prerequisites
<a name="create-asg-from-instance-prerequisites"></a>

The EC2 instance must meet the following criteria:
+ The instance is not a member of another Auto Scaling group.
+ The instance is in the `running` state.
+ The AMI that was used to launch the instance must still exist.

## Create an Auto Scaling group from an EC2 instance (AWS CLI)
<a name="create-asg-from-instance-aws-cli"></a>

The following procedure shows you how to use a CLI command to create an Auto Scaling group from an EC2 instance.

This procedure does not add the instance to the Auto Scaling group. For the instance to be attached, you must run the [attach-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-instances.html) command after the Auto Scaling group has been created.

Before you begin, find the ID of the EC2 instance using the Amazon EC2 console or the [describe-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html) command.

**To use your current instance as a template**
+ Use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create an Auto Scaling group, `my-asg-from-instance`, from the EC2 instance `i-123456789abcdefg0`.

  ```
  aws autoscaling create-auto-scaling-group --auto-scaling-group-name {{my-asg-from-instance}} \
    --instance-id {{i-123456789abcdefg0}} --min-size {{1}} --max-size {{2}} --desired-capacity {{2}}
  ```

**To verify that your Auto Scaling group has launched instances**
+ Use the following [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) command to verify that the Auto Scaling group was created successfully.

  ```
  aws autoscaling describe-auto-scaling-groups --auto-scaling-group-name {{my-asg-from-instance}}
  ```

  The following example response shows that the desired capacity of the group is 2, the group has 2 running instances, and the launch configuration is named `my-asg-from-instance`.

  ```
  {
    "AutoScalingGroups":[
      {
        "AutoScalingGroupName":"my-asg-from-instance",
        "AutoScalingGroupARN":"{{arn}}",
        "LaunchConfigurationName":"my-asg-from-instance",
        "MinSize":1,
        "MaxSize":2,
        "DesiredCapacity":2,
        "DefaultCooldown":300,
        "AvailabilityZones":[
          "us-west-2a"
        ],
        "LoadBalancerNames":[],
        "TargetGroupARNs":[],
        "HealthCheckType":"EC2",
        "HealthCheckGracePeriod":0,
        "Instances":[
          {
            "InstanceId":"i-34567890abcdef012",
            "InstanceType":"t2.micro",
            "AvailabilityZone":"us-west-2a",
            "LifecycleState":"InService",
            "HealthStatus":"Healthy",
            "LaunchConfigurationName":"my-asg-from-instance",
            "ProtectedFromScaleIn":false
          },
          {
            "InstanceId":"i-012345abcdefg6789",
            "InstanceType":"t2.micro",
            "AvailabilityZone":"us-west-2a",
            "LifecycleState":"InService",
            "HealthStatus":"Healthy",
            "LaunchConfigurationName":"my-asg-from-instance",
            "ProtectedFromScaleIn":false
          }
        ],
        "CreatedTime":"2020-10-28T02:39:22.152Z",
        "SuspendedProcesses":[ ],
        "VPCZoneIdentifier":"subnet-0abc1234",
        "EnabledMetrics":[ ],
        "Tags":[ ],
        "TerminationPolicies":[
          "Default"
        ],
        "NewInstancesProtectedFromScaleIn":false,
        "ServiceLinkedRoleARN":"{{arn}}",
        "TrafficSources":[]
      }
    ]
  }
  ```

**To view the launch configuration**
+ Use the following [describe-launch-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-launch-configurations.html) command to view the details of the launch configuration.

  ```
  aws autoscaling describe-launch-configurations --launch-configuration-names {{my-asg-from-instance}}
  ```

  The following is example output:

  ```
  {
    "LaunchConfigurations":[
      {
        "LaunchConfigurationName":"my-asg-from-instance",
        "LaunchConfigurationARN":"{{arn}}",
        "ImageId":"ami-234567890abcdefgh",
        "KeyName":"my-key-pair-uswest2",
        "SecurityGroups":[
          "sg-12abcdefgh3456789"
        ],
        "ClassicLinkVPCSecurityGroups":[ ],
        "UserData":"",
        "InstanceType":"t2.micro",
        "KernelId":"",
        "RamdiskId":"",
        "BlockDeviceMappings":[ ],
        "InstanceMonitoring":{
          "Enabled":true
        },
        "CreatedTime":"2020-10-28T02:39:22.321Z",
        "EbsOptimized":false,
        "AssociatePublicIpAddress":true
      }
    ]
  }
  ```

**To terminate the instance**
+ If you no longer need the instance, you can terminate it. The following [terminate-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/terminate-instances.html) command terminates the instance `i-123456789abcdefg0`.

  ```
  aws ec2 terminate-instances --instance-ids {{i-123456789abcdefg0}}
  ```

  After you terminate an Amazon EC2 instance, you can't restart the instance. After termination, its data is gone and the volume can't be attached to any instance. To learn more about terminating instances, see [Terminate an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#terminating-instances-console) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
