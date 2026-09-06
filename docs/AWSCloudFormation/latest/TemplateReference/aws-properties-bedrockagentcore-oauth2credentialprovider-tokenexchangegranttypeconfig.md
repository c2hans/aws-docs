---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider TokenExchangeGrantTypeConfig
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig"></a>

<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-description"></a>The `TokenExchangeGrantTypeConfig` property type specifies Property description not available. for an [AWS::BedrockAgentCore::OAuth2CredentialProvider](aws-resource-bedrockagentcore-oauth2credentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-syntax.json"></a>

```
{
  "[ActorTokenContent](#cfn-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-actortokencontent)" : {{String}},
  "[ActorTokenScopes](#cfn-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-actortokenscopes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-syntax.yaml"></a>

```
  [ActorTokenContent](#cfn-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-actortokencontent): {{String}}
  [ActorTokenScopes](#cfn-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-actortokenscopes): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-properties"></a>

`ActorTokenContent`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-actortokencontent"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | M2M | AWS_IAM_ID_TOKEN_JWT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ActorTokenScopes`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-tokenexchangegranttypeconfig-actortokenscopes"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
