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
