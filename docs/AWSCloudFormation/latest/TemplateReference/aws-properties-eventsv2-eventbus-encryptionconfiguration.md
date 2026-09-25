---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventbus-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventBus EncryptionConfiguration
<a name="aws-properties-eventsv2-eventbus-encryptionconfiguration"></a>

Encryption configuration for an event bus.

## Syntax
<a name="aws-properties-eventsv2-eventbus-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventbus-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyIdentifier](#cfn-eventsv2-eventbus-encryptionconfiguration-kmskeyidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventbus-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyIdentifier](#cfn-eventsv2-eventbus-encryptionconfiguration-kmskeyidentifier): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-eventbus-encryptionconfiguration-properties"></a>

`KmsKeyIdentifier`  <a name="cfn-eventsv2-eventbus-encryptionconfiguration-kmskeyidentifier"></a>
The identifier of the AWS KMS customer managed key that the event bus uses to encrypt events. You can specify the key ARN, key ID, alias name, or alias ARN. If you do not specify a key, EventBridge uses an AWS owned key.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-/:]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
