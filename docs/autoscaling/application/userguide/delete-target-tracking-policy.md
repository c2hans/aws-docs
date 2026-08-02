---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/delete-target-tracking-policy.html
---

# Delete a target tracking scaling policy for Application Auto Scaling using the AWS CLI
<a name="delete-target-tracking-policy"></a>

When you are finished with a target tracking scaling policy, you can delete it using the [delete-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/delete-scaling-policy.html) command.

The following command deletes the specified target tracking scaling policy for the specified Spot Fleet request. It also deletes the CloudWatch alarms that Application Auto Scaling created on your behalf.

**Linux, macOS, or Unix**

```
aws application-autoscaling delete-scaling-policy --service-namespace {{ec2}} \
  --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} \
  --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}} \
  --policy-name {{cpu50-target-tracking-scaling-policy}}
```

**Windows**

```
aws application-autoscaling delete-scaling-policy --service-namespace {{ec2}} ^
  --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} ^
  --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}} ^
  --policy-name {{cpu50-target-tracking-scaling-policy}}
```
