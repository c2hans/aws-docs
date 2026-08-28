---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs-decompression-disabling-console.html
---

# Disable decompression on Firehose stream
<a name="writing-with-cloudwatch-logs-decompression-disabling-console"></a>

To disable decompression on a data stream using the AWS Management Console

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. Choose **Amazon Data Firehose** in the navigation pane.

1. Choose the Firehose stream you wish to edit.

1. On **Firehose stream details** page, choose the **Configuration** tab.

1. In the **Transform and convert records** section, choose **Edit**.

1. Under **Decompress source records from Amazon CloudWatch Logs**, clear **Turn on decompression** and then choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
