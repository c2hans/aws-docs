---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-referencesets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup ReferenceSets
<a name="aws-properties-networkfirewall-rulegroup-referencesets"></a>

Configures the reference sets for a stateful rule group. For more information, see the [Using IP set references in Suricata compatible rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-ip-set-references.html) in the *Network Firewall User Guide*.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-referencesets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-referencesets-syntax.json"></a>

```
{
  "[IPSetReferences](#cfn-networkfirewall-rulegroup-referencesets-ipsetreferences)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-referencesets-syntax.yaml"></a>

```
  [IPSetReferences](#cfn-networkfirewall-rulegroup-referencesets-ipsetreferences): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-referencesets-properties"></a>

`IPSetReferences`  <a name="cfn-networkfirewall-rulegroup-referencesets-ipsetreferences"></a>
The IP set references to use in the stateful rule group.
*Required*: No
*Type*: Object of [IPSetReference](aws-properties-networkfirewall-rulegroup-ipsetreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
