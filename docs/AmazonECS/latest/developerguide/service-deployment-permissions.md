---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment-permissions.html
---

# Permissions required for viewing Amazon ECS service deployments
<a name="service-deployment-permissions"></a>

 When you follow the best practice of granting least privilege, you need to add additional permissions in order to view service deployments in the console.

You need access to the following actions:
+ ListServiceDeployments
+ DescribeServiceDeployments
+ DescribeServiceRevisions

You need access to the following resources:
+ Service
+ Service deployment
+ Service revision

The following example policy contains the required permissions, and limits the actions to a specified service.

Replace the `account`, `cluster-name`, and `service-name` with your values.

------
#### [ JSON ]

****

```
{
"Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "ecs:ListServiceDeployments",
            "ecs:DescribeServiceDeployments",
            "ecs:DescribeServiceRevisions"
        ],
        "Resource": [
            "arn:aws:ecs:us-east-1:123456789012:service/cluster-name/service-name",
            "arn:aws:ecs:us-east-1:123456789012:service-deployment/cluster-name/service-name/*",
            "arn:aws:ecs:us-east-1:123456789012:service-revision/cluster-name/service-name/*"
            ]
        }
   ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
