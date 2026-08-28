---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id-shared.html
---

# List shared sender IDs with the AWS CLI
<a name="sender-id-shared"></a>

You can use the [describe-sender-ids](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-sender-ids.html) or the [AWS RAM console](https://console.aws.amazon.com/ram) to view sender IDs shared with your account. For more information about shared resources, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md).

**To list all sender IDs shared with your account using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 describe-sender-ids --owner {{SHARED}}
  ```

In the preceding command, replace {{SHARED}} with {{SELF}} to list the sender Ids owned by your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
