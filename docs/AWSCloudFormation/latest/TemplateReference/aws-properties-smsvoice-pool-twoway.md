---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-pool-twoway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::Pool TwoWay
<a name="aws-properties-smsvoice-pool-twoway"></a>

The pool's two-way SMS configuration object.

## Syntax
<a name="aws-properties-smsvoice-pool-twoway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-pool-twoway-syntax.json"></a>

```
{
  "[ChannelArn](#cfn-smsvoice-pool-twoway-channelarn)" : {{String}},
  "[ChannelRole](#cfn-smsvoice-pool-twoway-channelrole)" : {{String}},
  "[Enabled](#cfn-smsvoice-pool-twoway-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-smsvoice-pool-twoway-syntax.yaml"></a>

```
  [ChannelArn](#cfn-smsvoice-pool-twoway-channelarn): {{String}}
  [ChannelRole](#cfn-smsvoice-pool-twoway-channelrole): {{String}}
  [Enabled](#cfn-smsvoice-pool-twoway-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-smsvoice-pool-twoway-properties"></a>

`ChannelArn`  <a name="cfn-smsvoice-pool-twoway-channelarn"></a>
The Amazon Resource Name (ARN) of the two way channel.
*Required*: No
*Type*: String
*Pattern*: `^[ \S]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelRole`  <a name="cfn-smsvoice-pool-twoway-channelrole"></a>
An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.
*Required*: No
*Type*: String
*Pattern*: `^arn:\S+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-smsvoice-pool-twoway-enabled"></a>
By default this is set to false. When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
