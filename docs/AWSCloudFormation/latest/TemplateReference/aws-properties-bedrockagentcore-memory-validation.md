---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-validation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory Validation
<a name="aws-properties-bedrockagentcore-memory-validation"></a>

Validation rules for extracted metadata values. Only one type can be specified, matching the field's data type.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-validation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-validation-syntax.json"></a>

```
{
  "[NumberValidation](#cfn-bedrockagentcore-memory-validation-numbervalidation)" : {{NumberValidation}},
  "[StringListValidation](#cfn-bedrockagentcore-memory-validation-stringlistvalidation)" : {{StringListValidation}},
  "[StringValidation](#cfn-bedrockagentcore-memory-validation-stringvalidation)" : {{StringValidation}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-validation-syntax.yaml"></a>

```
  [NumberValidation](#cfn-bedrockagentcore-memory-validation-numbervalidation): {{
    NumberValidation}}
  [StringListValidation](#cfn-bedrockagentcore-memory-validation-stringlistvalidation): {{
    StringListValidation}}
  [StringValidation](#cfn-bedrockagentcore-memory-validation-stringvalidation): {{
    StringValidation}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-validation-properties"></a>

`NumberValidation`  <a name="cfn-bedrockagentcore-memory-validation-numbervalidation"></a>
Property description not available.
*Required*: No
*Type*: [NumberValidation](aws-properties-bedrockagentcore-memory-numbervalidation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringListValidation`  <a name="cfn-bedrockagentcore-memory-validation-stringlistvalidation"></a>
Property description not available.
*Required*: No
*Type*: [StringListValidation](aws-properties-bedrockagentcore-memory-stringlistvalidation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValidation`  <a name="cfn-bedrockagentcore-memory-validation-stringvalidation"></a>
Property description not available.
*Required*: No
*Type*: [StringValidation](aws-properties-bedrockagentcore-memory-stringvalidation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
