---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-view.html
---

# View the details of an opt-out list in AWS End User Messaging SMS
<a name="opt-out-list-view"></a>

Use the AWS End User Messaging SMS console or AWS CLI to manage your opt-out lists.

------
#### [ View opt-out list (Console) ]

To view an opt-out list using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Opt-out lists**.

1. On the **Opt-out lists** page, choose an opt-out list and view the **Opt-out list details**.

------
#### [ Describe opt-out lists (AWS CLI) ]

You can use the [describe-opt-out-lists](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.html) command to view information about the opt-out lists in your AWS End User Messaging SMS account.

**To view information about all of your opt-out lists using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 describe-opt-out-lists
  ```

You can also view information about specific opt-out lists by using the `OptOutListNames` parameter.

**To view information about specific opt-out lists using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 describe-opt-out-lists \
  > --opt-out-list-names {{optOutListName}}
  ```

  In the preceding command, replace {{optOutListName}} with the name or Amazon Resource Name (ARN) of the opt-out list that you want to find more information about. You can also specify multiple opt-out lists by separating each list name with a space.

  The AWS CLI returns the following information about all of the opt-out lists in your account.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
