---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-certificateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider CertificateConfiguration
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-certificateconfiguration"></a>

<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-description"></a>The `CertificateConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::OAuth2CredentialProvider](aws-resource-bedrockagentcore-oauth2credentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-syntax.json"></a>

```
{
  "[S3](#cfn-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-s3)" : {{S3CertificateConfiguration}},
  "[SecretsManager](#cfn-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-secretsmanager)" : {{SecretsManagerCertificateConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-syntax.yaml"></a>

```
  [S3](#cfn-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-s3): {{
    S3CertificateConfiguration}}
  [SecretsManager](#cfn-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-secretsmanager): {{
    SecretsManagerCertificateConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-properties"></a>

`S3`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-s3"></a>
Property description not available.
*Required*: No
*Type*: [S3CertificateConfiguration](aws-properties-bedrockagentcore-oauth2credentialprovider-s3certificateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManager`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-certificateconfiguration-secretsmanager"></a>
Property description not available.
*Required*: No
*Type*: [SecretsManagerCertificateConfiguration](aws-properties-bedrockagentcore-oauth2credentialprovider-secretsmanagercertificateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
