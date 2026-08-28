---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/modify-the-allowed-and-denied-ip-sets-optional.html
---

# Modify the allowed and denied IP sets (optional)
<a name="modify-the-allowed-and-denied-ip-sets-optional"></a>

After deploying this solution’s CloudFormation stack, you can manually modify the allowed and denied IP sets to add or remove IP addresses as necessary.

1. Sign in to the [AWS WAF console](https://console.aws.amazon.com/wafv2/).

1. In the left navigation pane, choose **IP Sets**.

1. Choose **IP set for Allowed List** and add IP addresses from trusted sources.

1. Choose **IP set for Denied List** and add IP addresses you want to block.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
