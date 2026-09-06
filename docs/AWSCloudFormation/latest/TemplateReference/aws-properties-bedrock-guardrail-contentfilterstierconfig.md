---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-contentfilterstierconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail ContentFiltersTierConfig
<a name="aws-properties-bedrock-guardrail-contentfilterstierconfig"></a>

The tier that your guardrail uses for content filters. Consider using a tier that balances performance, accuracy, and compatibility with your existing generative AI workflows.

## Syntax
<a name="aws-properties-bedrock-guardrail-contentfilterstierconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-contentfilterstierconfig-syntax.json"></a>

```
{
  "[TierName](#cfn-bedrock-guardrail-contentfilterstierconfig-tiername)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-contentfilterstierconfig-syntax.yaml"></a>

```
  [TierName](#cfn-bedrock-guardrail-contentfilterstierconfig-tiername): {{String}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-contentfilterstierconfig-properties"></a>

`TierName`  <a name="cfn-bedrock-guardrail-contentfilterstierconfig-tiername"></a>
The tier that your guardrail uses for content filters. Valid values include:
+ `CLASSIC` tier – Provides established guardrails functionality supporting English, French, and Spanish languages.
+ `STANDARD` tier – Provides a more robust solution than the `CLASSIC` tier and has more comprehensive language support. This tier requires that your guardrail use [cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html).
*Required*: Yes
*Type*: String
*Allowed values*: `CLASSIC | STANDARD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
