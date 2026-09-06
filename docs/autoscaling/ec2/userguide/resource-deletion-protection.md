---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/resource-deletion-protection.html
---

# Configure deletion protection for your Amazon EC2 Auto Scaling resources
<a name="resource-deletion-protection"></a>

 Protect your Amazon EC2 Auto Scaling infrastructure from accidental deletion by configuring multiple layers of protection. Auto Scaling provides several approaches to prevent unwanted resource deletion for your Auto Scaling groups and the Amazon EC2 instances that it manages.

**Topics**
+ [Configure Auto Scaling group deletion protection](#asg-deletion-protection)
+ [Control deletion permissions with IAM policies](#deletion-protection-iam-policies)

## Configure Auto Scaling group deletion protection
<a name="asg-deletion-protection"></a>

 Deletion protection is a resource-level setting that prevents your Amazon EC2 Auto Scaling group from accidental deletion. When enabled, deletion protection blocks the [ DeleteAutoScalingGroup ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteAutoScalingGroup.html) API operation from succeeding, requiring you to first update the deletion protection setting to a less restrictive level before you can delete the Auto Scaling group.

Amazon EC2 Auto Scaling offers three levels of deletion protection:

**None** (default)
 No deletion protection is enabled, meaning your Auto Scaling group can be deleted with or without using the `ForceDelete` option. When `ForceDelete` is used, all Amazon EC2 instances managed by your Auto Scaling group will also be forcibly terminated without executing termination lifecycle hooks.

**Prevent force deletion**
 Your Auto Scaling group can't be deleted when using the `ForceDelete` option. This configuration allows deletion of empty Auto Scaling groups (groups with no instances). This option is recommended for production workloads where you want to prevent mass instance termination but allow cleanup of empty groups.

**Prevent all deletion**
 Your Auto Scaling group can't be deleted regardless of whether the `ForceDelete` option is used. This option provides the strongest protection against accidental deletion. It requires explicitly disabling deletion protection before your Auto Scaling group can be deleted. This is recommended for mission-critical Auto Scaling groups that should rarely or never be deleted.

### How deletion protection works
<a name="deletion-protection-how-it-works"></a>

 When you attempt the [ DeleteAutoScalingGroup ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteAutoScalingGroup.html) API operation with deletion protection enabled:

1.  Amazon EC2 Auto Scaling validates the deletion protection setting before processing the request.

1.  If the configured deletion protection level blocks the deletion attempt, Amazon EC2 Auto Scaling returns a `ValidationError`.

1.  Your Auto Scaling group and its Amazon EC2 instances remain unchanged.

1.  You must update the deletion protection setting to a less restrictive level before you can delete your Auto Scaling group.

 Deletion protection does not prevent other operations such as:
+  Updating the Auto Scaling group configuration.
+  Terminating individual instances.
+  Scaling operations (manual or automatic).
+  Suspending or resuming processes.

 For more information on how to gracefully handle instance termination, see [Design your applications to gracefully handle instance termination](gracefully-handle-instance-termination.md).

### Configure deletion protection
<a name="configure-deletion-protection"></a>

 You can set deletion protection when you create an Auto Scaling group or update the setting on an existing Auto Scaling group.

------
#### [ Console ]

**To create an Auto Scaling group with deletion protection**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Choose **Create Auto Scaling group**.

1. Complete the configuration steps for your Auto Scaling group.

1. On the **Configure group size and scaling** page, expand **Additional settings**.

1. For **Auto Scaling group deletion protection**, choose your desired protection level:
   + **None** - No deletion protection (default)
   + **Prevent force deletion** - Block force delete operations
   + **Prevent all deletion** - Block all delete operations

1. Complete the remaining steps to create your Auto Scaling group.

**To update deletion protection on an existing Auto Scaling group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

1. Choose **Actions**, **Edit**.

1. Under **Additional settings**, update the **Auto Scaling group deletion protection** setting.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To create an Auto Scaling group with deletion protection**
Use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command with the `--deletion-protection` parameter:

```
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name {{my-asg}} \
    --launch-template LaunchTemplateName={{my-template}},Version='$Latest' \
    --min-size {{1}} \
    --max-size {{5}} \
    --desired-capacity {{2}} \
    --vpc-zone-identifier "{{subnet-12345678,subnet-87654321}}" \
    --deletion-protection {{prevent-force-deletion}}
```

Valid values for `--deletion-protection` are: `none` \| `prevent-force-deletion` \| `prevent-all-deletion`

**To update deletion protection on an existing Auto Scaling group**
Use the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command:

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name {{my-asg}} \
    --deletion-protection {{prevent-all-deletion}}
```

**To disable deletion protection**
Set deletion protection to `none`:

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name {{my-asg}} \
    --deletion-protection {{none}}
```

**To verify deletion protection status**
Use the [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) command:

```
aws autoscaling describe-auto-scaling-groups \
    --auto-scaling-group-names {{my-asg}}
```

------

## Control deletion permissions with IAM policies
<a name="deletion-protection-iam-policies"></a>

 Use AWS Identity and Access Management (IAM) policies to control which users and roles can delete Auto Scaling groups. IAM-based controls provide an additional layer of security by restricting permissions at the identity level.

IAM policies are particularly useful when you want to:
+  Allow different users different levels of access to Auto Scaling operations.
+  Prevent specific users from using the `ForceDelete` option even if they can perform other Auto Scaling operations.
+  Restrict deletion permissions to specific Auto Scaling groups.

 The following policy allows deletion of an Auto Scaling group only if the group has the tag `environment=development`.

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement": [{
      "Effect": "Allow",
      "Action": "autoscaling:DeleteAutoScalingGroup",
      "Resource": "*",
      "Condition": {
          "StringEquals": { "aws:ResourceTag/{{environment}}": "{{development}}" }
      }
   }]
}
```

------

 The following policy uses the `autoscaling:ForceDelete` condition key to control access to the `DeleteAutoScalingGroup` API action. This can prevent certain users from using the `ForceDelete` operation, which terminates all Amazon EC2 instances within an Auto Scaling group.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [{
        "Effect": "Deny",
        "Action": "autoscaling:DeleteAutoScalingGroup",
        "Resource": "*",
        "Condition": {
            "Bool": {
                "autoscaling:ForceDelete": "true"
            }
        }
    }]
}
```

