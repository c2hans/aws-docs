---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ApiKeyCredentialProvider
<a name="aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider"></a>

An API key credential provider for gateway authentication. This structure contains the configuration for authenticating with the target endpoint using an API key.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider-syntax.json"></a>

```
{
  "[CredentialLocation](#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentiallocation)" : {{String}},
  "[CredentialParameterName](#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialparametername)" : {{String}},
  "[CredentialPrefix](#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialprefix)" : {{String}},
  "[ProviderArn](#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-providerarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider-syntax.yaml"></a>

```
  [CredentialLocation](#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentiallocation): {{String}}
  [CredentialParameterName](#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialparametername): {{String}}
  [CredentialPrefix](#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialprefix): {{String}}
  [ProviderArn](#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-providerarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider-properties"></a>

`CredentialLocation`  <a name="cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentiallocation"></a>
The location of the API key credential. This field specifies where in the request the API key should be placed.
*Required*: No
*Type*: String
*Allowed values*: `HEADER | QUERY_PARAMETER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialParameterName`  <a name="cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialparametername"></a>
The name of the credential parameter for the API key. This parameter name is used when sending the API key to the target endpoint.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialPrefix`  <a name="cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialprefix"></a>
The prefix for the API key credential. This prefix is added to the API key when sending it to the target endpoint.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderArn`  <a name="cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-providerarn"></a>
The Amazon Resource Name (ARN) of the API key credential provider. This ARN identifies the provider in AWS.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:([^:]*):([^:]*):([^:]*):([0-9]{12})?:(.+)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
