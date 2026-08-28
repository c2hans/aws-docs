---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-create.html
---

# Create an opt-out list in AWS End User Messaging SMS
<a name="opt-out-list-create"></a>

Use the AWS End User Messaging SMS console or AWS CLI to create an opt-out list.

------
#### [ Create opt-out list (Console) ]

To create an opt-out list using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Opt-out lists**.

1. On the **Opt-out lists** page, choose an opt-out list and then choose **Edit**.

1. On the **List details** page enter a **List name**.

1. Choose **Create list**.

------
#### [ Create opt-out list (AWS CLI) ]

At the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 create-opt-out-list \
> --opt-out-list-name {{optOutListName}}
```

In the preceding example, replace {{optOutListName}} with a name that makes the opt-out list easy to identify.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
