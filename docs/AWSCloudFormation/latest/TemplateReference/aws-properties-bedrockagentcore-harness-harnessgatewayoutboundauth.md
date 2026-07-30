---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessgatewayoutboundauth.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessGatewayOutboundAuth
<a name="aws-properties-bedrockagentcore-harness-harnessgatewayoutboundauth"></a>

Authentication method for calling a Gateway.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessgatewayoutboundauth-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessgatewayoutboundauth-syntax.json"></a>

```
{
  "[AwsIam](#cfn-bedrockagentcore-harness-harnessgatewayoutboundauth-awsiam)" : {{Json}},
  "[None](#cfn-bedrockagentcore-harness-harnessgatewayoutboundauth-none)" : {{Json}},
  "[Oauth](#cfn-bedrockagentcore-harness-harnessgatewayoutboundauth-oauth)" : {{OAuthCredentialProvider}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessgatewayoutboundauth-syntax.yaml"></a>

```
  [AwsIam](#cfn-bedrockagentcore-harness-harnessgatewayoutboundauth-awsiam): {{Json}}
  [None](#cfn-bedrockagentcore-harness-harnessgatewayoutboundauth-none): {{Json}}
  [Oauth](#cfn-bedrockagentcore-harness-harnessgatewayoutboundauth-oauth): {{
    OAuthCredentialProvider}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessgatewayoutboundauth-properties"></a>

`AwsIam`  <a name="cfn-bedrockagentcore-harness-harnessgatewayoutboundauth-awsiam"></a>
SigV4-sign requests using the agent's execution role.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`None`  <a name="cfn-bedrockagentcore-harness-harnessgatewayoutboundauth-none"></a>
No authentication.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Oauth`  <a name="cfn-bedrockagentcore-harness-harnessgatewayoutboundauth-oauth"></a>
Use OAuth credentials for outbound authentication to the gateway.
*Required*: No
*Type*: [OAuthCredentialProvider](aws-properties-bedrockagentcore-harness-oauthcredentialprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
