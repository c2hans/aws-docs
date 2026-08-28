---
source_url: https://docs.aws.amazon.com/glue/latest/dg/generating-help-with-q.html
---

# Generating help with Q
<a name="generating-help-with-q"></a>

Q help in the AWS Glue console provides context-aware, step-by-step guidance to help you complete tasks on the console page. When you choose the **Q help** link, Amazon Q generates guidance that is relevant to your current task. You can ask follow-up questions directly in the same panel to get additional help without leaving the page.

**Note**
Q help requires Amazon Q Developer permissions. If your account does not have Amazon Q enabled, help links display as **Info** and open the standard static help panel. The console automatically detects your permissions and adjusts the experience accordingly.

## Disabling or enabling Q help
<a name="disabling-enabling-q-help"></a>

Q help is enabled by default and can be turned off at any time through your console settings.

**To disable Q help**

1. In the AWS Management Console, choose **User Settings**.

1. Choose **See all user settings**.

1. Choose **Edit setting management**.

1. Clear the **Enable Q help links** checkbox.

After you save your changes, help links display as **Info** and open the standard help panel on the right side of the page.

To re-enable Q help, follow the same steps and select the **Enable Q help links** checkbox. The change takes effect immediately.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
