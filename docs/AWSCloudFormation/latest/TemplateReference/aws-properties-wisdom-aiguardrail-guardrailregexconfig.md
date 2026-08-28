---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiguardrail-guardrailregexconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail GuardrailRegexConfig
<a name="aws-properties-wisdom-aiguardrail-guardrailregexconfig"></a>

A regex configuration.

## Syntax
<a name="aws-properties-wisdom-aiguardrail-guardrailregexconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiguardrail-guardrailregexconfig-syntax.json"></a>

```
{
  "[Action](#cfn-wisdom-aiguardrail-guardrailregexconfig-action)" : {{String}},
  "[Description](#cfn-wisdom-aiguardrail-guardrailregexconfig-description)" : {{String}},
  "[Name](#cfn-wisdom-aiguardrail-guardrailregexconfig-name)" : {{String}},
  "[Pattern](#cfn-wisdom-aiguardrail-guardrailregexconfig-pattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiguardrail-guardrailregexconfig-syntax.yaml"></a>

```
  [Action](#cfn-wisdom-aiguardrail-guardrailregexconfig-action): {{String}}
  [Description](#cfn-wisdom-aiguardrail-guardrailregexconfig-description): {{String}}
  [Name](#cfn-wisdom-aiguardrail-guardrailregexconfig-name): {{String}}
  [Pattern](#cfn-wisdom-aiguardrail-guardrailregexconfig-pattern): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiguardrail-guardrailregexconfig-properties"></a>

`Action`  <a name="cfn-wisdom-aiguardrail-guardrailregexconfig-action"></a>
The action of the guardrail regex configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `BLOCK | ANONYMIZE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-wisdom-aiguardrail-guardrailregexconfig-description"></a>
The regex description.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wisdom-aiguardrail-guardrailregexconfig-name"></a>
A regex configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pattern`  <a name="cfn-wisdom-aiguardrail-guardrailregexconfig-pattern"></a>
The regex pattern.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
