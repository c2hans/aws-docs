---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/batch_sns_test_rule.html
---

# Tutorial: Test your rule
<a name="batch_sns_test_rule"></a>

To test your rule, submit a job that exits shortly after it starts with a non-zero exit code. If your event rule is configured correctly, you should receive an email message within a few minutes with the event text.

**To test a rule**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. Submit a new AWS Batch job. For more information, see [Tutorial: submit a job](submit_job.md). For the job's command, substitute this command to exit the container with an exit code of 1.

   ```
   /bin/sh, -c, 'exit 1'
   ```

1. Check your email to confirm that you received an email alert for the failed job notification.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
