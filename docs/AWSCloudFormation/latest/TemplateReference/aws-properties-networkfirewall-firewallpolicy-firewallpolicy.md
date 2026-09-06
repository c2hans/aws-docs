---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::FirewallPolicy FirewallPolicy
<a name="aws-properties-networkfirewall-firewallpolicy-firewallpolicy"></a>

The traffic filtering behavior of a firewall policy, defined in a collection of stateless and stateful rule groups and other settings.

## Syntax
<a name="aws-properties-networkfirewall-firewallpolicy-firewallpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewallpolicy-firewallpolicy-syntax.json"></a>

```
{
  "[EnableTLSSessionHolding](#cfn-networkfirewall-firewallpolicy-firewallpolicy-enabletlssessionholding)" : {{Boolean}},
  "[PolicyVariables](#cfn-networkfirewall-firewallpolicy-firewallpolicy-policyvariables)" : {{PolicyVariables}},
  "[StatefulDefaultActions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefuldefaultactions)" : {{[ String, ... ]}},
  "[StatefulEngineOptions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulengineoptions)" : {{StatefulEngineOptions}},
  "[StatefulRuleGroupReferences](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulrulegroupreferences)" : {{[ StatefulRuleGroupReference, ... ]}},
  "[StatelessCustomActions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelesscustomactions)" : {{[ CustomAction, ... ]}},
  "[StatelessDefaultActions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessdefaultactions)" : {{[ String, ... ]}},
  "[StatelessFragmentDefaultActions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessfragmentdefaultactions)" : {{[ String, ... ]}},
  "[StatelessRuleGroupReferences](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessrulegroupreferences)" : {{[ StatelessRuleGroupReference, ... ]}},
  "[TLSInspectionConfigurationArn](#cfn-networkfirewall-firewallpolicy-firewallpolicy-tlsinspectionconfigurationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewallpolicy-firewallpolicy-syntax.yaml"></a>

```
  [EnableTLSSessionHolding](#cfn-networkfirewall-firewallpolicy-firewallpolicy-enabletlssessionholding): {{Boolean}}
  [PolicyVariables](#cfn-networkfirewall-firewallpolicy-firewallpolicy-policyvariables): {{
    PolicyVariables}}
  [StatefulDefaultActions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefuldefaultactions): {{
    - String}}
  [StatefulEngineOptions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulengineoptions): {{
    StatefulEngineOptions}}
  [StatefulRuleGroupReferences](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulrulegroupreferences): {{
    - StatefulRuleGroupReference}}
  [StatelessCustomActions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelesscustomactions): {{
    - CustomAction}}
  [StatelessDefaultActions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessdefaultactions): {{
    - String}}
  [StatelessFragmentDefaultActions](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessfragmentdefaultactions): {{
    - String}}
  [StatelessRuleGroupReferences](#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessrulegroupreferences): {{
    - StatelessRuleGroupReference}}
  [TLSInspectionConfigurationArn](#cfn-networkfirewall-firewallpolicy-firewallpolicy-tlsinspectionconfigurationarn): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-firewallpolicy-firewallpolicy-properties"></a>

`EnableTLSSessionHolding`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-enabletlssessionholding"></a>
When true, prevents TCP and TLS packets from reaching destination servers until TLS Inspection has evaluated Server Name Indication (SNI) rules. Requires an associated TLS Inspection configuration.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyVariables`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-policyvariables"></a>
Contains variables that you can use to override default Suricata settings in your firewall policy.
*Required*: No
*Type*: [PolicyVariables](aws-properties-networkfirewall-firewallpolicy-policyvariables.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatefulDefaultActions`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-statefuldefaultactions"></a>
The default actions to take on a packet that doesn't match any stateful rules. The stateful default action is optional, and is only valid when using the strict rule order.
Valid values of the stateful default action:
+ aws:drop\_strict
+ aws:drop\_established
+ aws:alert\_strict
+ aws:alert\_established
+ aws:drop\_established\_app\_layer
+ aws:alert\_established\_app\_layer
+ aws:drop\_established\_app\_layer\_to\_server
+ aws:alert\_established\_app\_layer\_to\_server
For more information, see [Strict evaluation order](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html#suricata-strict-rule-evaluation-order.html) in the *AWS Network Firewall Developer Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatefulEngineOptions`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulengineoptions"></a>
Additional options governing how Network Firewall handles stateful rules. The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.
*Required*: No
*Type*: [StatefulEngineOptions](aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatefulRuleGroupReferences`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulrulegroupreferences"></a>
References to the stateful rule groups that are used in the policy. These define the inspection criteria in stateful rules.
*Required*: No
*Type*: Array of [StatefulRuleGroupReference](aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatelessCustomActions`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-statelesscustomactions"></a>
The custom action definitions that are available for use in the firewall policy's `StatelessDefaultActions` setting. You name each custom action that you define, and then you can use it by name in your default actions specifications.
*Required*: No
*Type*: Array of [CustomAction](aws-properties-networkfirewall-firewallpolicy-customaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatelessDefaultActions`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessdefaultactions"></a>
The actions to take on a packet if it doesn't match any of the stateless rules in the policy. If you want non-matching packets to be forwarded for stateful inspection, specify `aws:forward_to_sfe`.
You must specify one of the standard actions: `aws:pass`, `aws:drop`, or `aws:forward_to_sfe`. In addition, you can specify custom actions that are compatible with your standard section choice.
For example, you could specify `["aws:pass"]` or you could specify `["aws:pass", “customActionName”]`. For information about compatibility, see the custom action descriptions.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatelessFragmentDefaultActions`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessfragmentdefaultactions"></a>
The actions to take on a fragmented UDP packet if it doesn't match any of the stateless rules in the policy. Network Firewall only manages UDP packet fragments and silently drops packet fragments for other protocols. If you want non-matching fragmented UDP packets to be forwarded for stateful inspection, specify `aws:forward_to_sfe`.
You must specify one of the standard actions: `aws:pass`, `aws:drop`, or `aws:forward_to_sfe`. In addition, you can specify custom actions that are compatible with your standard section choice.
For example, you could specify `["aws:pass"]` or you could specify `["aws:pass", “customActionName”]`. For information about compatibility, see the custom action descriptions.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatelessRuleGroupReferences`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessrulegroupreferences"></a>
References to the stateless rule groups that are used in the policy. These define the matching criteria in stateless rules.
*Required*: No
*Type*: Array of [StatelessRuleGroupReference](aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TLSInspectionConfigurationArn`  <a name="cfn-networkfirewall-firewallpolicy-firewallpolicy-tlsinspectionconfigurationarn"></a>
The Amazon Resource Name (ARN) of the TLS inspection configuration.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws.*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
