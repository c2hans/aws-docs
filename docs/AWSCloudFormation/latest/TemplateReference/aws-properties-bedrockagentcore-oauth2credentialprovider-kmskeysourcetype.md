---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider KmsKeySourceType
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype"></a>

<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-description"></a>The `KmsKeySourceType` property type specifies Property description not available. for an [AWS::BedrockAgentCore::OAuth2CredentialProvider](aws-resource-bedrockagentcore-oauth2credentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-properties"></a>

`KmsKeyArn`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-kmskeysourcetype-kmskeyarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
