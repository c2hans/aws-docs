---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/accessing-firehose-data-delivery-logs.html
---

# Access CloudWatch logs for Amazon Data Firehose
<a name="accessing-firehose-data-delivery-logs"></a>

You can view the error logs related to Amazon Data Firehose data delivery failure using the Amazon Data Firehose console or the CloudWatch console. The following procedures show you how to access error logs using these two methods.

**To access error logs using the Amazon Data Firehose console**

1. Sign in to the AWS Management Console and open the Firehose console at https://console.aws.amazon.com/firehose

1. On the navigation bar, choose an AWS Region.

1. Choose a Firehose stream name to go to the Firehose stream details page.

1. Choose **Error Log** to view a list of error logs related to data delivery failure.

**To access error logs using the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. On the navigation bar, choose a Region.

1. In the navigation pane, choose **Logs**.

1. Choose a log group and log stream to view a list of error logs related to data delivery failure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
