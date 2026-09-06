---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-contextualgroundingfilterconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail ContextualGroundingFilterConfig
<a name="aws-properties-bedrock-guardrail-contextualgroundingfilterconfig"></a>

The filter configuration details for the guardrails contextual grounding filter.

## Syntax
<a name="aws-properties-bedrock-guardrail-contextualgroundingfilterconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-contextualgroundingfilterconfig-syntax.json"></a>

```
{
  "[Action](#cfn-bedrock-guardrail-contextualgroundingfilterconfig-action)" : {{String}},
  "[Enabled](#cfn-bedrock-guardrail-contextualgroundingfilterconfig-enabled)" : {{Boolean}},
  "[Threshold](#cfn-bedrock-guardrail-contextualgroundingfilterconfig-threshold)" : {{Number}},
  "[Type](#cfn-bedrock-guardrail-contextualgroundingfilterconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-contextualgroundingfilterconfig-syntax.yaml"></a>

```
  [Action](#cfn-bedrock-guardrail-contextualgroundingfilterconfig-action): {{String}}
  [Enabled](#cfn-bedrock-guardrail-contextualgroundingfilterconfig-enabled): {{Boolean}}
  [Threshold](#cfn-bedrock-guardrail-contextualgroundingfilterconfig-threshold): {{Number}}
  [Type](#cfn-bedrock-guardrail-contextualgroundingfilterconfig-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-contextualgroundingfilterconfig-properties"></a>

`Action`  <a name="cfn-bedrock-guardrail-contextualgroundingfilterconfig-action"></a>
Specifies the action to take when content fails the contextual grounding evaluation. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-bedrock-guardrail-contextualgroundingfilterconfig-enabled"></a>
Specifies whether to enable contextual grounding evaluation. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Threshold`  <a name="cfn-bedrock-guardrail-contextualgroundingfilterconfig-threshold"></a>
The threshold details for the guardrails contextual grounding filter.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-guardrail-contextualgroundingfilterconfig-type"></a>
The filter details for the guardrails contextual grounding filter.
*Required*: Yes
*Type*: String
*Allowed values*: `GROUNDING | RELEVANCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
