---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider OnBehalfOfTokenExchangeConfig
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig"></a>

<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-description"></a>The `OnBehalfOfTokenExchangeConfig` property type specifies Property description not available. for an [AWS::BedrockAgentCore::OAuth2CredentialProvider](aws-resource-bedrockagentcore-oauth2credentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-syntax.json"></a>

```
{
  "[GrantType](#cfn-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-granttype)" : {{String}},
  "[TokenExchangeGrantTypeConfig](#cfn-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-tokenexchangegranttypeconfig)" : {{TokenExchangeGrantTypeConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-syntax.yaml"></a>

```
  [GrantType](#cfn-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-granttype): {{String}}
  [TokenExchangeGrantTypeConfig](#cfn-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-tokenexchangegranttypeconfig): {{
    TokenExchangeGrantTypeConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-properties"></a>

`GrantType`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-granttype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `TOKEN_EXCHANGE | JWT_AUTHORIZATION_GRANT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenExchangeGrantTypeConfig`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-onbehalfoftokenexchangeconfig-tokenexchangegranttypeconfig"></a>
Property description not available.
*Required*: No
*Type*: [TokenExchangeGrantTypeConfig](aws-properties-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
