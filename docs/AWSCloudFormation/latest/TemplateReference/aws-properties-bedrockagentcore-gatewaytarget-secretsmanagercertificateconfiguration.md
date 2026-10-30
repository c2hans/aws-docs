---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget SecretsManagerCertificateConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration"></a>

<a name="aws-properties-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration-description"></a>The `SecretsManagerCertificateConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::GatewayTarget](aws-resource-bedrockagentcore-gatewaytarget.md).

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration-syntax.json"></a>

```
{
  "[SecretArn](#cfn-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration-syntax.yaml"></a>

```
  [SecretArn](#cfn-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration-secretarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration-properties"></a>

`SecretArn`  <a name="cfn-bedrockagentcore-gatewaytarget-secretsmanagercertificateconfiguration-secretarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
