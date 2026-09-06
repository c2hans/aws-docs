---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIGuardrail AIGuardrailContentPolicyConfig
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig"></a>

Content policy config for a guardrail.

## Syntax
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig-syntax.json"></a>

```
{
  "[FiltersConfig](#cfn-wisdom-aiguardrail-aiguardrailcontentpolicyconfig-filtersconfig)" : {{[ GuardrailContentFilterConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig-syntax.yaml"></a>

```
  [FiltersConfig](#cfn-wisdom-aiguardrail-aiguardrailcontentpolicyconfig-filtersconfig): {{
    - GuardrailContentFilterConfig}}
```

## Properties
<a name="aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig-properties"></a>

`FiltersConfig`  <a name="cfn-wisdom-aiguardrail-aiguardrailcontentpolicyconfig-filtersconfig"></a>
List of content filter configurations in a content policy.
*Required*: Yes
*Type*: Array of [GuardrailContentFilterConfig](aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig.md)
*Minimum*: `1`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
