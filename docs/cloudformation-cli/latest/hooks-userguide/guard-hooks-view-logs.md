---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-view-logs.html
---

# View logs for the Guard Hooks in your account
<a name="guard-hooks-view-logs"></a>

When you activate a Guard Hook, you can specify an Amazon S3 bucket as the destination for the Hook output report. Once activated, the Hook automatically stores the results of your Guard rule validations in the specified bucket. You can then view these results in the Amazon S3 console.

## View Guard Hook logs in the Amazon S3 console
<a name="guard-hooks-view-logs-console"></a>

**To view the Guard Hook output log file**

1. Sign-in to the [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. On the navigation bar at the top of the screen, choose your AWS Region.

1. Choose **Buckets**.

1. Choose the bucket you selected for your Guard output report.

1. Choose the desired validation output report log file.

1. Choose whether you want to **Download** the file or **Open** it to view.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
