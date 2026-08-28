---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-credentialprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget CredentialProvider
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialprovider"></a>

A credential provider for gateway authentication. This structure contains the configuration for authenticating with the target endpoint.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialprovider-syntax.json"></a>

```
{
  "[ApiKeyCredentialProvider](#cfn-bedrockagentcore-gatewaytarget-credentialprovider-apikeycredentialprovider)" : {{ApiKeyCredentialProvider}},
  "[IamCredentialProvider](#cfn-bedrockagentcore-gatewaytarget-credentialprovider-iamcredentialprovider)" : {{IamCredentialProvider}},
  "[OauthCredentialProvider](#cfn-bedrockagentcore-gatewaytarget-credentialprovider-oauthcredentialprovider)" : {{OAuthCredentialProvider}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialprovider-syntax.yaml"></a>

```
  [ApiKeyCredentialProvider](#cfn-bedrockagentcore-gatewaytarget-credentialprovider-apikeycredentialprovider): {{
    ApiKeyCredentialProvider}}
  [IamCredentialProvider](#cfn-bedrockagentcore-gatewaytarget-credentialprovider-iamcredentialprovider): {{
    IamCredentialProvider}}
  [OauthCredentialProvider](#cfn-bedrockagentcore-gatewaytarget-credentialprovider-oauthcredentialprovider): {{
    OAuthCredentialProvider}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-credentialprovider-properties"></a>

`ApiKeyCredentialProvider`  <a name="cfn-bedrockagentcore-gatewaytarget-credentialprovider-apikeycredentialprovider"></a>
The API key credential provider. This provider uses an API key to authenticate with the target endpoint.
*Required*: No
*Type*: [ApiKeyCredentialProvider](aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamCredentialProvider`  <a name="cfn-bedrockagentcore-gatewaytarget-credentialprovider-iamcredentialprovider"></a>
The IAM credential provider. This provider uses IAM authentication with SigV4 signing to access the target endpoint.
*Required*: No
*Type*: [IamCredentialProvider](aws-properties-bedrockagentcore-gatewaytarget-iamcredentialprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OauthCredentialProvider`  <a name="cfn-bedrockagentcore-gatewaytarget-credentialprovider-oauthcredentialprovider"></a>
The OAuth credential provider. This provider uses OAuth authentication to access the target endpoint.
*Required*: No
*Type*: [OAuthCredentialProvider](aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
