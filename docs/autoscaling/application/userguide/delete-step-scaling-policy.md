---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/delete-step-scaling-policy.html
---

# Delete a step scaling policy for Application Auto Scaling using the AWS CLI
<a name="delete-step-scaling-policy"></a>

When you no longer need a step scaling policy, you can delete it. To delete both the scaling policy and the associated CloudWatch alarm, complete the following tasks.

**To delete your scaling policy**
Use the [delete-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/delete-scaling-policy.html) command.

**Linux, macOS, or Unix**

```
aws application-autoscaling delete-scaling-policy --service-namespace {{ecs}} \
  --scalable-dimension {{ecs:service:DesiredCount}} \
  --resource-id {{service/my-cluster/my-service}} \
  --policy-name {{my-step-scaling-policy}}
```

**Windows**

```
aws application-autoscaling delete-scaling-policy --service-namespace {{ecs}} ^
  --scalable-dimension {{ecs:service:DesiredCount}} ^
  --resource-id {{service/my-cluster/my-service}} ^
  --policy-name {{my-step-scaling-policy}}
```

**To delete the CloudWatch alarm**
Use the [delete-alarms](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/delete-alarms.html) command. You can delete one or more alarms at a time. For example, use the following command to delete the `Step-Scaling-AlarmHigh-ECS:service/my-cluster/my-service` and `Step-Scaling-AlarmLow-ECS:service/my-cluster/my-service` alarms.

```
aws cloudwatch delete-alarms --alarm-name {{Step-Scaling-AlarmHigh-ECS:service/my-cluster/my-service}} {{Step-Scaling-AlarmLow-ECS:service/my-cluster/my-service}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
