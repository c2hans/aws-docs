---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/security-iam-permissions-console-logs.html
---

# Permissions required to view compute logs in the console
<a name="security-iam-permissions-console-logs"></a>

To view the logs in the Commands action on the CodePipeline console, the console role must have permissions. To view logs in the console, add the `logs:GetLogEvents` permissions to the console role.

In the console role policy statement, scope down the permissions to the pipeline level as shown in the following example.

```
{
    "Effect": "Allow",
    "Action": [
        "Action": "logs:GetLogEvents"
    ],
    "Resource": "arn:aws:logs:*:{{YOUR_AWS_ACCOUNT_ID}}:log-group:/aws/codepipeline/{{YOUR_PIPELINE_NAME}}:*"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
