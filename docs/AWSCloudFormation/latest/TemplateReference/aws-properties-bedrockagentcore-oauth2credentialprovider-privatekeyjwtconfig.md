---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider PrivateKeyJwtConfig
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig"></a>

<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-description"></a>The `PrivateKeyJwtConfig` property type specifies Property description not available. for an [AWS::BedrockAgentCore::OAuth2CredentialProvider](aws-resource-bedrockagentcore-oauth2credentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-syntax.json"></a>

```
{
  "[AdditionalHeaderClaims](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-additionalheaderclaims)" : {{{{{Key}}: {{Value}}, ...}}},
  "[AdditionalPayloadClaims](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-additionalpayloadclaims)" : {{{{{Key}}: {{Value}}, ...}}},
  "[PrivateKeySource](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-privatekeysource)" : {{PrivateKeySource}},
  "[SigningAlgorithm](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-signingalgorithm)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-syntax.yaml"></a>

```
  [AdditionalHeaderClaims](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-additionalheaderclaims): {{
    {{Key}}: {{Value}}}}
  [AdditionalPayloadClaims](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-additionalpayloadclaims): {{
    {{Key}}: {{Value}}}}
  [PrivateKeySource](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-privatekeysource): {{
    PrivateKeySource}}
  [SigningAlgorithm](#cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-signingalgorithm): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-properties"></a>

`AdditionalHeaderClaims`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-additionalheaderclaims"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[A-Za-z0-9_.:#-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdditionalPayloadClaims`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-additionalpayloadclaims"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[A-Za-z0-9_.:#-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateKeySource`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-privatekeysource"></a>
Property description not available.
*Required*: No
*Type*: [PrivateKeySource](aws-properties-bedrockagentcore-oauth2credentialprovider-privatekeysource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SigningAlgorithm`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-privatekeyjwtconfig-signingalgorithm"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `RS256 | PS256 | ES256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
