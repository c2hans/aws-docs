---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput SrtDecryptionConfiguration
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration"></a>

Contains the configuration settings for decrypting SRT streams, including the encryption key details and decryption parameters.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration-syntax.json"></a>

```
{
  "[EncryptionKey](#cfn-mediaconnect-routerinput-srtdecryptionconfiguration-encryptionkey)" : {{SecretsManagerEncryptionKeyConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration-syntax.yaml"></a>

```
  [EncryptionKey](#cfn-mediaconnect-routerinput-srtdecryptionconfiguration-encryptionkey): {{
    SecretsManagerEncryptionKeyConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration-properties"></a>

`EncryptionKey`  <a name="cfn-mediaconnect-routerinput-srtdecryptionconfiguration-encryptionkey"></a>
Specifies the encryption key configuration used for decrypting SRT streams, including the key source and associated credentials.
*Required*: Yes
*Type*: [SecretsManagerEncryptionKeyConfiguration](aws-properties-mediaconnect-routerinput-secretsmanagerencryptionkeyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
