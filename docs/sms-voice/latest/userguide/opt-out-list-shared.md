---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-shared.html
---

# List shared opt-out lists with the AWS CLI
<a name="opt-out-list-shared"></a>

You can use the [describe-opt-out-lists](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.html) to view opt-out lists shared with your account. For more information about shared resources, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md).

**To list all opt-out lists shared with your account using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 describe-opt-out-lists --owner {{SHARED}}
  ```

In the preceding command, replace {{SHARED}} with {{SELF}} to list the opt-out lists owned by your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
