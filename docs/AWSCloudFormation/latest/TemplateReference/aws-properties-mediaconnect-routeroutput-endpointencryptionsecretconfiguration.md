---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-endpointencryptionsecretconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput EndpointEncryptionSecretConfiguration
<a name="aws-properties-mediaconnect-routeroutput-endpointencryptionsecretconfiguration"></a>

<a name="aws-properties-mediaconnect-routeroutput-endpointencryptionsecretconfiguration-description"></a>The `EndpointEncryptionSecretConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::RouterOutput](aws-resource-mediaconnect-routeroutput.md).

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-endpointencryptionsecretconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-endpointencryptionsecretconfiguration-syntax.json"></a>

```
{
  "[SecretArn](#cfn-mediaconnect-routeroutput-endpointencryptionsecretconfiguration-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-endpointencryptionsecretconfiguration-syntax.yaml"></a>

```
  [SecretArn](#cfn-mediaconnect-routeroutput-endpointencryptionsecretconfiguration-secretarn): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-endpointencryptionsecretconfiguration-properties"></a>

`SecretArn`  <a name="cfn-mediaconnect-routeroutput-endpointencryptionsecretconfiguration-secretarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
