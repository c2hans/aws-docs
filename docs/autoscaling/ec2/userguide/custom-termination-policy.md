---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/custom-termination-policy.html
---

# Change the termination policy for an Auto Scaling group
<a name="custom-termination-policy"></a>

To change the termination policy for your Auto Scaling group, use one of the following methods.

------
#### [ Console ]

You can't change the termination policy when you initially create an Auto Scaling group in the Amazon EC2 Auto Scaling console. The default termination policy is used automatically. After your Auto Scaling group has been created, you can replace the default policy with a different termination policy or multiple termination policies listed in the order in which they should apply.

**To change the termination policy for an Auto Scaling group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Details** tab, choose **Advanced configurations**, **Edit**.

1. For **Termination policies**, choose one or more termination policies. If you choose multiple policies, put them in the order that you want them evaluated in.

   You can optionally choose **Custom termination policy** and then choose a Lambda function that meets your needs. If you have created versions and aliases for your Lambda function, you can choose a version or alias from the **Version/Alias** drop-down. To use the unpublished version of your Lambda function, keep **Version/Alias** set to its default. For more information, see [Create a custom termination policy with Lambda](lambda-custom-termination-policy.md).
**Note**
When using multiple policies, their order must be set correctly:
If you use the **Default** policy, it must be the last policy in the list.
If you use a **Custom termination policy**, it must be the first policy in the list.

1. Choose **Update**.

------
#### [ AWS CLI ]

The default termination policy is used automatically unless a different policy is specified.

**To change the termination policy for an Auto Scaling group**
Use one of the following commands:
+ [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html)
+ [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html)

You can use termination policies individually, or combine them into a list of policies. For example, use the following command to update an Auto Scaling group to use the `OldestLaunchConfiguration` policy first and then use the `ClosestToNextInstanceHour` policy.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} --termination-policies "OldestLaunchConfiguration" "ClosestToNextInstanceHour"
```

If you use the `Default` termination policy, make it the last one in the list of termination policies. For example, `--termination-policies "OldestLaunchConfiguration" "Default"`.

To use a custom termination policy, you must first create your termination policy using AWS Lambda. To specify the Lambda function to use as your termination policy, make it the first one in the list of termination policies. For example, `--termination-policies "arn:aws:lambda:us-west-2:123456789012:function:HelloFunction:prod" "OldestLaunchConfiguration"`. For more information, see [Create a custom termination policy with Lambda](lambda-custom-termination-policy.md).

------
