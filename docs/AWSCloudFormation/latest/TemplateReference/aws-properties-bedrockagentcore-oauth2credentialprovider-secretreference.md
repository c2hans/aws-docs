---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-secretreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider SecretReference
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-secretreference"></a>

Contains a reference to a secret stored in AWS Secrets Manager.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-secretreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-secretreference-syntax.json"></a>

```
{
  "[JsonKey](#cfn-bedrockagentcore-oauth2credentialprovider-secretreference-jsonkey)" : {{String}},
  "[SecretId](#cfn-bedrockagentcore-oauth2credentialprovider-secretreference-secretid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-secretreference-syntax.yaml"></a>

```
  [JsonKey](#cfn-bedrockagentcore-oauth2credentialprovider-secretreference-jsonkey): {{String}}
  [SecretId](#cfn-bedrockagentcore-oauth2credentialprovider-secretreference-secretid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-secretreference-properties"></a>

`JsonKey`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-secretreference-jsonkey"></a>
The JSON key used to extract the secret value from the AWS Secrets Manager secret.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretId`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-secretreference-secretid"></a>
The ID of the AWS Secrets Manager secret that stores the secret value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
