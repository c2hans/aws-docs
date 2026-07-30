---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-user-voiceenhancementconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User VoiceEnhancementConfig
<a name="aws-properties-connect-user-voiceenhancementconfig"></a>

Configuration settings for voice enhancement.

## Syntax
<a name="aws-properties-connect-user-voiceenhancementconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-user-voiceenhancementconfig-syntax.json"></a>

```
{
  "[Channel](#cfn-connect-user-voiceenhancementconfig-channel)" : {{String}},
  "[VoiceEnhancementMode](#cfn-connect-user-voiceenhancementconfig-voiceenhancementmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-user-voiceenhancementconfig-syntax.yaml"></a>

```
  [Channel](#cfn-connect-user-voiceenhancementconfig-channel): {{String}}
  [VoiceEnhancementMode](#cfn-connect-user-voiceenhancementconfig-voiceenhancementmode): {{String}}
```

## Properties
<a name="aws-properties-connect-user-voiceenhancementconfig-properties"></a>

`Channel`  <a name="cfn-connect-user-voiceenhancementconfig-channel"></a>
The channel for this voice enhancement configuration. **Only `VOICE` is supported for this data type.**
*Required*: Yes
*Type*: String
*Allowed values*: `VOICE | CHAT | TASK | EMAIL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VoiceEnhancementMode`  <a name="cfn-connect-user-voiceenhancementconfig-voiceenhancementmode"></a>
The voice enhancement mode.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | VOICE_ISOLATION | NOISE_SUPPRESSION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
