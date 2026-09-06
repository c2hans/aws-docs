---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-application-status-checks-auto-scaling-group.html
---

# Use application status checks with an Auto Scaling group
<a name="use-application-status-checks-auto-scaling-group"></a>

With application status checks, your Auto Scaling group can replace instances whose applications have stopped responding, even when the underlying infrastructure is healthy. Application status checks monitor whether an application on your instance responds to HTTP or HTTPS calls. Unlike Amazon EC2 status checks, which detect problems with the underlying instance or system, application status checks detect failures at the application layer. For example, they detect a web server process that has stopped responding. If instances in your Auto Scaling group have application status checks associated and included in aggregation, Amazon EC2 Auto Scaling automatically terminates and replaces instances whose overall application status reports `impaired`. No additional Auto Scaling group configuration is required.

Application status checks are created and managed in Amazon EC2, not in Amazon EC2 Auto Scaling. Create the application status check, associate it with the instances in the Auto Scaling group by tag, and verify that it is reporting correctly. For more information about creating application status checks, see [Application status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/application-status-checks.html) in the *Amazon EC2 User Guide*.

**Prerequisites**
To use application status checks with your Auto Scaling group, make sure you have the following:
+ An Auto Scaling group with at least one instance.
+ One or more application status checks associated with the instances in the group (through tags).
+ An application endpoint listening at a network port on each instance that responds to HTTP or HTTPS calls on the port and path configured in the check.

## How Amazon EC2 Auto Scaling uses application status checks
<a name="how-asg-uses-application-status-checks"></a>

Amazon EC2 Auto Scaling uses the aggregated (overall) application status for each instance. When the overall application status reports `impaired`, Amazon EC2 Auto Scaling terminates the instance and launches a replacement. This maintains the desired capacity of the group.

Amazon EC2 Auto Scaling does not act on individual check status. Checks that are marked as `excluded` from aggregation do not affect the overall application status and therefore do not drive Amazon EC2 Auto Scaling actions. Checks that are suppressed do not drive Amazon EC2 Auto Scaling actions.

Amazon EC2 Auto Scaling also does not act on application status values other than `impaired`. If the overall status is `ok`, `initializing`, `insufficient-data`, `not-applicable`, or `suppressed`, Amazon EC2 Auto Scaling takes no action based on application status.

## Set up application status checks for an Auto Scaling group
<a name="set-up-application-status-checks-asg"></a>

To use application status checks with an Auto Scaling group, create an application status check in Amazon EC2 and then associate it with the Auto Scaling group using the `aws:autoscaling:groupName` system tag. Amazon EC2 Auto Scaling automatically applies this tag to every instance in the group. No launch template changes are required. New instances are associated automatically when they launch.

```
aws ec2 associate-application-status-check \
    --application-status-check-id asc-1234567890abcdef0 \
    --target-tag-associations Key=aws:autoscaling:groupName,Value=my-asg
```

Where:
+ `asc-1234567890abcdef0` — the ID of your application status check.
+ `my-asg` — the name of your Auto Scaling group.

When the check is included in aggregation, Amazon EC2 Auto Scaling automatically acts on instances whose overall application status reports `impaired`. No additional Auto Scaling group configuration is required.

For more information about creating and associating application status checks, see [Application status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/application-status-checks.html) in the *Amazon EC2 User Guide*.

## Health check grace period
<a name="asg-asc-health-check-grace-period"></a>

Amazon EC2 Auto Scaling uses a health check grace period to allow new instances time to start up before health checks begin. Make sure the grace period is long enough for your application to begin responding to health check calls after the instance launches. If the grace period is too short, Amazon EC2 Auto Scaling might terminate and replace instances before they are ready to serve traffic.

For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

## Suppress application status checks during maintenance
<a name="asg-asc-suppress-during-maintenance"></a>

If you need to perform in-place patching or maintenance on an instance in an Auto Scaling group, you can temporarily suppress application status checks for that instance so that Amazon EC2 Auto Scaling does not terminate it during the window. For more information about suppressing application status checks, see [In-place patching and maintenance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/application-status-checks.html#asc-in-place-patching-and-maintenance) in the *Amazon EC2 User Guide*.
