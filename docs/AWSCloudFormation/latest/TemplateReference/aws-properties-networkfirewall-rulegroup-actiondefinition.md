---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-actiondefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup ActionDefinition
<a name="aws-properties-networkfirewall-rulegroup-actiondefinition"></a>

A custom action to use in stateless rule actions settings.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-actiondefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-actiondefinition-syntax.json"></a>

```
{
  "[PublishMetricAction](#cfn-networkfirewall-rulegroup-actiondefinition-publishmetricaction)" : {{PublishMetricAction}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-actiondefinition-syntax.yaml"></a>

```
  [PublishMetricAction](#cfn-networkfirewall-rulegroup-actiondefinition-publishmetricaction): {{
    PublishMetricAction}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-actiondefinition-properties"></a>

`PublishMetricAction`  <a name="cfn-networkfirewall-rulegroup-actiondefinition-publishmetricaction"></a>
Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet. This setting defines a CloudWatch dimension value to be published.
You can pair this custom action with any of the standard stateless rule actions. For example, you could pair this in a rule action with the standard action that forwards the packet for stateful inspection. Then, when a packet matches the rule, Network Firewall publishes metrics for the packet and forwards it.
*Required*: No
*Type*: [PublishMetricAction](aws-properties-networkfirewall-rulegroup-publishmetricaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
