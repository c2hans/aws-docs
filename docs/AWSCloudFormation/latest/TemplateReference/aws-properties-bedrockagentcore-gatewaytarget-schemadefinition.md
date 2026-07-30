---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget SchemaDefinition
<a name="aws-properties-bedrockagentcore-gatewaytarget-schemadefinition"></a>

A schema definition for a gateway target. This structure defines the structure of the API that the target exposes.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-schemadefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-schemadefinition-syntax.json"></a>

```
{
  "[Description](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-description)" : {{String}},
  "[Items](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-items)" : {{SchemaDefinition}},
  "[Properties](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-properties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Required](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-required)" : {{[ String, ... ]}},
  "[Type](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-schemadefinition-syntax.yaml"></a>

```
  [Description](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-description): {{String}}
  [Items](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-items): {{
    SchemaDefinition}}
  [Properties](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-properties): {{
    {{Key}}: {{Value}}}}
  [Required](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-required): {{
    - String}}
  [Type](#cfn-bedrockagentcore-gatewaytarget-schemadefinition-type): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-schemadefinition-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-gatewaytarget-schemadefinition-description"></a>
The description of the schema definition. This description provides information about the purpose and usage of the schema.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Items`  <a name="cfn-bedrockagentcore-gatewaytarget-schemadefinition-items"></a>
The items in the schema definition. This field is used for array types to define the structure of the array elements.
*Required*: No
*Type*: [SchemaDefinition](#aws-properties-bedrockagentcore-gatewaytarget-schemadefinition)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-bedrockagentcore-gatewaytarget-schemadefinition-properties"></a>
The properties of the schema definition. These properties define the fields in the schema.
*Required*: No
*Type*: Object of [SchemaDefinition](#aws-properties-bedrockagentcore-gatewaytarget-schemadefinition)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Required`  <a name="cfn-bedrockagentcore-gatewaytarget-schemadefinition-required"></a>
The required fields in the schema definition. These fields must be provided when using the schema.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrockagentcore-gatewaytarget-schemadefinition-type"></a>
The type of the schema definition. This field specifies the data type of the schema.
*Required*: Yes
*Type*: String
*Allowed values*: `string | number | object | array | boolean | integer`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
