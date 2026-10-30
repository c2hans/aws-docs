---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-certificateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget CertificateConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-certificateconfiguration"></a>

<a name="aws-properties-bedrockagentcore-gatewaytarget-certificateconfiguration-description"></a>The `CertificateConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::GatewayTarget](aws-resource-bedrockagentcore-gatewaytarget.md).

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-certificateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-certificateconfiguration-syntax.json"></a>

```
{
  "[S3](#cfn-bedrockagentcore-gatewaytarget-certificateconfiguration-s3)" : {{S3CertificateConfiguration}},
  "[SecretsManager](#cfn-bedrockagentcore-gatewaytarget-certificateconfiguration-secretsmanager)" : {{SecretsManagerCertificateConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-certificateconfiguration-syntax.yaml"></a>

```
  [S3](#cfn-bedrockagentcore-gatewaytarget-certificateconfiguration-s3): {{
    S3CertificateConfiguration}}
  [SecretsManager](#cfn-bedrockagentcore-gatewaytarget-certificateconfiguration-secretsmanager): {{
    SecretsManagerCertificateConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-certificateconfiguration-properties"></a>

`S3`  <a name="cfn-bedrockagentcore-gatewaytarget-certificateconfiguration-s3"></a>
Property description not available.
*Required*: No
*Type*: [S3CertificateConfiguration](aws-properties-bedrockagentcore-gatewaytarget-s3certificateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManager`  <a name="cfn-bedrockagentcore-gatewaytarget-certificateconfiguration-secretsmanager"></a>
Property description not available.
*Required*: No
*Type*: [SecretsManagerCertificateConfiguration](aws-properties-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
