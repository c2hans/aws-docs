---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatefulRule.html
---

# StatefulRule
<a name="API_StatefulRule"></a>

A single Suricata rules specification, for use in a stateful rule group. Use this option to specify a simple Suricata rule with protocol, source and destination, ports, direction, and rule options. For information about the Suricata `Rules` format, see [Rules Format](https://suricata.readthedocs.io/en/suricata-8.0.3/rules/intro.html).

## Contents
<a name="API_StatefulRule_Contents"></a>

 ** Action **   <a name="networkfirewall-Type-StatefulRule-Action"></a>
Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria. For all actions, Network Firewall performs the specified action and discontinues stateful inspection of the traffic flow.
The actions for a stateful rule are defined as follows:
+  **PASS** - Permits the packets to go to the intended destination.
+  **DROP** - Blocks the packets from going to the intended destination and sends an alert log message, if alert logging is configured in the [Firewall](API_Firewall.md) [LoggingConfiguration](API_LoggingConfiguration.md).
+  **ALERT** - Sends an alert log message, if alert logging is configured in the [Firewall](API_Firewall.md) [LoggingConfiguration](API_LoggingConfiguration.md).

  You can use this action to test a rule that you intend to use to drop traffic. You can enable the rule with `ALERT` action, verify in the logs that the rule is filtering as you want, then change the action to `DROP`.
+  **REJECT** - Drops traffic that matches the conditions of the stateful rule, and sends a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and an RST bit contained in the TCP header flags. REJECT is available only for TCP traffic. This option doesn't support FTP or IMAP protocols.
Type: String
Valid Values: `PASS | DROP | ALERT | REJECT`
Required: Yes

 ** Header **   <a name="networkfirewall-Type-StatefulRule-Header"></a>
The stateful inspection criteria for this rule, used to inspect traffic flows.
Type: [Header](API_Header.md) object
Required: Yes

 ** RuleOptions **   <a name="networkfirewall-Type-StatefulRule-RuleOptions"></a>
Additional options for the rule. These are the Suricata `RuleOptions` settings.
Type: Array of [RuleOption](API_RuleOption.md) objects
Required: Yes

## See Also
<a name="API_StatefulRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatefulRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatefulRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatefulRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
