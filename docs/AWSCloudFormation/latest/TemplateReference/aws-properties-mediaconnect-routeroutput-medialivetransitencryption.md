---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-medialivetransitencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput MediaLiveTransitEncryption
<a name="aws-properties-mediaconnect-routeroutput-medialivetransitencryption"></a>

The encryption configuration that defines how content is encrypted during transit between MediaConnect Router and MediaLive. This configuration determines whether encryption keys are automatically managed by the service or manually managed through AWS Secrets Manager.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-medialivetransitencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-medialivetransitencryption-syntax.json"></a>

```
{
  "[EncryptionKeyConfiguration](#cfn-mediaconnect-routeroutput-medialivetransitencryption-encryptionkeyconfiguration)" : {{MediaLiveTransitEncryptionKeyConfiguration}},
  "[EncryptionKeyType](#cfn-mediaconnect-routeroutput-medialivetransitencryption-encryptionkeytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-medialivetransitencryption-syntax.yaml"></a>

```
  [EncryptionKeyConfiguration](#cfn-mediaconnect-routeroutput-medialivetransitencryption-encryptionkeyconfiguration): {{
    MediaLiveTransitEncryptionKeyConfiguration}}
  [EncryptionKeyType](#cfn-mediaconnect-routeroutput-medialivetransitencryption-encryptionkeytype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-medialivetransitencryption-properties"></a>

`EncryptionKeyConfiguration`  <a name="cfn-mediaconnect-routeroutput-medialivetransitencryption-encryptionkeyconfiguration"></a>
The configuration details for the MediaLive encryption key.
*Required*: Yes
*Type*: [MediaLiveTransitEncryptionKeyConfiguration](aws-properties-mediaconnect-routeroutput-medialivetransitencryptionkeyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionKeyType`  <a name="cfn-mediaconnect-routeroutput-medialivetransitencryption-encryptionkeytype"></a>
The type of encryption key to use for MediaLive transit encryption.
*Required*: No
*Type*: String
*Allowed values*: `SECRETS_MANAGER | AUTOMATIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
