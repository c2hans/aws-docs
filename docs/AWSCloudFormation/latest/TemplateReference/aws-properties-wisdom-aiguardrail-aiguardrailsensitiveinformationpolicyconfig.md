---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail AIGuardrailSensitiveInformationPolicyConfig
<a name="aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig"></a>

Sensitive information policy configuration for a guardrail.

## Syntax
<a name="aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-syntax.json"></a>

```
{
  "[PiiEntitiesConfig](#cfn-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-piientitiesconfig)" : {{[ GuardrailPiiEntityConfig, ... ]}},
  "[RegexesConfig](#cfn-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-regexesconfig)" : {{[ GuardrailRegexConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-syntax.yaml"></a>

```
  [PiiEntitiesConfig](#cfn-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-piientitiesconfig): {{
    - GuardrailPiiEntityConfig}}
  [RegexesConfig](#cfn-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-regexesconfig): {{
    - GuardrailRegexConfig}}
```

## Properties
<a name="aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-properties"></a>

`PiiEntitiesConfig`  <a name="cfn-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-piientitiesconfig"></a>
List of entities.
*Required*: No
*Type*: Array of [GuardrailPiiEntityConfig](aws-properties-wisdom-aiguardrail-guardrailpiientityconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegexesConfig`  <a name="cfn-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-regexesconfig"></a>
List of regex.
*Required*: No
*Type*: Array of [GuardrailRegexConfig](aws-properties-wisdom-aiguardrail-guardrailregexconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
