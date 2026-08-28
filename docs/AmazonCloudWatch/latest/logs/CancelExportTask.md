---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CancelExportTask.html
---

# Cancel an export task (CLI)
<a name="CancelExportTask"></a>

You can cancel an export task if it's in a `PENDING` or `RUNNING` state.

**To cancel an export task using the AWS CLI**
At a command prompt, use the following [cancel-export-task](https://docs.aws.amazon.com/cli/latest/reference/logs/cancel-export-task.html) command:

```
aws logs --profile CWLExportUser cancel-export-task --task-id "{{cda45419-90ea-4db5-9833-aade86253e66}}"
```

You can use the [describe-export-tasks](https://docs.aws.amazon.com/cli/latest/reference/logs/describe-export-tasks.html) command to verify that the task was canceled successfully.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
