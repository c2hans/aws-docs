---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2discovery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider Oauth2Discovery
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2discovery"></a>

Contains the discovery information for an OAuth2 provider.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2discovery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2discovery-syntax.json"></a>

```
{
  "[AuthorizationServerMetadata](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2discovery-authorizationservermetadata)" : {{Oauth2AuthorizationServerMetadata}},
  "[DiscoveryUrl](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2discovery-discoveryurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2discovery-syntax.yaml"></a>

```
  [AuthorizationServerMetadata](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2discovery-authorizationservermetadata): {{
    Oauth2AuthorizationServerMetadata}}
  [DiscoveryUrl](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2discovery-discoveryurl): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2discovery-properties"></a>

`AuthorizationServerMetadata`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2discovery-authorizationservermetadata"></a>
The authorization server metadata for the OAuth2 provider.
*Required*: No
*Type*: [Oauth2AuthorizationServerMetadata](aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2authorizationservermetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryUrl`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2discovery-discoveryurl"></a>
The discovery URL for the OAuth2 provider.
*Required*: No
*Type*: String
*Pattern*: `^.+/\.well-known/openid-configuration$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
