---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::FirewallPolicy StatefulRuleGroupOverride
<a name="aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride"></a>

The setting that allows the policy owner to change the behavior of the rule group within a policy.

## Syntax
<a name="aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride-syntax.json"></a>

```
{
  "[Action](#cfn-networkfirewall-firewallpolicy-statefulrulegroupoverride-action)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride-syntax.yaml"></a>

```
  [Action](#cfn-networkfirewall-firewallpolicy-statefulrulegroupoverride-action): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride-properties"></a>

`Action`  <a name="cfn-networkfirewall-firewallpolicy-statefulrulegroupoverride-action"></a>
The action that changes the rule group from `DROP` to `ALERT`. This only applies to managed rule groups.
*Required*: No
*Type*: String
*Allowed values*: `DROP_TO_ALERT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
