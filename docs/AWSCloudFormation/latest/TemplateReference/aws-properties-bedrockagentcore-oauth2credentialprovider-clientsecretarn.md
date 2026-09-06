---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider ClientSecretArn
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn"></a>

<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-description"></a>The `ClientSecretArn` property type specifies Property description not available. for an [AWS::BedrockAgentCore::OAuth2CredentialProvider](aws-resource-bedrockagentcore-oauth2credentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-syntax.json"></a>

```
{
  "[SecretArn](#cfn-bedrockagentcore-oauth2credentialprovider-clientsecretarn-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-syntax.yaml"></a>

```
  [SecretArn](#cfn-bedrockagentcore-oauth2credentialprovider-clientsecretarn-secretarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-clientsecretarn-properties"></a>

`SecretArn`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-clientsecretarn-secretarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov):secretsmanager:[A-Za-z0-9-]{1,64}:[0-9]{12}:secret:[a-zA-Z0-9-_/+=.@!]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
