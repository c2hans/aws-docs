---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/lambda-debug.html
---

# Debugging a Lambda function using CloudWatch Logs logs
<a name="lambda-debug"></a>

[Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) is a tool for tracking API calls and metrics that you can use to help debug your Lambda functions. When you test your bot in the console or with API calls, CloudWatch logs each step of the conversation. If you use a print function in your Lambda code, CloudWatch displays it as well.

**To view CloudWatch logs for your Lambda function**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Under the **Logs** menu in the left side bar, select **Log groups**.

1. Select your Lambda function log group, which should be of the format `/aws/lambda/{{function-name}}`.

1. The list of **Log streams** contains a log for each session with a bot. Choose a log stream to view it.

1. In the list of **Log events**, select the right arrow next to the **Timestamp** to expand the details for that event. Anything you print from your Lambda code will appear as a log event. Use this information to debug your code.

1. After you debug your code, remember to **Deploy** the Lambda function and, if you are using the console, to reload the **Test** window before re-testing the bot's behavior.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
