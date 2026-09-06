---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-stringvalidation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory StringValidation
<a name="aws-properties-bedrockagentcore-memory-stringvalidation"></a>

Validation for STRING fields.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-stringvalidation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-stringvalidation-syntax.json"></a>

```
{
  "[AllowedValues](#cfn-bedrockagentcore-memory-stringvalidation-allowedvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-stringvalidation-syntax.yaml"></a>

```
  [AllowedValues](#cfn-bedrockagentcore-memory-stringvalidation-allowedvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-stringvalidation-properties"></a>

`AllowedValues`  <a name="cfn-bedrockagentcore-memory-stringvalidation-allowedvalues"></a>
Allowed values for this STRING field.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
