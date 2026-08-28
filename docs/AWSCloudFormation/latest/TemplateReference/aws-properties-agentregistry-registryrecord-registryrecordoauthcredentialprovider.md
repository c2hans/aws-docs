---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord RegistryRecordOAuthCredentialProvider
<a name="aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider"></a>

The configuration for an OAuth 2.0 credential provider that authenticates requests to a registry record's source.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider-syntax.json"></a>

```
{
  "[CustomParameters](#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-customparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[GrantType](#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-granttype)" : {{String}},
  "[ProviderArn](#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-providerarn)" : {{String}},
  "[Scopes](#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-scopes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider-syntax.yaml"></a>

```
  [CustomParameters](#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-customparameters): {{
    {{Key}}: {{Value}}}}
  [GrantType](#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-granttype): {{String}}
  [ProviderArn](#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-providerarn): {{String}}
  [Scopes](#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-scopes): {{
    - String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider-properties"></a>

`CustomParameters`  <a name="cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-customparameters"></a>
Additional parameters to include in the OAuth 2.0 token request.
*Required*: No
*Type*: Object of String
*Pattern*: `^.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GrantType`  <a name="cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-granttype"></a>
The OAuth 2.0 grant type used to obtain access tokens.
*Required*: No
*Type*: String
*Allowed values*: `CLIENT_CREDENTIALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderArn`  <a name="cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-providerarn"></a>
The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scopes`  <a name="cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-scopes"></a>
The OAuth 2.0 scopes to request when obtaining access tokens.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
