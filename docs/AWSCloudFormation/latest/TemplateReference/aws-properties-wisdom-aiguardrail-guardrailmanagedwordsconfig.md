---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail GuardrailManagedWordsConfig
<a name="aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig"></a>

A managed words config.

## Syntax
<a name="aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig-syntax.json"></a>

```
{
  "[Type](#cfn-wisdom-aiguardrail-guardrailmanagedwordsconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig-syntax.yaml"></a>

```
  [Type](#cfn-wisdom-aiguardrail-guardrailmanagedwordsconfig-type): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig-properties"></a>

`Type`  <a name="cfn-wisdom-aiguardrail-guardrailmanagedwordsconfig-type"></a>
The type of guardrail managed words.
*Required*: Yes
*Type*: String
*Allowed values*: `PROFANITY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
