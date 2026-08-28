---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-sensitiveinformationpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail SensitiveInformationPolicyConfig
<a name="aws-properties-bedrock-guardrail-sensitiveinformationpolicyconfig"></a>

Contains details about PII entities and regular expressions to configure for the guardrail.

## Syntax
<a name="aws-properties-bedrock-guardrail-sensitiveinformationpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-sensitiveinformationpolicyconfig-syntax.json"></a>

```
{
  "[PiiEntitiesConfig](#cfn-bedrock-guardrail-sensitiveinformationpolicyconfig-piientitiesconfig)" : {{[ PiiEntityConfig, ... ]}},
  "[RegexesConfig](#cfn-bedrock-guardrail-sensitiveinformationpolicyconfig-regexesconfig)" : {{[ RegexConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-sensitiveinformationpolicyconfig-syntax.yaml"></a>

```
  [PiiEntitiesConfig](#cfn-bedrock-guardrail-sensitiveinformationpolicyconfig-piientitiesconfig): {{
    - PiiEntityConfig}}
  [RegexesConfig](#cfn-bedrock-guardrail-sensitiveinformationpolicyconfig-regexesconfig): {{
    - RegexConfig}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-sensitiveinformationpolicyconfig-properties"></a>

`PiiEntitiesConfig`  <a name="cfn-bedrock-guardrail-sensitiveinformationpolicyconfig-piientitiesconfig"></a>
A list of PII entities to configure to the guardrail.
*Required*: No
*Type*: Array of [PiiEntityConfig](aws-properties-bedrock-guardrail-piientityconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegexesConfig`  <a name="cfn-bedrock-guardrail-sensitiveinformationpolicyconfig-regexesconfig"></a>
A list of regular expressions to configure to the guardrail.
*Required*: No
*Type*: Array of [RegexConfig](aws-properties-bedrock-guardrail-regexconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
