---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-guardrailcrossregionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail GuardrailCrossRegionConfig
<a name="aws-properties-bedrock-guardrail-guardrailcrossregionconfig"></a>

The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination AWS Regions where guardrail inference requests can be automatically routed. Using guardrail profiles helps maintain guardrail performance and reliability when demand increases.

For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html).

## Syntax
<a name="aws-properties-bedrock-guardrail-guardrailcrossregionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-guardrailcrossregionconfig-syntax.json"></a>

```
{
  "[GuardrailProfileArn](#cfn-bedrock-guardrail-guardrailcrossregionconfig-guardrailprofilearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-guardrailcrossregionconfig-syntax.yaml"></a>

```
  [GuardrailProfileArn](#cfn-bedrock-guardrail-guardrailcrossregionconfig-guardrailprofilearn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-guardrailcrossregionconfig-properties"></a>

`GuardrailProfileArn`  <a name="cfn-bedrock-guardrail-guardrailcrossregionconfig-guardrailprofilearn"></a>
The Amazon Resource Name (ARN) of the guardrail profile that your guardrail is using. Guardrail profile availability depends on your current AWS Region. For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region-support.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail-profile/[a-z0-9-]+[.]{1}guardrail[.]{1}v[0-9:]+$`
*Minimum*: `15`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
