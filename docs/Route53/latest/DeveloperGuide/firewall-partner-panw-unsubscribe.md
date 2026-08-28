---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/firewall-partner-panw-unsubscribe.html
---

# Unsubscribe from Palo Alto Networks
<a name="firewall-partner-panw-unsubscribe"></a>

**Important**
To stop subscription charges, you must remove all PANW rules from your DNS Firewall rule groups in addition to unsubscribing from AWS Marketplace. If you unsubscribe but leave the rules in your rule groups, charges continue until you remove the rules.

**Remove PANW rules from all rule groups**
Use the following procedure to remove PANW rules.

1. Open the Amazon Virtual Private Cloud console.

1. In the navigation pane, choose **DNS Firewall**, then choose **Rule groups**.

1. For each rule group containing Palo Alto Networks rules, select the partner managed rules and choose **Delete**.

1. Confirm deletion.

**Cancel the Marketplace subscription**
Use the following procedure to cancel the subscription.

1. Open the AWS Marketplace console.

1. Choose **Manage subscriptions**.

1. Open the **Delivery method** list and choose **SaaS**.

1. Under **Agreement**, open the **Actions** list and choose **Cancel subscription** next to the Palo Alto Networks product.

1. In the **Cancel subscription** dialog box, enter **confirm**, then choose **Yes, cancel subscription**.

**Note**
If you unsubscribe but leave the rules in your rule groups, charges continue until you remove the rules.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
