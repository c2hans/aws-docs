---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-contextualgroundingpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail ContextualGroundingPolicyConfig
<a name="aws-properties-bedrock-guardrail-contextualgroundingpolicyconfig"></a>

The policy configuration details for the guardrails contextual grounding policy.

## Syntax
<a name="aws-properties-bedrock-guardrail-contextualgroundingpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-contextualgroundingpolicyconfig-syntax.json"></a>

```
{
  "[FiltersConfig](#cfn-bedrock-guardrail-contextualgroundingpolicyconfig-filtersconfig)" : {{[ ContextualGroundingFilterConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-contextualgroundingpolicyconfig-syntax.yaml"></a>

```
  [FiltersConfig](#cfn-bedrock-guardrail-contextualgroundingpolicyconfig-filtersconfig): {{
    - ContextualGroundingFilterConfig}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-contextualgroundingpolicyconfig-properties"></a>

`FiltersConfig`  <a name="cfn-bedrock-guardrail-contextualgroundingpolicyconfig-filtersconfig"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [ContextualGroundingFilterConfig](aws-properties-bedrock-guardrail-contextualgroundingfilterconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
