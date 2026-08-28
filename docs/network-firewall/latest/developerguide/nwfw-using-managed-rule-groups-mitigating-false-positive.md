---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-using-managed-rule-groups-mitigating-false-positive.html
---

# Troubleshooting AWS managed rule groups in Network Firewall
<a name="nwfw-using-managed-rule-groups-mitigating-false-positive"></a>

As a best practice, before using a rule group in production, with logging enabled, run the managed rule group in **alert mode** if you're using an intrusion detection system (IDS), or in **drop mode** if you use an intrusion prevention system (IPS) in a non-production environment. Either mode sends alert messages to the logs for traffic that doesn't pass inspection. For more information, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).

Running a managed rule group in either alert mode or drop mode allows you to do a dry run with alert logs that show you what the resulting behavior would be before you commit to making changes to your traffic. Evaluate the rule group using Network Firewall logs. When you're satisfied that the rule group does what you want it to do, disable test mode on the group.

**Mitigating false-positive scenarios**
If you are encountering false-positive scenarios with AWS managed rule groups, perform the following steps:

1. In the firewall policy's AWS managed rule group settings in the Network Firewall console, override the actions in the rules of the rule groups by enabling **Run in alert mode**. This stops them from blocking legitimate traffic.

1. Use [Network Firewall logs](logging-monitoring.md) to identify which AWS managed rule group is triggering the false positive.

1. In the AWS Network Firewall console, edit the firewall policy, and locate the AWS managed rule group that you've identified. Then, disable **Run in alert mode** for the rules that aren't causing the false positive, and leave the rule group that is causing the false positive in alert mode.

For more information about a rule in an AWS managed rule group, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
