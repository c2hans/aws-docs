---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider Oauth2AuthorizationServerMetadata
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata"></a>

Contains the authorization server metadata for an OAuth2 provider.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-syntax.json"></a>

```
{
  "[AuthorizationEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-authorizationendpoint)" : {{String}},
  "[Issuer](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-issuer)" : {{String}},
  "[ResponseTypes](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-responsetypes)" : {{[ String, ... ]}},
  "[TokenEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-tokenendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-syntax.yaml"></a>

```
  [AuthorizationEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-authorizationendpoint): {{String}}
  [Issuer](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-issuer): {{String}}
  [ResponseTypes](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-responsetypes): {{
    - String}}
  [TokenEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-tokenendpoint): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-properties"></a>

`AuthorizationEndpoint`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-authorizationendpoint"></a>
The authorization endpoint URL for the OAuth2 authorization server.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-issuer"></a>
The issuer URL for the OAuth2 authorization server.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponseTypes`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-responsetypes"></a>
The supported response types for the OAuth2 authorization server.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenEndpoint`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata-tokenendpoint"></a>
The token endpoint URL for the OAuth2 authorization server.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
