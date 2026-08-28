---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/managing-recorder_console-start.html
---

# Starting the customer managed configuration recorder
<a name="managing-recorder_console-start"></a>

You can use the AWS Config console or the AWS CLI start the customer managed configuration recorder.

------
#### [ To start the customer managed configuration recorder (Console) ]

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home).

1. Choose **Settings** in the navigation pane.

1. On the **Customer managed recorder** tab, choose **Start recording**. When prompted, choose **Confirm**.

------
#### [ To start the customer managed configuration recorder (CLI) ]

Use the [`start-configuration-recorder`](http://docs.aws.amazon.com/cli/latest/reference/configservice/start-configuration-recorder.html) command:

```
$ aws configservice start-configuration-recorder --configuration-recorder-name {{configRecorderName}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
