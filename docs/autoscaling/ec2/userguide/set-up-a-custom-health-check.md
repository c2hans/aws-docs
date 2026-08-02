---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/set-up-a-custom-health-check.html
---

# Set up a custom health check for your Auto Scaling group
<a name="set-up-a-custom-health-check"></a>

You can use custom health checks to complement the existing health check options provided by Amazon EC2 Auto Scaling. By combining custom health checks with the other health check types, you can create a comprehensive health monitoring system tailored to your application's needs.

To get started, create custom tests to verify that the instances in your Auto Scaling group are working correctly and can handle incoming traffic. If the health check that you configure detects that an instance isn't responding, then mark that particular instance as `Unhealthy`, which causes Amazon EC2 Auto Scaling to immediately replace it.

You can send the health status of an instance directly to Amazon EC2 Auto Scaling by using the AWS CLI or an SDK. The following examples show you how to use the AWS CLI to configure the health status of an instance and then verify the instance's health status.

Use the following [set-instance-health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/set-instance-health.html) command to set the health status of the specified instance to `Unhealthy`.

```
aws autoscaling set-instance-health --instance-id {{i-1234567890abcdef0}} --health-status Unhealthy
```

By default, this command respects the health check grace period. However, you can override this behavior and not respect the grace period by including the `--no-should-respect-grace-period` option.

Use the following [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) command to verify that the instance's health status is `Unhealthy`.

```
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names {{my-asg}}
```

The following is an example response that shows you that the health status of the instance is `Unhealthy`, and that the instance is terminating.

```
{
    "AutoScalingGroups": [
        {
            ....
            "Instances": [
                {
                    "ProtectedFromScaleIn": false,
                    "AvailabilityZone": "us-west-2a",
                    "LaunchTemplate": {
                        "LaunchTemplateName": "my-launch-template",
                        "Version": "1",
                        "LaunchTemplateId": "lt-1234567890abcdef0"
                    },
                    "InstanceId": "i-1234567890abcdef0",
                    "InstanceType": "t2.micro",
                    "HealthStatus": "Unhealthy",
                    "LifecycleState": "Terminating"
                },
                ...
            ]
        }
    ]
}
```
