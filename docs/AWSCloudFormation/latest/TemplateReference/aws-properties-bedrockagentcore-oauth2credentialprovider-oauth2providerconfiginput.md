---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider Oauth2ProviderConfigInput
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput"></a>

Contains the input configuration for an OAuth2 provider.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-syntax.json"></a>

```
{
  "[AtlassianOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-atlassianoauth2providerconfig)" : {{AtlassianOauth2ProviderConfigInput}},
  "[CustomOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-customoauth2providerconfig)" : {{CustomOauth2ProviderConfigInput}},
  "[GithubOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-githuboauth2providerconfig)" : {{GithubOauth2ProviderConfigInput}},
  "[GoogleOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-googleoauth2providerconfig)" : {{GoogleOauth2ProviderConfigInput}},
  "[IncludedOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-includedoauth2providerconfig)" : {{IncludedOauth2ProviderConfigInput}},
  "[LinkedinOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-linkedinoauth2providerconfig)" : {{LinkedinOauth2ProviderConfigInput}},
  "[MicrosoftOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-microsoftoauth2providerconfig)" : {{MicrosoftOauth2ProviderConfigInput}},
  "[SalesforceOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-salesforceoauth2providerconfig)" : {{SalesforceOauth2ProviderConfigInput}},
  "[SlackOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-slackoauth2providerconfig)" : {{SlackOauth2ProviderConfigInput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-syntax.yaml"></a>

```
  [AtlassianOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-atlassianoauth2providerconfig): {{
    AtlassianOauth2ProviderConfigInput}}
  [CustomOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-customoauth2providerconfig): {{
    CustomOauth2ProviderConfigInput}}
  [GithubOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-githuboauth2providerconfig): {{
    GithubOauth2ProviderConfigInput}}
  [GoogleOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-googleoauth2providerconfig): {{
    GoogleOauth2ProviderConfigInput}}
  [IncludedOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-includedoauth2providerconfig): {{
    IncludedOauth2ProviderConfigInput}}
  [LinkedinOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-linkedinoauth2providerconfig): {{
    LinkedinOauth2ProviderConfigInput}}
  [MicrosoftOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-microsoftoauth2providerconfig): {{
    MicrosoftOauth2ProviderConfigInput}}
  [SalesforceOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-salesforceoauth2providerconfig): {{
    SalesforceOauth2ProviderConfigInput}}
  [SlackOauth2ProviderConfig](#cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-slackoauth2providerconfig): {{
    SlackOauth2ProviderConfigInput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-properties"></a>

`AtlassianOauth2ProviderConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-atlassianoauth2providerconfig"></a>
Configuration settings for Atlassian OAuth2 provider integration.
*Required*: No
*Type*: [AtlassianOauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-atlassianoauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomOauth2ProviderConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-customoauth2providerconfig"></a>
The configuration for a custom OAuth2 provider.
*Required*: No
*Type*: [CustomOauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-customoauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GithubOauth2ProviderConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-githuboauth2providerconfig"></a>
The configuration for a GitHub OAuth2 provider.
*Required*: No
*Type*: [GithubOauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-githuboauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GoogleOauth2ProviderConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-googleoauth2providerconfig"></a>
The configuration for a Google OAuth2 provider.
*Required*: No
*Type*: [GoogleOauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-googleoauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludedOauth2ProviderConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-includedoauth2providerconfig"></a>
The configuration for a non-custom OAuth2 provider. This includes settings for supported OAuth2 providers that have built-in integration support.
*Required*: No
*Type*: [IncludedOauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-includedoauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkedinOauth2ProviderConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-linkedinoauth2providerconfig"></a>
Configuration settings for LinkedIn OAuth2 provider integration.
*Required*: No
*Type*: [LinkedinOauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-linkedinoauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MicrosoftOauth2ProviderConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-microsoftoauth2providerconfig"></a>
The configuration for a Microsoft OAuth2 provider.
*Required*: No
*Type*: [MicrosoftOauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-microsoftoauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SalesforceOauth2ProviderConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-salesforceoauth2providerconfig"></a>
The configuration for a Salesforce OAuth2 provider.
*Required*: No
*Type*: [SalesforceOauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-salesforceoauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlackOauth2ProviderConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-oauth2providerconfiginput-slackoauth2providerconfig"></a>
The configuration for a Slack OAuth2 provider.
*Required*: No
*Type*: [SlackOauth2ProviderConfigInput](aws-properties-bedrockagentcore-oauth2credentialprovider-slackoauth2providerconfiginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
