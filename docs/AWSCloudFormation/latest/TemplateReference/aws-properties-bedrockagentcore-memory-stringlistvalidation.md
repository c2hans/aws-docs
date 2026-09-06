---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-stringlistvalidation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory StringListValidation
<a name="aws-properties-bedrockagentcore-memory-stringlistvalidation"></a>

Validation for STRINGLIST fields.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-stringlistvalidation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-stringlistvalidation-syntax.json"></a>

```
{
  "[AllowedValues](#cfn-bedrockagentcore-memory-stringlistvalidation-allowedvalues)" : {{[ String, ... ]}},
  "[MaxItems](#cfn-bedrockagentcore-memory-stringlistvalidation-maxitems)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-stringlistvalidation-syntax.yaml"></a>

```
  [AllowedValues](#cfn-bedrockagentcore-memory-stringlistvalidation-allowedvalues): {{
    - String}}
  [MaxItems](#cfn-bedrockagentcore-memory-stringlistvalidation-maxitems): {{Integer}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-stringlistvalidation-properties"></a>

`AllowedValues`  <a name="cfn-bedrockagentcore-memory-stringlistvalidation-allowedvalues"></a>
Allowed values for items in this STRINGLIST field.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxItems`  <a name="cfn-bedrockagentcore-memory-stringlistvalidation-maxitems"></a>
Maximum number of items in the string list.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
