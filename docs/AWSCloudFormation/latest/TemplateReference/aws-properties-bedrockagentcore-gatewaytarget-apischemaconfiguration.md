---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ApiSchemaConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration"></a>

Configuration for API schema.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration-syntax.json"></a>

```
{
  "[InlinePayload](#cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-inlinepayload)" : {{String}},
  "[S3](#cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-s3)" : {{S3Configuration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration-syntax.yaml"></a>

```
  [InlinePayload](#cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-inlinepayload): {{String}}
  [S3](#cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-s3): {{
    S3Configuration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration-properties"></a>

`InlinePayload`  <a name="cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-inlinepayload"></a>
The inline payload containing the API schema definition.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-s3"></a>
The S3 configuration for a gateway. This structure defines how the gateway accesses files in S3.
*Required*: No
*Type*: [S3Configuration](aws-properties-bedrockagentcore-gatewaytarget-s3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
