---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::FirewallPolicy PublishMetricAction
<a name="aws-properties-networkfirewall-firewallpolicy-publishmetricaction"></a>

Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet. This setting defines a CloudWatch dimension value to be published.

## Syntax
<a name="aws-properties-networkfirewall-firewallpolicy-publishmetricaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewallpolicy-publishmetricaction-syntax.json"></a>

```
{
  "[Dimensions](#cfn-networkfirewall-firewallpolicy-publishmetricaction-dimensions)" : {{[ Dimension, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewallpolicy-publishmetricaction-syntax.yaml"></a>

```
  [Dimensions](#cfn-networkfirewall-firewallpolicy-publishmetricaction-dimensions): {{
    - Dimension}}
```

## Properties
<a name="aws-properties-networkfirewall-firewallpolicy-publishmetricaction-properties"></a>

`Dimensions`  <a name="cfn-networkfirewall-firewallpolicy-publishmetricaction-dimensions"></a>

*Required*: Yes
*Type*: Array of [Dimension](aws-properties-networkfirewall-firewallpolicy-dimension.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
