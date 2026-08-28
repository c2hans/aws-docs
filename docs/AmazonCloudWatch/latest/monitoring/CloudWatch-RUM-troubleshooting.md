---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-troubleshooting.html
---

# Troubleshooting CloudWatch RUM
<a name="CloudWatch-RUM-troubleshooting"></a>

This section contains tips to help you troubleshoot CloudWatch RUM.

## There is no data for my application
<a name="CloudWatch-RUM-troubleshooting-nodata"></a>

First, make sure that the code snippet has been correctly inserted into your application. For more information, see [Inserting the CloudWatch app monitor code snippet into your application](CloudWatch-RUM-get-started-insert-code-snippet.md).

If that is not the issue, then maybe there has been no traffic to your application yet. Generate some traffic by accessing your application the same way that a user would.

## Data has stopped being recorded for my application
<a name="CloudWatch-RUM-troubleshooting-nonewdata"></a>

Your application might have been updated and now no longer contains a CloudWatch RUM code snippet. Check your application code.

Another possibility is that someone may have updated the code snippet but then didn't insert the updated snippet into the application. Find the current correct code snippet by following the directions in [How do I find a code snippet that I've already generated?](CloudWatch-RUM-find-code-snippet.md) and compare it to the code snippet that is pasted into your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
