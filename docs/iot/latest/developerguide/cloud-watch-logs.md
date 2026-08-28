---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/cloud-watch-logs.html
---

# Monitor AWS IoT using CloudWatch Logs
<a name="cloud-watch-logs"></a>

When [AWS IoT logging is enabled](configure-logging.md), AWS IoT sends progress events about each message as it passes from your devices through the message broker and rules engine. In the [CloudWatch console](https://console.aws.amazon.com/cloudwatch), CloudWatch logs appear in a log group named **AWSIotLogs**.

For more information about CloudWatch Logs, see [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.html). For information about supported AWS IoT CloudWatch Logs, see [CloudWatch Logs AWS IoT log entries](cwl-format.md) .

## Viewing AWS IoT logs in the CloudWatch console
<a name="viewing-logs"></a>

**Note**
The `AWSIotLogsV2` log group is not visible in the CloudWatch console until:
You've enabled logging in AWS IoT. For more info on how to enable logging in AWS IoT, see [Configure AWS IoT logging](configure-logging.md)
Some log entries have been written by AWS IoT operations.

**To view your AWS IoT logs in the CloudWatch console**

1.  Browse to [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/). In the navigation pane, choose **Log groups**.

1. In the **Filter** text box, enter **AWSIotLogsV2** , and then press Enter.

1. Double-click the `AWSIotLogsV2` log group.

1. Choose **Search All**. A complete list of the AWS IoT logs generated for your account is displayed.

1. Choose the expand icon to look at an individual stream.

You can also enter a query in the **Filter events** text box. Here are some interesting queries to try:
+  `{ $.logLevel = "INFO" }`

   Find all logs that have a log level of `INFO`.
+  `{ $.status = "Success" }`

   Find all logs that have a status of `Success`.
+  `{ $.status = "Success" && $.eventType = "GetThingShadow" }`

   Find all logs that have a status of `Success` and an event type of `GetThingShadow`.

For more information about creating filter expressions, see [CloudWatch Logs Queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
