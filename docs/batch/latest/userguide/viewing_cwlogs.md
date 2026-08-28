---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/viewing_cwlogs.html
---

# Tutorial: View CloudWatch Logs
<a name="viewing_cwlogs"></a>

You can view and search CloudWatch Logs logs in the AWS Management Console.

**Note**
It might take a few minutes for data to display in CloudWatch Logs.

**To view your CloudWatch Logs data**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation pane, choose **Logs**, then choose **Log groups**.
![CloudWatch console log groups](http://docs.aws.amazon.com/batch/latest/userguide/images/cwl-log-groups.png)

1. Choose a log group to view.
![CloudWatch console log streams](http://docs.aws.amazon.com/batch/latest/userguide/images/cw_log_stream.png)

1. Choose a log stream to view. By default, the streams are identified by the first 200 characters of the job name and the Amazon ECS task ID.
**Tip**
To download log stream data, choose **Actions**.
![CloudWatch console log events](http://docs.aws.amazon.com/batch/latest/userguide/images/cw_log_events.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
