---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/administrative-role.html
---

# Administrative role
<a name="administrative-role"></a>

Landing Zone Accelerator on AWS uses an IAM role with administrative privileges to manage the orchestration of resources across the environment. We recommend you activate AWS Control Tower and use the `AWSControlTowerExecution` role. You can also leverage other existing cross-account access roles such as `OrganizationAccountAccessRole`, which is the default cross-account role that’s utilized by AWS Organizations.

If you prefer using custom roles, a role with administrative privileges must be deployed in each member account managed by the Landing Zone Accelerator on AWS. These roles must have a trust relationship defined that grants the `sts:AssumeRole` permission to the IAM service role for the Landing Zone Accelerator on AWS CodeBuild projects. The following demonstrates the ARN changes based on the [partition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html#cfn-pseudo-param-partition) of the resource:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:$PARTITION:iam::$MANAGEMENT_ACCOUNT_ID:root"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
