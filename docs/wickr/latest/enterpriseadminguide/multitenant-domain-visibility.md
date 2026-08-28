---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/multitenant-domain-visibility.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Multitenant Domain Visibility
<a name="multitenant-domain-visibility"></a>

Super administrators can hide local domains from lower-level administrators.

**To hide local domains**

1. In the navigation pane of the Wickr Super Administrator Console, choose **Global Federation**.

1. In the **Local Domains for Federation**, turn off the toggle next to **Show Domains to Admin**.

 Turning off the toggle hides the **Learn More** prompt in the team directory, which prevents the viewing of other local domains associated with other networks in the Enterprise deployment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
