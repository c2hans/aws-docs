---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-protectconfiguration-countryruleset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::ProtectConfiguration CountryRuleSet
<a name="aws-properties-smsvoice-protectconfiguration-countryruleset"></a>

The set of `CountryRules` you specify to control which countries AWS End User Messaging SMS can send your messages to.

**Note**
If you don't specify all available ISO country codes in the `CountryRuleSet` for each number capability, the CloudFormation drift detection feature will detect drift. This is because AWS End User Messaging SMS always returns all country codes.

## Syntax
<a name="aws-properties-smsvoice-protectconfiguration-countryruleset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-protectconfiguration-countryruleset-syntax.json"></a>

```
{
  "[MMS](#cfn-smsvoice-protectconfiguration-countryruleset-mms)" : {{[ CountryRule, ... ]}},
  "[SMS](#cfn-smsvoice-protectconfiguration-countryruleset-sms)" : {{[ CountryRule, ... ]}},
  "[VOICE](#cfn-smsvoice-protectconfiguration-countryruleset-voice)" : {{[ CountryRule, ... ]}}
}
```

### YAML
<a name="aws-properties-smsvoice-protectconfiguration-countryruleset-syntax.yaml"></a>

```
  [MMS](#cfn-smsvoice-protectconfiguration-countryruleset-mms): {{
    - CountryRule}}
  [SMS](#cfn-smsvoice-protectconfiguration-countryruleset-sms): {{
    - CountryRule}}
  [VOICE](#cfn-smsvoice-protectconfiguration-countryruleset-voice): {{
    - CountryRule}}
```

## Properties
<a name="aws-properties-smsvoice-protectconfiguration-countryruleset-properties"></a>

`MMS`  <a name="cfn-smsvoice-protectconfiguration-countryruleset-mms"></a>
The set of `CountryRule`s to control which destination countries AWS End User Messaging SMS can send your MMS messages to.
*Required*: No
*Type*: Array of [CountryRule](aws-properties-smsvoice-protectconfiguration-countryrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SMS`  <a name="cfn-smsvoice-protectconfiguration-countryruleset-sms"></a>
The set of `CountryRule`s to control which destination countries AWS End User Messaging SMS can send your SMS messages to.
*Required*: No
*Type*: Array of [CountryRule](aws-properties-smsvoice-protectconfiguration-countryrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VOICE`  <a name="cfn-smsvoice-protectconfiguration-countryruleset-voice"></a>
The set of `CountryRule`s to control which destination countries AWS End User Messaging SMS can send your VOICE messages to.
*Required*: No
*Type*: Array of [CountryRule](aws-properties-smsvoice-protectconfiguration-countryrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
