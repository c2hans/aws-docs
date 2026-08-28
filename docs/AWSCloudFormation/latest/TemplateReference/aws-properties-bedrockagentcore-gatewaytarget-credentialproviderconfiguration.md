---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget CredentialProviderConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration"></a>

The configuration for a credential provider. This structure defines how the gateway authenticates with the target endpoint.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-syntax.json"></a>

```
{
  "[CredentialProvider](#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovider)" : {{CredentialProvider}},
  "[CredentialProviderType](#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovidertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-syntax.yaml"></a>

```
  [CredentialProvider](#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovider): {{
    CredentialProvider}}
  [CredentialProviderType](#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovidertype): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-properties"></a>

`CredentialProvider`  <a name="cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovider"></a>
The credential provider. This field contains the specific configuration for the credential provider type.
*Required*: No
*Type*: [CredentialProvider](aws-properties-bedrockagentcore-gatewaytarget-credentialprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialProviderType`  <a name="cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovidertype"></a>
The type of credential provider. This field specifies which authentication method the gateway uses.
*Required*: Yes
*Type*: String
*Allowed values*: `GATEWAY_IAM_ROLE | OAUTH | API_KEY | CALLER_IAM_CREDENTIALS | JWT_PASSTHROUGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
