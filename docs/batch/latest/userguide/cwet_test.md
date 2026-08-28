---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/cwet_test.html
---

# Tutorial: Test your configuration
<a name="cwet_test"></a>

You can now test your EventBridge configuration by submitting a job to your job queue. If everything is configured properly, your Lambda function is triggered and it writes the event data to a CloudWatch Logs log stream for the function.

**To test your configuration**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. Submit a new AWS Batch job. For more information, see [Tutorial: submit a job](submit_job.md).

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. On the navigation pane, choose **Logs** and select the log group for your Lambda function (for example, **/aws/lambda/**{{my-function}}).

1. Select a log stream to view the event data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
