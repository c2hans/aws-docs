---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-ipsetreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup IPSetReference
<a name="aws-properties-networkfirewall-rulegroup-ipsetreference"></a>

Configures one or more IP set references for a Suricata-compatible rule group. An IP set reference is a rule variable that references a resource that you create and manage in another AWS service, such as an Amazon VPC prefix list. Network Firewall IP set references enable you to dynamically update the contents of your rules. When you create, update, or delete the IP set you are referencing in your rule, Network Firewall automatically updates the rule's content with the changes. For more information about IP set references in Network Firewall, see [Using IP set references](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-ip-set-references.html) in the *Network Firewall Developer Guide*.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-ipsetreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-ipsetreference-syntax.json"></a>

```
{
  "[ReferenceArn](#cfn-networkfirewall-rulegroup-ipsetreference-referencearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-ipsetreference-syntax.yaml"></a>

```
  [ReferenceArn](#cfn-networkfirewall-rulegroup-ipsetreference-referencearn): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-ipsetreference-properties"></a>

`ReferenceArn`  <a name="cfn-networkfirewall-rulegroup-ipsetreference-referencearn"></a>
The Amazon Resource Name (ARN) of the resource to include in the IP set reference.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws.*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
