---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/data-protection-configure.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Configuring data protection for a protection pack (web ACL)
<a name="data-protection-configure"></a>

This section provides instructions for configuring data protection for a protection pack (web ACL).

**To configure data protection for a protection pack (web ACL)**

1. Sign in to the AWS Management Console and open the AWS WAF console at [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2).

1. In the navigation pane, choose **protection packs (web ACLs)**.

1. Choose the name of the protection pack (web ACL) that you want to enable data protection for. The console takes you to the protection pack (web ACL)'s description, where you can edit it.

1. On the **Logging and metrics** tab, in the **Data protection settings** pane, choose **Enable** or **Edit**.

1. Choose the scope **Global** and then make your field data protection selections. For each field data protection configuration, you can also specify exceptions to exclude from the protection behavior.

1. When you've completed your selections, choose **Save**. The interface returns to the **Logging and metrics** tab where your selections are summarized.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
