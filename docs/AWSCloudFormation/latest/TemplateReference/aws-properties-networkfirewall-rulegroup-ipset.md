---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-ipset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup IPSet
<a name="aws-properties-networkfirewall-rulegroup-ipset"></a>

A list of IP addresses and address ranges, in CIDR notation. This is part of a `RuleVariables`.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-ipset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-ipset-syntax.json"></a>

```
{
  "[Definition](#cfn-networkfirewall-rulegroup-ipset-definition)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-ipset-syntax.yaml"></a>

```
  [Definition](#cfn-networkfirewall-rulegroup-ipset-definition): {{
    - String}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-ipset-properties"></a>

`Definition`  <a name="cfn-networkfirewall-rulegroup-ipset-definition"></a>
The list of IP addresses and address ranges, in CIDR notation.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
