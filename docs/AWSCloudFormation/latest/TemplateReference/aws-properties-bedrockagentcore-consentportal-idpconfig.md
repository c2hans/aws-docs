---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-consentportal-idpconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ConsentPortal IdpConfig
<a name="aws-properties-bedrockagentcore-consentportal-idpconfig"></a>

<a name="aws-properties-bedrockagentcore-consentportal-idpconfig-description"></a>The `IdpConfig` property type specifies Property description not available. for an [AWS::BedrockAgentCore::ConsentPortal](aws-resource-bedrockagentcore-consentportal.md).

## Syntax
<a name="aws-properties-bedrockagentcore-consentportal-idpconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-consentportal-idpconfig-syntax.json"></a>

```
{
  "[Audience](#cfn-bedrockagentcore-consentportal-idpconfig-audience)" : {{String}},
  "[CredentialProviderArn](#cfn-bedrockagentcore-consentportal-idpconfig-credentialproviderarn)" : {{String}},
  "[Scopes](#cfn-bedrockagentcore-consentportal-idpconfig-scopes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-consentportal-idpconfig-syntax.yaml"></a>

```
  [Audience](#cfn-bedrockagentcore-consentportal-idpconfig-audience): {{String}}
  [CredentialProviderArn](#cfn-bedrockagentcore-consentportal-idpconfig-credentialproviderarn): {{String}}
  [Scopes](#cfn-bedrockagentcore-consentportal-idpconfig-scopes): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-consentportal-idpconfig-properties"></a>

`Audience`  <a name="cfn-bedrockagentcore-consentportal-idpconfig-audience"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialProviderArn`  <a name="cfn-bedrockagentcore-consentportal-idpconfig-credentialproviderarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):bedrock-agentcore:[a-z0-9-]{1,32}:[0-9]{12}:token-vault/[a-zA-Z0-9_-]{1,64}/oauth2credentialprovider/[a-zA-Z0-9_-]{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scopes`  <a name="cfn-bedrockagentcore-consentportal-idpconfig-scopes"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
