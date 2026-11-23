---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-tlsencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput TlsEncryptionConfiguration

The configuration settings for TLS encryption.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-tlsencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-tlsencryptionconfiguration-syntax.json"></a>

```json
{
  "[Public](#cfn-mediaconnect-routeroutput-tlsencryptionconfiguration-public)" : {{Json}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-tlsencryptionconfiguration-syntax.yaml"></a>

```yaml
  [Public](#cfn-mediaconnect-routeroutput-tlsencryptionconfiguration-public): {{Json}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-tlsencryptionconfiguration-properties"></a>

`Public`  <a name="cfn-mediaconnect-routeroutput-tlsencryptionconfiguration-public"></a>
The TLS encryption configuration that validates the destination by using a publicly trusted certificate authority.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
