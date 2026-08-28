---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::FirewallPolicy StatefulEngineOptions
<a name="aws-properties-networkfirewall-firewallpolicy-statefulengineoptions"></a>

Configuration settings for the handling of the stateful rule groups in a firewall policy.

**Important**
Updating any setting in `StatefulEngineOptions` may require a restart of the stateful engine in order to apply the changes. When this occurs, existing connections will be treated according to your stream exception policy configuration.

## Syntax
<a name="aws-properties-networkfirewall-firewallpolicy-statefulengineoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewallpolicy-statefulengineoptions-syntax.json"></a>

```
{
  "[FlowTimeouts](#cfn-networkfirewall-firewallpolicy-statefulengineoptions-flowtimeouts)" : {{FlowTimeouts}},
  "[RuleOrder](#cfn-networkfirewall-firewallpolicy-statefulengineoptions-ruleorder)" : {{String}},
  "[StreamExceptionPolicy](#cfn-networkfirewall-firewallpolicy-statefulengineoptions-streamexceptionpolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewallpolicy-statefulengineoptions-syntax.yaml"></a>

```
  [FlowTimeouts](#cfn-networkfirewall-firewallpolicy-statefulengineoptions-flowtimeouts): {{
    FlowTimeouts}}
  [RuleOrder](#cfn-networkfirewall-firewallpolicy-statefulengineoptions-ruleorder): {{String}}
  [StreamExceptionPolicy](#cfn-networkfirewall-firewallpolicy-statefulengineoptions-streamexceptionpolicy): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-firewallpolicy-statefulengineoptions-properties"></a>

`FlowTimeouts`  <a name="cfn-networkfirewall-firewallpolicy-statefulengineoptions-flowtimeouts"></a>
Configures the amount of time that can pass without any traffic sent through the firewall before the firewall determines that the connection is idle.
*Required*: No
*Type*: [FlowTimeouts](aws-properties-networkfirewall-firewallpolicy-flowtimeouts.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleOrder`  <a name="cfn-networkfirewall-firewallpolicy-statefulengineoptions-ruleorder"></a>
Indicates how to manage the order of stateful rule evaluation for the policy. `DEFAULT_ACTION_ORDER` is the default behavior. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see [Evaluation order for stateful rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html) in the *AWS Network Firewall Developer Guide*.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT_ACTION_ORDER | STRICT_ORDER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamExceptionPolicy`  <a name="cfn-networkfirewall-firewallpolicy-statefulengineoptions-streamexceptionpolicy"></a>
Configures how Network Firewall processes traffic when a network connection breaks midstream. Network connections can break due to disruptions in external networks or within the firewall itself.
+ `DROP` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. This is the default behavior.
+ `CONTINUE` - Network Firewall continues to apply rules to the subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on this context. For example, if you have a stateful rule to `drop http` traffic, Network Firewall won't match the traffic for this rule because the service won't have the context from session initialization defining the application layer protocol as HTTP. However, this behavior is rule dependent—a TCP-layer rule using a `flow:stateless` rule would still match, as would the `aws:drop_strict` default action.
+ `REJECT` - Network Firewall fails closed and drops all subsequent traffic going to the firewall. Network Firewall also sends a TCP reject packet back to your client so that the client can immediately establish a new session. Network Firewall will have context about the new session and will apply rules to the subsequent traffic.
*Required*: No
*Type*: String
*Allowed values*: `DROP | CONTINUE | REJECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
