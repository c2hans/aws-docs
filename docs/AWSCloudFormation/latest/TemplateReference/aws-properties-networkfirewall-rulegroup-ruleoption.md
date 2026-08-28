---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-rulegroup-ruleoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::RuleGroup RuleOption
<a name="aws-properties-networkfirewall-rulegroup-ruleoption"></a>

Additional settings for a stateful rule.

## Syntax
<a name="aws-properties-networkfirewall-rulegroup-ruleoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-rulegroup-ruleoption-syntax.json"></a>

```
{
  "[Keyword](#cfn-networkfirewall-rulegroup-ruleoption-keyword)" : {{String}},
  "[Settings](#cfn-networkfirewall-rulegroup-ruleoption-settings)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-networkfirewall-rulegroup-ruleoption-syntax.yaml"></a>

```
  [Keyword](#cfn-networkfirewall-rulegroup-ruleoption-keyword): {{String}}
  [Settings](#cfn-networkfirewall-rulegroup-ruleoption-settings): {{
    - String}}
```

## Properties
<a name="aws-properties-networkfirewall-rulegroup-ruleoption-properties"></a>

`Keyword`  <a name="cfn-networkfirewall-rulegroup-ruleoption-keyword"></a>
The Suricata rule option keywords. For Network Firewall, the keyword signature ID (sid) is required in the format `sid:112233`. The sid must be unique within the rule group. For information about Suricata rule option keywords, see [Rule options](https://suricata.readthedocs.io/en/suricata-7.0.8/rules/intro.html#rule-options).
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Settings`  <a name="cfn-networkfirewall-rulegroup-ruleoption-settings"></a>
The Suricata rule option settings. Settings have zero or more values, and the number of possible settings and required settings depends on the keyword. The format for Settings is `number`. For information about Suricata rule option settings, see [Rule options](https://suricata.readthedocs.io/en/suricata-7.0.8/rules/intro.html#rule-options).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
