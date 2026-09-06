---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-user-aftercontactworkconfigperchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User AfterContactWorkConfigPerChannel
<a name="aws-properties-connect-user-aftercontactworkconfigperchannel"></a>

Configuration settings for after contact work (ACW) timeout for a specific channel.

## Syntax
<a name="aws-properties-connect-user-aftercontactworkconfigperchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-user-aftercontactworkconfigperchannel-syntax.json"></a>

```
{
  "[AfterContactWorkConfig](#cfn-connect-user-aftercontactworkconfigperchannel-aftercontactworkconfig)" : {{AfterContactWorkConfig}},
  "[AgentFirstCallbackAfterContactWorkConfig](#cfn-connect-user-aftercontactworkconfigperchannel-agentfirstcallbackaftercontactworkconfig)" : {{AfterContactWorkConfig}},
  "[Channel](#cfn-connect-user-aftercontactworkconfigperchannel-channel)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-user-aftercontactworkconfigperchannel-syntax.yaml"></a>

```
  [AfterContactWorkConfig](#cfn-connect-user-aftercontactworkconfigperchannel-aftercontactworkconfig): {{
    AfterContactWorkConfig}}
  [AgentFirstCallbackAfterContactWorkConfig](#cfn-connect-user-aftercontactworkconfigperchannel-agentfirstcallbackaftercontactworkconfig): {{
    AfterContactWorkConfig}}
  [Channel](#cfn-connect-user-aftercontactworkconfigperchannel-channel): {{String}}
```

## Properties
<a name="aws-properties-connect-user-aftercontactworkconfigperchannel-properties"></a>

`AfterContactWorkConfig`  <a name="cfn-connect-user-aftercontactworkconfigperchannel-aftercontactworkconfig"></a>
The ACW timeout settings for this channel.
*Required*: Yes
*Type*: [AfterContactWorkConfig](aws-properties-connect-user-aftercontactworkconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentFirstCallbackAfterContactWorkConfig`  <a name="cfn-connect-user-aftercontactworkconfigperchannel-agentfirstcallbackaftercontactworkconfig"></a>
The ACW timeout settings for agent-first callbacks. This setting only applies to the VOICE channel.
*Required*: No
*Type*: [AfterContactWorkConfig](aws-properties-connect-user-aftercontactworkconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Channel`  <a name="cfn-connect-user-aftercontactworkconfigperchannel-channel"></a>
The channel for this ACW timeout configuration. Valid values: VOICE, CHAT, TASK, EMAIL.
*Required*: Yes
*Type*: String
*Allowed values*: `VOICE | CHAT | TASK | EMAIL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
