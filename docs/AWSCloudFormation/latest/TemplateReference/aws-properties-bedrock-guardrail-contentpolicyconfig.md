---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-contentpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail ContentPolicyConfig
<a name="aws-properties-bedrock-guardrail-contentpolicyconfig"></a>

Contains details about how to handle harmful content.

## Syntax
<a name="aws-properties-bedrock-guardrail-contentpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-contentpolicyconfig-syntax.json"></a>

```
{
  "[ContentFiltersTierConfig](#cfn-bedrock-guardrail-contentpolicyconfig-contentfilterstierconfig)" : {{ContentFiltersTierConfig}},
  "[FiltersConfig](#cfn-bedrock-guardrail-contentpolicyconfig-filtersconfig)" : {{[ ContentFilterConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-contentpolicyconfig-syntax.yaml"></a>

```
  [ContentFiltersTierConfig](#cfn-bedrock-guardrail-contentpolicyconfig-contentfilterstierconfig): {{
    ContentFiltersTierConfig}}
  [FiltersConfig](#cfn-bedrock-guardrail-contentpolicyconfig-filtersconfig): {{
    - ContentFilterConfig}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-contentpolicyconfig-properties"></a>

`ContentFiltersTierConfig`  <a name="cfn-bedrock-guardrail-contentpolicyconfig-contentfilterstierconfig"></a>
The tier that your guardrail uses for content filters. Consider using a tier that balances performance, accuracy, and compatibility with your existing generative AI workflows.
*Required*: No
*Type*: [ContentFiltersTierConfig](aws-properties-bedrock-guardrail-contentfilterstierconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FiltersConfig`  <a name="cfn-bedrock-guardrail-contentpolicyconfig-filtersconfig"></a>
Contains the type of the content filter and how strongly it should apply to prompts and model responses.
*Required*: Yes
*Type*: Array of [ContentFilterConfig](aws-properties-bedrock-guardrail-contentfilterconfig.md)
*Minimum*: `1`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
