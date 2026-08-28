---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/url-redirection-enable.html
---

# Enable host-to-client URL redirection
<a name="url-redirection-enable"></a>

Complete the following steps to enable host-to-client URL redirection on a new or existing stack.

**To enable host-to-client URL redirection**

1. Open the WorkSpaces Applications AWS Management Console.

1. In the left navigation pane, choose **Stacks**.

1. Do one of the following:
   + To configure a new stack, choose **Create Stack**.
   + To modify an existing stack, select the stack and choose **Edit**.

1. In the **Content Redirection** section, select **Enable host to client URL redirection**.

1. Configure the URL patterns and optional exception list as described in the following sections.

1. Choose **Update** to save your stack configuration.

**Note**
After you save the stack settings, the changes take effect when a new streaming session is created. Existing sessions are not affected.

After you enable the feature, two configuration fields become available: **Configure host to client URL patterns** (required) and **Configure exception list** (optional).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
