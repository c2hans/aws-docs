---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2-start-stop-match-tags.html
---

# EC2: Start or stop instances based on matching principal and resource tags
<a name="reference_policies_examples_ec2-start-stop-match-tags"></a>

This example shows how you might create an identity-based policy that allows a principal to start or stop an Amazon EC2 instance when the instance's resource tag and the principal's tag have the same value for the tag key `CostCenter`. This policy grants the permissions necessary to complete this action programmatically from the AWS API or AWS CLI. To use this policy, replace the {{italicized placeholder text}} in the example policy with your own information. Then, follow the directions in [create a policy](access_policies_create.md) or [edit a policy](access_policies_manage-edit.md).

**Note**
As a best practice, attach policies with the `aws:PrincipalTag` condition key to IAM groups, for the case where some users might have the specified tag and some might not.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "ec2:startInstances",
            "ec2:stopInstances"
        ],
        "Resource": "*",
        "Condition": {"StringEquals":
            {"aws:ResourceTag/CostCenter": "${aws:PrincipalTag/{{CostCenter}}}"}}
    }
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
