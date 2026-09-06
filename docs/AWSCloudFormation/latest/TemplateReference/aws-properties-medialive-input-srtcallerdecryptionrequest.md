---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-srtcallerdecryptionrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input SrtCallerDecryptionRequest
<a name="aws-properties-medialive-input-srtcallerdecryptionrequest"></a>

The decryption settings for an SRT caller source. Complete these parameters only if the content is encrypted.

The parent of this entity is SrtCallerSourceRequest.

## Syntax
<a name="aws-properties-medialive-input-srtcallerdecryptionrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-srtcallerdecryptionrequest-syntax.json"></a>

```
{
  "[Algorithm](#cfn-medialive-input-srtcallerdecryptionrequest-algorithm)" : {{String}},
  "[PassphraseSecretArn](#cfn-medialive-input-srtcallerdecryptionrequest-passphrasesecretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-srtcallerdecryptionrequest-syntax.yaml"></a>

```
  [Algorithm](#cfn-medialive-input-srtcallerdecryptionrequest-algorithm): {{String}}
  [PassphraseSecretArn](#cfn-medialive-input-srtcallerdecryptionrequest-passphrasesecretarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-srtcallerdecryptionrequest-properties"></a>

`Algorithm`  <a name="cfn-medialive-input-srtcallerdecryptionrequest-algorithm"></a>
The algorithm used to encrypt content.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PassphraseSecretArn`  <a name="cfn-medialive-input-srtcallerdecryptionrequest-passphrasesecretarn"></a>
The ARN for the secret in Secrets Manager. Someone in your organization must create a secret and provide you with its ARN. This secret holds the passphrase that MediaLive will use to decrypt the source content.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
