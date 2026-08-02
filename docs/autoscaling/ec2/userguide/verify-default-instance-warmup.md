---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/verify-default-instance-warmup.html
---

# Verify the default instance warmup time for a group
<a name="verify-default-instance-warmup"></a>

Use the following procedure to verify the default instance warmup time for an Auto Scaling group using the AWS CLI.

**To verify the default instance warmup time for an Auto Scaling group**
Use the following [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) command. Replace {{my-asg}} with the name of your Auto Scaling group.

```
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-name {{my-asg}}
```

The following is an example response.

```
{
    "AutoScalingGroups": [
        {
            "AutoScalingGroupName": "my-asg",
            "AutoScalingGroupARN": "arn",
            ...
            "DefaultInstanceWarmup": 120
        }
    ]
}
```
