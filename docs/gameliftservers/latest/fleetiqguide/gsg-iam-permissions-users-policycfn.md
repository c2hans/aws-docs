---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users-policycfn.html
---

# Additional permissions for CloudFormation
<a name="gsg-iam-permissions-users-policycfn"></a>

If you use CloudFormation to manage your game hosting resources, add the CloudFormation permissions to the policy syntax.

```
    {
      "Action": [
        "autoscaling:DescribeLifecycleHooks",
        "autoscaling:DescribeNotificationConfigurations",
        "ec2:DescribeLaunchTemplateVersions"
      ]
      "Effect": "Allow",
      "Resource": "*"
    }
```
