---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-create.html
---

# Create a configuration set in AWS End User Messaging SMS
<a name="configuration-set-create"></a>

Use the AWS End User Messaging SMS console or AWS CLI to create a configuration set. After you have created a configuration set you should add an [event destination](configuration-sets-event-destinations.md#configuration-sets-event-destinations.title) and [protect configuration](protect-configuration.md#protect-configuration.title).

------
#### [ Creating a configuration set (Console) ]

To create a configuration set using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Configuration sets** and then **Create configuration set**.

1. For **Configuration set name** enter a descriptive name for the configuration set.

1. Choose **Create configuration set**.

------
#### [ Creating a configuration set (AWS CLI) ]

You can use the [create-configuration-set](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/create-configuration-set.html) command to create a new configuration set.

```
$ aws pinpoint-sms-voice-v2 create-configuration-set \
> --configuration-set-name {{configurationSet}}
```

In the preceding command, replace {{configurationSet}} with the name of the configuration set that you want to create.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
