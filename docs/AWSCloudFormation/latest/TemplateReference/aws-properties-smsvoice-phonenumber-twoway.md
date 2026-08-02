---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-phonenumber-twoway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::PhoneNumber TwoWay
<a name="aws-properties-smsvoice-phonenumber-twoway"></a>

The phone number's two-way SMS configuration object.

## Syntax
<a name="aws-properties-smsvoice-phonenumber-twoway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-phonenumber-twoway-syntax.json"></a>

```
{
  "[ChannelArn](#cfn-smsvoice-phonenumber-twoway-channelarn)" : {{String}},
  "[ChannelRole](#cfn-smsvoice-phonenumber-twoway-channelrole)" : {{String}},
  "[Enabled](#cfn-smsvoice-phonenumber-twoway-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-smsvoice-phonenumber-twoway-syntax.yaml"></a>

```
  [ChannelArn](#cfn-smsvoice-phonenumber-twoway-channelarn): {{String}}
  [ChannelRole](#cfn-smsvoice-phonenumber-twoway-channelrole): {{String}}
  [Enabled](#cfn-smsvoice-phonenumber-twoway-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-smsvoice-phonenumber-twoway-properties"></a>

`ChannelArn`  <a name="cfn-smsvoice-phonenumber-twoway-channelarn"></a>
The Amazon Resource Name (ARN) of the two way channel.
*Required*: No
*Type*: String
*Pattern*: `^arn:\S+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelRole`  <a name="cfn-smsvoice-phonenumber-twoway-channelrole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
*Required*: No
*Type*: String
*Pattern*: `^arn:\S+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-smsvoice-phonenumber-twoway-enabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
