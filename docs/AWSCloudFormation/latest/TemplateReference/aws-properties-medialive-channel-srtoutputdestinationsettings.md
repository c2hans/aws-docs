---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-srtoutputdestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel SrtOutputDestinationSettings
<a name="aws-properties-medialive-channel-srtoutputdestinationsettings"></a>

SRT output destination settings.

## Syntax
<a name="aws-properties-medialive-channel-srtoutputdestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-srtoutputdestinationsettings-syntax.json"></a>

```
{
  "[ConnectionMode](#cfn-medialive-channel-srtoutputdestinationsettings-connectionmode)" : {{String}},
  "[EncryptionPassphraseSecretArn](#cfn-medialive-channel-srtoutputdestinationsettings-encryptionpassphrasesecretarn)" : {{String}},
  "[ListenerPort](#cfn-medialive-channel-srtoutputdestinationsettings-listenerport)" : {{Integer}},
  "[StreamId](#cfn-medialive-channel-srtoutputdestinationsettings-streamid)" : {{String}},
  "[Url](#cfn-medialive-channel-srtoutputdestinationsettings-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-srtoutputdestinationsettings-syntax.yaml"></a>

```
  [ConnectionMode](#cfn-medialive-channel-srtoutputdestinationsettings-connectionmode): {{String}}
  [EncryptionPassphraseSecretArn](#cfn-medialive-channel-srtoutputdestinationsettings-encryptionpassphrasesecretarn): {{String}}
  [ListenerPort](#cfn-medialive-channel-srtoutputdestinationsettings-listenerport): {{Integer}}
  [StreamId](#cfn-medialive-channel-srtoutputdestinationsettings-streamid): {{String}}
  [Url](#cfn-medialive-channel-srtoutputdestinationsettings-url): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-srtoutputdestinationsettings-properties"></a>

`ConnectionMode`  <a name="cfn-medialive-channel-srtoutputdestinationsettings-connectionmode"></a>
Specifies the mode the output should use for connection establishment. CALLER mode requires URL, LISTENER mode requires port.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionPassphraseSecretArn`  <a name="cfn-medialive-channel-srtoutputdestinationsettings-encryptionpassphrasesecretarn"></a>
Arn used to extract the password from Secrets Manager.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListenerPort`  <a name="cfn-medialive-channel-srtoutputdestinationsettings-listenerport"></a>
Port number for listener mode connections (required when connectionMode is LISTENER, must not be provided when connectionMode is CALLER).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-medialive-channel-srtoutputdestinationsettings-streamid"></a>
Stream id for SRT destinations (URLs of type srt://).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-medialive-channel-srtoutputdestinationsettings-url"></a>
A URL specifying a destination.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
