---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-view.html
---

# View all configuration sets in AWS End User Messaging SMS
<a name="configuration-set-view"></a>

Use the AWS CLI to view your configuration sets.

------
#### [ List configuration sets (AWS CLI) ]

You can use the [describe-configuration-sets](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-configuration-sets.html) command to view information about the configuration sets in your AWS End User Messaging SMS account.

**To view a list of the configuration sets in your account using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 describe-configuration-sets
  ```

------
#### [ Describe a configuration set (AWS CLI) ]

You can use the [describe-configuration-sets](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-configuration-sets.html) command to view information about a configuration set in your AWS End User Messaging SMS account.

**To view information about specific configuration sets using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 describe-configuration-sets \
  > --configuration-set-names {{configurationSet}}
  ```

In the preceding command, replace {{configurationSet}} with the name of the configuration set that you want to find the details of. You can also specify multiple configuration sets by separating the name of each configuration set with a space.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
