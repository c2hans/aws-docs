---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/suspend-scheduled-scaling.html
---

# Turn off scheduled scaling for a scalable target
<a name="suspend-scheduled-scaling"></a>

You can temporarily turn off scheduled scaling without deleting your scheduled actions. For more information, see [Suspend and resume scaling for Application Auto Scaling](application-auto-scaling-suspend-resume-scaling.md).

**To suspend scheduled scaling**
Suspend scheduled scaling on a scalable target by using the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command with the `--suspended-state` option, and specifying `true` as the value of the `ScheduledScalingSuspended` attribute, as shown in the following example.

**Linux, macOS, or Unix**

```
aws application-autoscaling register-scalable-target --service-namespace {{rds}} \
  --scalable-dimension {{rds:cluster:ReadReplicaCount}} --resource-id {{cluster:my-db-cluster}} \
  --suspended-state '{"ScheduledScalingSuspended": true}'
```

**Windows**

```
aws application-autoscaling register-scalable-target --service-namespace {{rds}} ^
  --scalable-dimension {{rds:cluster:ReadReplicaCount}} --resource-id {{cluster:my-db-cluster}} ^
  --suspended-state "{\"ScheduledScalingSuspended\": true}"
```

**Output**
If the command succeeds, it returns the ARN of the scalable target. The following is example output.

```
{
    "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
}
```

**To resume scheduled scaling**
To resume scheduled scaling, run the **register-scalable-target** command again, specifying `false` as the value for `ScheduledScalingSuspended`.
