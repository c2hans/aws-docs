---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail AIGuardrailContextualGroundingPolicyConfig
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig"></a>

Contextual grounding policy config for a guardrail.

## Syntax
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig-syntax.json"></a>

```
{
  "[FiltersConfig](#cfn-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig-filtersconfig)" : {{[ GuardrailContextualGroundingFilterConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig-syntax.yaml"></a>

```
  [FiltersConfig](#cfn-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig-filtersconfig): {{
    - GuardrailContextualGroundingFilterConfig}}
```

## Properties
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig-properties"></a>

`FiltersConfig`  <a name="cfn-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig-filtersconfig"></a>
List of contextual grounding filter configs.
*Required*: Yes
*Type*: Array of [GuardrailContextualGroundingFilterConfig](aws-properties-wisdom-aiguardrail-guardrailcontextualgroundingfilterconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
