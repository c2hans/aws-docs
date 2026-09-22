---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-namespacekeyvalidation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory NamespaceKeyValidation
<a name="aws-properties-bedrockagentcore-memory-namespacekeyvalidation"></a>

The validation rules for namespace variable values. When you specify multiple rules, the service enforces a logical `AND` across all provided key-value pairs.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-namespacekeyvalidation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-namespacekeyvalidation-syntax.json"></a>

```
{
  "[AllowedValues](#cfn-bedrockagentcore-memory-namespacekeyvalidation-allowedvalues)" : {{[ String, ... ]}},
  "[RegexPattern](#cfn-bedrockagentcore-memory-namespacekeyvalidation-regexpattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-namespacekeyvalidation-syntax.yaml"></a>

```
  [AllowedValues](#cfn-bedrockagentcore-memory-namespacekeyvalidation-allowedvalues): {{
    - String}}
  [RegexPattern](#cfn-bedrockagentcore-memory-namespacekeyvalidation-regexpattern): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-namespacekeyvalidation-properties"></a>

`AllowedValues`  <a name="cfn-bedrockagentcore-memory-namespacekeyvalidation-allowedvalues"></a>
The allowed values for this namespace variable key.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegexPattern`  <a name="cfn-bedrockagentcore-memory-namespacekeyvalidation-regexpattern"></a>
A regex pattern that the namespace variable key-value must match.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
