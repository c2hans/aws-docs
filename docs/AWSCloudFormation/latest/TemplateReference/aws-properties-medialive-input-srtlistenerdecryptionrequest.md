---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-srtlistenerdecryptionrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input SrtListenerDecryptionRequest
<a name="aws-properties-medialive-input-srtlistenerdecryptionrequest"></a>

The decryption settings for an SRT listener input. Decryption is required for all SRT listener inputs for security reasons.

The parent of this entity is SrtListenerSettingsRequest.

## Syntax
<a name="aws-properties-medialive-input-srtlistenerdecryptionrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-srtlistenerdecryptionrequest-syntax.json"></a>

```
{
  "[Algorithm](#cfn-medialive-input-srtlistenerdecryptionrequest-algorithm)" : {{String}},
  "[PassphraseSecretArn](#cfn-medialive-input-srtlistenerdecryptionrequest-passphrasesecretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-srtlistenerdecryptionrequest-syntax.yaml"></a>

```
  [Algorithm](#cfn-medialive-input-srtlistenerdecryptionrequest-algorithm): {{String}}
  [PassphraseSecretArn](#cfn-medialive-input-srtlistenerdecryptionrequest-passphrasesecretarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-srtlistenerdecryptionrequest-properties"></a>

`Algorithm`  <a name="cfn-medialive-input-srtlistenerdecryptionrequest-algorithm"></a>
Required. The decryption algorithm.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PassphraseSecretArn`  <a name="cfn-medialive-input-srtlistenerdecryptionrequest-passphrasesecretarn"></a>
Required. The ARN for the secret in Secrets Manager that holds the passphrase.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
