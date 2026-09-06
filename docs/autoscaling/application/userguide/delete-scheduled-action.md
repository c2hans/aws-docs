---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/delete-scheduled-action.html
---

# Delete a scheduled action for Application Auto Scaling using the AWS CLI
<a name="delete-scheduled-action"></a>

When you are finished with a scheduled action, you can delete it.

**To delete your scheduled action**
Use the [delete-scheduled-action](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scheduled-action.html) command. If successful, this command does not return any output.

**Linux, macOS, or Unix**

```
aws application-autoscaling delete-scheduled-action \
  --service-namespace {{ec2}} \
  --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} \
  --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-37294EXAMPLE}} \
  --scheduled-action-name {{my-recurring-action}}
```

**Windows**

```
aws application-autoscaling delete-scheduled-action ^
  --service-namespace {{ec2}} ^
  --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} ^
  --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-37294EXAMPLE}} ^
  --scheduled-action-name {{my-recurring-action}}
```

**To deregister the scalable target**
If you are also finished with the scalable target, you can deregister it. Use the following [deregister-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/deregister-scalable-target.html) command. If there are any scaling policies or scheduled actions that have not yet been deleted, they are deleted by this command. If successful, this command does not return any output.

**Linux, macOS, or Unix**

```
aws application-autoscaling deregister-scalable-target \
  --service-namespace {{ec2}} \
  --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} \
  --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-37294EXAMPLE}}
```

**Windows**

```
aws application-autoscaling deregister-scalable-target ^
  --service-namespace {{ec2}} ^
  --scalable-dimension {{ec2:spot-fleet-request:TargetCapacity}} ^
  --resource-id {{spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-37294EXAMPLE}}
```
