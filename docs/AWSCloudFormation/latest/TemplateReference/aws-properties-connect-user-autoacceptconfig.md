---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-user-autoacceptconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User AutoAcceptConfig
<a name="aws-properties-connect-user-autoacceptconfig"></a>

Configuration settings for auto-accept for a specific channel.

## Syntax
<a name="aws-properties-connect-user-autoacceptconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-user-autoacceptconfig-syntax.json"></a>

```
{
  "[AgentFirstCallbackAutoAccept](#cfn-connect-user-autoacceptconfig-agentfirstcallbackautoaccept)" : {{Boolean}},
  "[AutoAccept](#cfn-connect-user-autoacceptconfig-autoaccept)" : {{Boolean}},
  "[Channel](#cfn-connect-user-autoacceptconfig-channel)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-user-autoacceptconfig-syntax.yaml"></a>

```
  [AgentFirstCallbackAutoAccept](#cfn-connect-user-autoacceptconfig-agentfirstcallbackautoaccept): {{Boolean}}
  [AutoAccept](#cfn-connect-user-autoacceptconfig-autoaccept): {{Boolean}}
  [Channel](#cfn-connect-user-autoacceptconfig-channel): {{String}}
```

## Properties
<a name="aws-properties-connect-user-autoacceptconfig-properties"></a>

`AgentFirstCallbackAutoAccept`  <a name="cfn-connect-user-autoacceptconfig-agentfirstcallbackautoaccept"></a>
Indicates whether auto-accept is enabled for agent-first callbacks. This setting only applies to the VOICE channel.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoAccept`  <a name="cfn-connect-user-autoacceptconfig-autoaccept"></a>
Indicates whether auto-accept is enabled for this channel. When enabled, available agents are automatically connected to contacts from this channel.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Channel`  <a name="cfn-connect-user-autoacceptconfig-channel"></a>
The channel for this auto-accept configuration. Valid values: VOICE, CHAT, TASK, EMAIL.
*Required*: Yes
*Type*: String
*Allowed values*: `VOICE | CHAT | TASK | EMAIL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
