---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-slackbidirectionalconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association SlackBidirectionalConfiguration

Configuration for bidirectional communication between AWS DevOps Agent and the Slack channel of this association. Use `RoleArn` to specify the IAM role that the agent assumes to handle conversations in that channel. Use `Enabled` to control whether the agent responds to mentions in that channel.

## Syntax
<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-devopsagent-association-slackbidirectionalconfiguration-enabled)" : {{Boolean}},
  "[RoleArn](#cfn-devopsagent-association-slackbidirectionalconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-devopsagent-association-slackbidirectionalconfiguration-enabled): {{Boolean}}
  [RoleArn](#cfn-devopsagent-association-slackbidirectionalconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-slackbidirectionalconfiguration-properties"></a>

`Enabled`  <a name="cfn-devopsagent-association-slackbidirectionalconfiguration-enabled"></a>
Specifies whether bidirectional communication is enabled for this association. When set to `true`, you can mention the agent in the associated Slack channel and receive responses in that channel. When omitted or set to `false`, the agent ignores mentions and only sends notifications. Bidirectional communication is supported only in private channels.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-devopsagent-association-slackbidirectionalconfiguration-rolearn"></a>
The ARN of the IAM role that AWS DevOps Agent assumes to handle conversations in the Slack channel of this association. The role authorizes the agent to create chats and send messages in your Agent Space on behalf of the users in that channel.
The role must allow the `aidevops.amazonaws.com` service principal to call `sts:AssumeRole` and `sts:TagSession`. Scope that trust policy with the `aws:SourceAccount` and `aws:SourceArn` condition keys. These keys restrict the trust to your account and your Agent Space ARN. Attach the AWS managed policy `AIDevOpsChannelAccessPolicy` to the role.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
