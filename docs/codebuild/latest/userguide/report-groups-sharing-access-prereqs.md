---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/report-groups-sharing-access-prereqs.html
---

# Access report groups shared with you
<a name="report-groups-sharing-access-prereqs"></a>

To access a shared report group, a consumer's IAM role requires the `BatchGetReportGroups` permission. You can attach the following policy to their IAM role:

```
{
    "Effect": "Allow",
    "Resource": [
        "*"
    ],
    "Action": [
        "codebuild:BatchGetReportGroups"
    ]
}
```

 For more information, see [Using identity-based policies for AWS CodeBuild](auth-and-access-control-iam-identity-based-access-control.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
