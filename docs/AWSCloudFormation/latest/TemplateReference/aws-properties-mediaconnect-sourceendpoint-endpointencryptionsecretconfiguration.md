---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint EndpointEncryptionSecretConfiguration
<a name="aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration"></a>

<a name="aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration-description"></a>The `EndpointEncryptionSecretConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::SourceEndpoint](aws-resource-mediaconnect-sourceendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration-syntax.json"></a>

```
{
  "[SecretArn](#cfn-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration-syntax.yaml"></a>

```
  [SecretArn](#cfn-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration-secretarn): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration-properties"></a>

`SecretArn`  <a name="cfn-mediaconnect-sourceendpoint-endpointencryptionsecretconfiguration-secretarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
