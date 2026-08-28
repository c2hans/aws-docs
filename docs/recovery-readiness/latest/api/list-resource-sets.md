---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/list-resource-sets.html
---

# List resource sets
<a name="list-resource-sets"></a>

The following is an example of a request to list the resource sets in an account, and the response.

```
aws route53-recovery-readiness --region us-west-2 list-resource-sets
```

```
{
    "ResourceSets": [
        {
            "ResourceSetArn": "arn:aws:route53-recovery-readiness::888888888888:resource-set/sample-resource-set",
            "ResourceSetName": "sample-resource-set",
            "Resources": [
                {
                    "ReadinessScopes": [],
                    "ResourceArn": "arn:aws:ec2:us-west-2:888888888888:volume/vol-014869e6063ed547b"
                },
                {
                    "ReadinessScopes": [],
                    "ResourceArn": "arn:aws:ec2:ap-southeast-1:888888888888:volume/vol-0bc095e048255a901"
                }
            ],
            "Tags": {}
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
