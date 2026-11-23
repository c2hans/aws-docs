---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-tlsencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput TlsEncryption

The Transport Layer Security (TLS) encryption settings used to establish a secure connection to a destination.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-tlsencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-tlsencryption-syntax.json"></a>

```json
{
  "[EncryptionConfiguration](#cfn-mediaconnect-routeroutput-tlsencryption-encryptionconfiguration)" : {{TlsEncryptionConfiguration}},
  "[EncryptionType](#cfn-mediaconnect-routeroutput-tlsencryption-encryptiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-tlsencryption-syntax.yaml"></a>

```yaml
  [EncryptionConfiguration](#cfn-mediaconnect-routeroutput-tlsencryption-encryptionconfiguration): {{
    TlsEncryptionConfiguration}}
  [EncryptionType](#cfn-mediaconnect-routeroutput-tlsencryption-encryptiontype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-tlsencryption-properties"></a>

`EncryptionConfiguration`  <a name="cfn-mediaconnect-routeroutput-tlsencryption-encryptionconfiguration"></a>
The configuration settings for the specified TLS encryption type.
*Required*: Yes
*Type*: [TlsEncryptionConfiguration](aws-properties-mediaconnect-routeroutput-tlsencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionType`  <a name="cfn-mediaconnect-routeroutput-tlsencryption-encryptiontype"></a>
The type of TLS encryption to use for the connection.
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
