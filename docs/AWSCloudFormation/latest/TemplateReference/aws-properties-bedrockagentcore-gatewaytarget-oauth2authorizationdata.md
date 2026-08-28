---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-oauth2authorizationdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget OAuth2AuthorizationData
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauth2authorizationdata"></a>

OAuth2-specific authorization data, including the authorization URL and user identifier for the authorization session.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauth2authorizationdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauth2authorizationdata-syntax.json"></a>

```
{
  "[AuthorizationUrl](#cfn-bedrockagentcore-gatewaytarget-oauth2authorizationdata-authorizationurl)" : {{String}},
  "[UserId](#cfn-bedrockagentcore-gatewaytarget-oauth2authorizationdata-userid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauth2authorizationdata-syntax.yaml"></a>

```
  [AuthorizationUrl](#cfn-bedrockagentcore-gatewaytarget-oauth2authorizationdata-authorizationurl): {{String}}
  [UserId](#cfn-bedrockagentcore-gatewaytarget-oauth2authorizationdata-userid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-oauth2authorizationdata-properties"></a>

`AuthorizationUrl`  <a name="cfn-bedrockagentcore-gatewaytarget-oauth2authorizationdata-authorizationurl"></a>
The URL to initiate the authorization process. This URL is provided when the OAuth2 access token requires user authorization.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserId`  <a name="cfn-bedrockagentcore-gatewaytarget-oauth2authorizationdata-userid"></a>
The user identifier associated with the OAuth2 authorization session that is defined by AgentCore Gateway.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
