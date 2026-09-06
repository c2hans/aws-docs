---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-chatbot-slackchannelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Chatbot::SlackChannelConfiguration
<a name="aws-resource-chatbot-slackchannelconfiguration"></a>

**Note**
AWS Chatbot is now Amazon Q Developer. [Learn more](https://docs.aws.amazon.com/chatbot/latest/adminguide/service-rename.html)
`Type` attribute values remain unchanged.

The `AWS::Chatbot::SlackChannelConfiguration` resource configures a Slack channel to allow users to use Amazon Q Developer with CloudFormation templates.

This resource requires some setup to be done in the Amazon Q Developer in chat applications console. To provide the required Slack workspace ID, you must perform the initial authorization flow with Slack in the Amazon Q Developer in chat applications console, then copy and paste the workspace ID from the console. For more details, see steps 1-3 in [Tutorial: Get started with Slack](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html#slack-client-setup) in the *Amazon Q Developer in chat applications User Guide*.

## Syntax
<a name="aws-resource-chatbot-slackchannelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-chatbot-slackchannelconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::Chatbot::SlackChannelConfiguration",
  "Properties" : {
      "[ConfigurationName](#cfn-chatbot-slackchannelconfiguration-configurationname)" : {{String}},
      "[CustomizationResourceArns](#cfn-chatbot-slackchannelconfiguration-customizationresourcearns)" : {{[ String, ... ]}},
      "[GuardrailPolicies](#cfn-chatbot-slackchannelconfiguration-guardrailpolicies)" : {{[ String, ... ]}},
      "[IamRoleArn](#cfn-chatbot-slackchannelconfiguration-iamrolearn)" : {{String}},
      "[LoggingLevel](#cfn-chatbot-slackchannelconfiguration-logginglevel)" : {{String}},
      "[SlackChannelId](#cfn-chatbot-slackchannelconfiguration-slackchannelid)" : {{String}},
      "[SlackWorkspaceId](#cfn-chatbot-slackchannelconfiguration-slackworkspaceid)" : {{String}},
      "[SnsTopicArns](#cfn-chatbot-slackchannelconfiguration-snstopicarns)" : {{[ String, ... ]}},
      "[Tags](#cfn-chatbot-slackchannelconfiguration-tags)" : {{[ Tag, ... ]}},
      "[UserRoleRequired](#cfn-chatbot-slackchannelconfiguration-userrolerequired)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-chatbot-slackchannelconfiguration-syntax.yaml"></a>

```
Type: AWS::Chatbot::SlackChannelConfiguration
Properties:
  [ConfigurationName](#cfn-chatbot-slackchannelconfiguration-configurationname): {{String}}
  [CustomizationResourceArns](#cfn-chatbot-slackchannelconfiguration-customizationresourcearns): {{
    - String}}
  [GuardrailPolicies](#cfn-chatbot-slackchannelconfiguration-guardrailpolicies): {{
    - String}}
  [IamRoleArn](#cfn-chatbot-slackchannelconfiguration-iamrolearn): {{String}}
  [LoggingLevel](#cfn-chatbot-slackchannelconfiguration-logginglevel): {{String}}
  [SlackChannelId](#cfn-chatbot-slackchannelconfiguration-slackchannelid): {{String}}
  [SlackWorkspaceId](#cfn-chatbot-slackchannelconfiguration-slackworkspaceid): {{String}}
  [SnsTopicArns](#cfn-chatbot-slackchannelconfiguration-snstopicarns): {{
    - String}}
  [Tags](#cfn-chatbot-slackchannelconfiguration-tags): {{
    - Tag}}
  [UserRoleRequired](#cfn-chatbot-slackchannelconfiguration-userrolerequired): {{Boolean}}
```

## Properties
<a name="aws-resource-chatbot-slackchannelconfiguration-properties"></a>

`ConfigurationName`  <a name="cfn-chatbot-slackchannelconfiguration-configurationname"></a>
The name of the configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomizationResourceArns`  <a name="cfn-chatbot-slackchannelconfiguration-customizationresourcearns"></a>
Links a list of resource ARNs (for example, custom action ARNs) to a Slack channel configuration for Amazon Q Developer.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GuardrailPolicies`  <a name="cfn-chatbot-slackchannelconfiguration-guardrailpolicies"></a>
The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamRoleArn`  <a name="cfn-chatbot-slackchannelconfiguration-iamrolearn"></a>
The ARN of the IAM role that defines the permissions for Amazon Q Developer.
This is a user-defined role that Amazon Q Developer will assume. This is not the service-linked role. For more information, see [IAM Policies for Amazon Q Developerin chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoggingLevel`  <a name="cfn-chatbot-slackchannelconfiguration-logginglevel"></a>
Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs.
Logging levels include `ERROR`, `INFO`, or `NONE`.
*Required*: No
*Type*: String
*Pattern*: `^(ERROR|INFO|NONE)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlackChannelId`  <a name="cfn-chatbot-slackchannelconfiguration-slackchannelid"></a>
The ID of the Slack channel.
To get the ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the character string at the end of the URL. For example, `ABCBBLZZZ`.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlackWorkspaceId`  <a name="cfn-chatbot-slackchannelconfiguration-slackworkspaceid"></a>
The ID of the Slack workspace authorized with Amazon Q Developer.
To get the workspace ID, you must perform the initial authorization flow with Slack in the Amazon Q Developer in chat applications console. Then you can copy and paste the workspace ID from the console. For more details, see steps 1-3 in [Tutorial: Get started with Slack](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html#slack-client-setup) in the *Amazon Q Developer in chat applications User Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Z]{1,255}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnsTopicArns`  <a name="cfn-chatbot-slackchannelconfiguration-snstopicarns"></a>
The ARNs of the SNS topics that deliver notifications to Amazon Q Developer.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-chatbot-slackchannelconfiguration-tags"></a>
The tags to add to the configuration.
*Required*: No
*Type*: Array of [Tag](aws-properties-chatbot-slackchannelconfiguration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserRoleRequired`  <a name="cfn-chatbot-slackchannelconfiguration-userrolerequired"></a>
Enables use of a user role requirement in your chat configuration.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-chatbot-slackchannelconfiguration-return-values"></a>

### Ref
<a name="aws-resource-chatbot-slackchannelconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the ARN of the configuration created.

### Fn::GetAtt
<a name="aws-resource-chatbot-slackchannelconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-chatbot-slackchannelconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the resource.

## Remarks
<a name="aws-resource-chatbot-slackchannelconfiguration--remarks"></a>

Common troubleshooting scenarios:
+  *I don't have a workspace ID.*

  If you don't have a workspace ID, you must perform the initial authorization flow in the Amazon Q Developer in chat applications console. Then you will be able to copy and paste the workspace ID from the console. For more details, see steps 1-3 in [Tutorial: Get started with Slack](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html#slack-client-setup) in the *Amazon Q Developer in chat applications Administrator Guide*.
+  *I have already done the initial authorization for my workspace. Do I need to do it again?*

  No, you can use your existing workspace. You must log into the Amazon Q Developer in chat applications console to get the workspace ID.