------

 Alternatively, if you are not using condition keys to control access to Auto Scaling groups, you can specify the ARNs of resources in the `Resource` element to control access instead.

 The following policy gives users permissions to use the `DeleteAutoScalingGroup` API action, but only for Auto Scaling groups whose name begins with `devteam-`.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "autoscaling:DeleteAutoScalingGroup",
            "Resource": "arn:aws:autoscaling:{{us-east-1}}:{{111122223333}}:autoScalingGroup:*:autoScalingGroupName/{{devteam-}}*"
        }
    ]
}
```

------

 You can also specify multiple ARNs by enclosing them in a list. Including the UUID ensures that access is granted to the specific Auto Scaling group. The UUID for a new group is different from the UUID for a deleted group with the same name.

```
"Resource": [
    "arn:aws:autoscaling:{{region}}:{{account-id}}:autoScalingGroup:{{uuid}}:autoScalingGroupName/{{devteam-1}}",
    "arn:aws:autoscaling:{{region}}:{{account-id}}:autoScalingGroup:{{uuid}}:autoScalingGroupName/{{devteam-2}}",
    "arn:aws:autoscaling:{{region}}:{{account-id}}:autoScalingGroup:{{uuid}}:autoScalingGroupName/{{devteam-3}}"
]
```

 For additional examples of IAM policies for Amazon EC2 Auto Scaling, including policies that control deletion permissions, see [Identity-based policy examples](security_iam_id-based-policy-examples.md).
