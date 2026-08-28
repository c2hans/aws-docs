---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail GuardrailContentFilterConfig
<a name="aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig"></a>

Content filter configuration in content policy.

## Syntax
<a name="aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig-syntax.json"></a>

```
{
  "[InputStrength](#cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-inputstrength)" : {{String}},
  "[OutputStrength](#cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-outputstrength)" : {{String}},
  "[Type](#cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig-syntax.yaml"></a>

```
  [InputStrength](#cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-inputstrength): {{String}}
  [OutputStrength](#cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-outputstrength): {{String}}
  [Type](#cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-type): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig-properties"></a>

`InputStrength`  <a name="cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-inputstrength"></a>
The strength of the input for the guardrail content filter.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputStrength`  <a name="cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-outputstrength"></a>
The output strength of the guardrail content filter.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-type"></a>
The type of the guardrail content filter.
*Required*: Yes
*Type*: String
*Allowed values*: `SEXUAL | VIOLENCE | HATE | INSULTS | MISCONDUCT | PROMPT_ATTACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
