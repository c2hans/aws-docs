---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-authorizationdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget AuthorizationData
<a name="aws-properties-bedrockagentcore-gatewaytarget-authorizationdata"></a>

Contains the authorization data that is returned when a gateway target is configured with a credential provider with authorization code grant type and requires user federation.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-authorizationdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-authorizationdata-syntax.json"></a>

```
{
  "[Oauth2](#cfn-bedrockagentcore-gatewaytarget-authorizationdata-oauth2)" : {{OAuth2AuthorizationData}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-authorizationdata-syntax.yaml"></a>

```
  [Oauth2](#cfn-bedrockagentcore-gatewaytarget-authorizationdata-oauth2): {{
    OAuth2AuthorizationData}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-authorizationdata-properties"></a>

`Oauth2`  <a name="cfn-bedrockagentcore-gatewaytarget-authorizationdata-oauth2"></a>
OAuth2 authorization data for the gateway target.
*Required*: Yes
*Type*: [OAuth2AuthorizationData](aws-properties-bedrockagentcore-gatewaytarget-oauth2authorizationdata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
