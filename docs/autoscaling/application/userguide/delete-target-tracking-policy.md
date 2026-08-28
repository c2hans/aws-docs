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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
