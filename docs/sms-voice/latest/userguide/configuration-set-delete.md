---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-delete.html
---

# Delete a configuration set in AWS End User Messaging SMS
<a name="configuration-set-delete"></a>

Use the AWS End User Messaging SMS console or AWS CLI to delete a configuration set.

------
#### [ Deleting a configuration set (Console) ]

To delete a configuration set using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Configuration sets**.

1. Select the **Configuration set** you want to delete and then choose **Delete**.

------
#### [ Deleting a configuration set (AWS CLI) ]

You can use the [delete-configuration-set](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/delete-configuration-set.html) command to delete a configuration set.

```
$ aws pinpoint-sms-voice-v2 delete-configuration-set \
> --configuration-set-name {{configurationSet}}
```

In the preceding command, replace {{configurationSet}} with the name of the configuration set that you want to delete.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
