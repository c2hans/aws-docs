---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-certificateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway CertificateConfiguration

<a name="aws-properties-bedrockagentcore-gateway-certificateconfiguration-description"></a>The `CertificateConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Gateway](aws-resource-bedrockagentcore-gateway.md).

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-certificateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-certificateconfiguration-syntax.json"></a>

```json
{
  "[S3](#cfn-bedrockagentcore-gateway-certificateconfiguration-s3)" : {{S3CertificateConfiguration}},
  "[SecretsManager](#cfn-bedrockagentcore-gateway-certificateconfiguration-secretsmanager)" : {{SecretsManagerCertificateConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-certificateconfiguration-syntax.yaml"></a>

```yaml
  [S3](#cfn-bedrockagentcore-gateway-certificateconfiguration-s3): {{
    S3CertificateConfiguration}}
  [SecretsManager](#cfn-bedrockagentcore-gateway-certificateconfiguration-secretsmanager): {{
    SecretsManagerCertificateConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-certificateconfiguration-properties"></a>

`S3`  <a name="cfn-bedrockagentcore-gateway-certificateconfiguration-s3"></a>
Property description not available.
*Required*: No
*Type*: [S3CertificateConfiguration](aws-properties-bedrockagentcore-gateway-s3certificateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManager`  <a name="cfn-bedrockagentcore-gateway-certificateconfiguration-secretsmanager"></a>
Property description not available.
*Required*: No
*Type*: [SecretsManagerCertificateConfiguration](aws-properties-bedrockagentcore-gateway-secretsmanagercertificateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
