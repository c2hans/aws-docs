---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-authorizerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway AuthorizerConfiguration
<a name="aws-properties-bedrockagentcore-gateway-authorizerconfiguration"></a>

Represents inbound authorization configuration options used to authenticate incoming requests.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-authorizerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-authorizerconfiguration-syntax.json"></a>

```
{
  "[CustomJWTAuthorizer](#cfn-bedrockagentcore-gateway-authorizerconfiguration-customjwtauthorizer)" : {{CustomJWTAuthorizerConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-authorizerconfiguration-syntax.yaml"></a>

```
  [CustomJWTAuthorizer](#cfn-bedrockagentcore-gateway-authorizerconfiguration-customjwtauthorizer): {{
    CustomJWTAuthorizerConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-authorizerconfiguration-properties"></a>

`CustomJWTAuthorizer`  <a name="cfn-bedrockagentcore-gateway-authorizerconfiguration-customjwtauthorizer"></a>
The inbound JWT-based authorization, specifying how incoming requests should be authenticated.
*Required*: Yes
*Type*: [CustomJWTAuthorizerConfiguration](aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
