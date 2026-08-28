---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-cloud-watch-creating-role.html
---

# IAM policy for Amazon CloudWatch
<a name="configuration-sets-cloud-watch-creating-role"></a>

Use the following example to create a policy for sending events to a CloudWatch group.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:DescribeLogStreams",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{log-group-name}}:*"
            ]
        }
    ]
}
```

------

For more information about IAM policies, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.

The following example statement uses the, optional but recommended, `SourceAccount` and `SourceArn` conditions to check that only the AWS End User Messaging SMS owner account has access to the configuration set. In this example, replace {{accountId}} with your AWS account id, {{region}} with the AWS Region name and {{ConfigSetName}} with the name of the Configuration Set.

After you create the policy, create a new IAM role, and then attach the policy to it. When you create the role, also add the following trust policy to it:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Principal": {
            "Service": "sms-voice.amazonaws.com"
        },
        "Action": "sts:AssumeRole",
        "Condition": {
            "StringEquals": {
                "aws:SourceAccount": "{{111122223333}}"
            },
            "ArnLike": {
                "aws:SourceArn": "arn:aws:sms-voice:{{us-east-1}}:{{111122223333}}:configuration-set/{{ConfigSetName}}"
            }
        }
    }
}
```

------

For more information about creating IAM roles, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
