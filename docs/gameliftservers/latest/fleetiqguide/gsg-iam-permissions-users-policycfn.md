---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/fleetiqguide/gsg-iam-permissions-users-policycfn.html
---

# Additional permissions for CloudFormation
<a name="gsg-iam-permissions-users-policycfn"></a>

If you use CloudFormationto manage your game hosting resources, add the CloudFormation permissions to the policy syntax.

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
