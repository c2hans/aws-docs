---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorial-create-ami-terraform-permissions.html
---

# Required permissions
<a name="tutorial-create-ami-terraform-permissions"></a>

You need the following permissions to deploy a custom AMI with Terraform:
+ assume the ParallelCluster API role, which is in charge of interacting with the ParallelCluster API
+ describe the CloudFormation stack of the ParallelCluster API, to verify it exists and retrieve its parameters and outputs

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:sts::{{111122223333}}:role/PCAPIUserRole-*",
            "Effect": "Allow",
            "Sid": "AssumePCAPIUserRole"
        },
        {
            "Action": [
                "cloudformation:DescribeStacks"
            ],
            "Resource": "arn:aws:cloudformation:{{us-east-1}}:{{111122223333}}:stack/*",
            "Effect": "Allow",
            "Sid": "CloudFormation"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
