---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmcontacts-plan-channeltargetinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMContacts::Plan ChannelTargetInfo
<a name="aws-properties-ssmcontacts-plan-channeltargetinfo"></a>

Information about the contact channel that Incident Manager uses to engage the contact.

## Syntax
<a name="aws-properties-ssmcontacts-plan-channeltargetinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmcontacts-plan-channeltargetinfo-syntax.json"></a>

```
{
  "[ChannelId](#cfn-ssmcontacts-plan-channeltargetinfo-channelid)" : {{String}},
  "[RetryIntervalInMinutes](#cfn-ssmcontacts-plan-channeltargetinfo-retryintervalinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ssmcontacts-plan-channeltargetinfo-syntax.yaml"></a>

```
  [ChannelId](#cfn-ssmcontacts-plan-channeltargetinfo-channelid): {{String}}
  [RetryIntervalInMinutes](#cfn-ssmcontacts-plan-channeltargetinfo-retryintervalinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-ssmcontacts-plan-channeltargetinfo-properties"></a>

`ChannelId`  <a name="cfn-ssmcontacts-plan-channeltargetinfo-channelid"></a>
The Amazon Resource Name (ARN) of the contact channel.
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryIntervalInMinutes`  <a name="cfn-ssmcontacts-plan-channeltargetinfo-retryintervalinminutes"></a>
The number of minutes to wait before retrying to send engagement if the engagement initially failed.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
