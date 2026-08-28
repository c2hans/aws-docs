---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-using-managed-rule-groups-console.html
---

# Working with AWS managed rule groups in the Network Firewall console
<a name="nwfw-using-managed-rule-groups-console"></a>

Through the console, you access managed rule group information when you add and edit rules in your firewall policies. Through the APIs and the command line interface (CLI), you can directly request managed rule group information.

When you use a managed rule group in your firewall policy, you can edit the following setting:
+ **Set rule actions to alert** – Managed rule groups are designed to block traffic with `drop` rules. This setting in the API matches the **Run in alert mode** setting in the console. This overrides all rule actions in the rule group to `alert` instead. This is useful for testing a rule group before using it to control traffic.

To edit the managed rule group alert settings in your firewall policy:

------
#### [ Console ]

After you add the managed rule group to your firewall policy, from the **Policies** page, choose the firewall policy you just created. This takes you to the policy detail page where you can edit aspects of the policy, and view details about the policy.

In the **Network Firewall rule groups** tab, in the **Stateful rule groups** section, choose the rule group that you'd like to run in alert mode, then from the **Actions** drop-down menu, choose **Rule group details**. For the **Run in alert mode** setting, toggle to **Enabled** to run the rule group in alert mode.

------
#### [ CLI ]

Use the [StatefulRuleGroupOverride](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatefulRuleGroupOverride.html) setting in a `StatefulRuleGroupReference`.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
