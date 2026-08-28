---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/auth-and-access-control-using-tags.html
---

# Using tags to control access to Amazon CodeGuru Profiler resources
<a name="auth-and-access-control-using-tags"></a>

Conditions in IAM policy statements are part of the syntax that you can use to specify permissions for CodeGuru Profiler profiling group-based actions. You can create a policy that allows or denies actions for profiling groups based on the tags associated with those profiling groups, and then apply those policies to the IAM groups you configure for managing IAM users. For information about applying tags to a profiling group, see [Tagging profiling groups](tagging-profiling-groups.md).

**Example 1: Give all CodeGuru Profiler permissions to the role.**
The first statement gives all CodeGuru Profiler permissions to all groups with the role. The second statement provides deny permissions to delete any profiling group with tag `{stage: prod}` from the role.
****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "codeguru-profiler:*"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "codeguru-profiler:DeleteProfilingGroup"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/stage": "prod"
                }
            },
            "Resource": "*"
        }
    ]
}
```

**Example 2: Deny tagging and untagging a resource.**
The following policy prevents a role from tagging or untagging a resource if the resource is marked with the tag `{stage: prod}`.
****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "codeguru-profiler:*"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "codeguru-profiler:TagResource",
                "codeguru-profiler:UntagResource"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/stage": "prod"
                }
            },
            "Resource": "*"
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
