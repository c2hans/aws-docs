---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-privateendpointoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider PrivateEndpointOverride
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privateendpointoverride"></a>

A mapping of a specific domain to a private endpoint for secure connectivity through a VPC Lattice resource configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-syntax.json"></a>

```
{
  "[Domain](#cfn-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-domain)" : {{String}},
  "[PrivateEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-privateendpoint)" : {{PrivateEndpoint}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-syntax.yaml"></a>

```
  [Domain](#cfn-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-domain): {{String}}
  [PrivateEndpoint](#cfn-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-privateendpoint): {{
    PrivateEndpoint}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-properties"></a>

`Domain`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-domain"></a>
The domain to override with a private endpoint.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpoint`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-privateendpointoverride-privateendpoint"></a>
The private endpoint configuration for the specified domain.
*Required*: Yes
*Type*: [PrivateEndpoint](aws-properties-bedrockagentcore-oauth2credentialprovider-privateendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
